#!/usr/bin/env python3
"""
Bombay Gothic — Shopify Bulk Update Script
Updates product titles, descriptions, and creates blog posts via Shopify Admin API.

Usage:
  1. Get your Shopify Admin API access token from:
     Settings → Apps → Develop apps → Create app → Configure Admin API scopes
     Required scopes: write_products, write_content (for blogs)

  2. Run:
     export SHOPIFY_ACCESS_TOKEN="your-token-here"
     python3 shopify-bulk-update.py --store shop.bombaygothic.com [--dry-run]
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error

# ─── Configuration ───────────────────────────────────────────────────────────

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
PRODUCT_UPDATES_FILE = os.path.join(PROJECT_DIR, ".claude", "product-updates.json")
BLOG_ARTICLES_DIR = os.path.join(PROJECT_DIR, ".claude", "blog-articles")


def api_request(store, token, endpoint, method="GET", data=None):
    """Make a Shopify Admin API request."""
    url = f"https://{store}/admin/api/2024-01/{endpoint}"
    headers = {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
    }

    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"  ✗ API Error {e.code}: {error_body[:200]}")
        return None


def get_all_products(store, token):
    """Fetch all products (paginated)."""
    products = []
    endpoint = "products.json?limit=250&fields=id,title,body_html,handle"

    while endpoint:
        result = api_request(store, token, endpoint)
        if not result:
            break
        products.extend(result.get("products", []))
        # Simple pagination — check if we got a full page
        if len(result.get("products", [])) < 250:
            break
        last_id = products[-1]["id"]
        endpoint = f"products.json?limit=250&since_id={last_id}&fields=id,title,body_html,handle"

    return products


def update_products(store, token, dry_run=False):
    """Update product titles and descriptions."""
    print("\n═══ PRODUCT UPDATES ═══\n")

    with open(PRODUCT_UPDATES_FILE) as f:
        updates = json.load(f)

    print(f"Loading {len(updates)} product updates from gold copy...")
    print("Fetching current products from Shopify...\n")

    products = get_all_products(store, token)
    print(f"Found {len(products)} products in store.\n")

    # Build lookup by title (case-insensitive)
    product_lookup = {}
    for p in products:
        product_lookup[p["title"].upper().strip()] = p

    updated = 0
    skipped = 0
    not_found = 0

    for update in updates:
        old_title = update["old_title"].strip()
        new_title = update["new_title"].strip()
        description = update.get("description", "").strip()
        care = update.get("care_instruction", "").strip()
        material = update.get("material", "").strip()

        # Find product by old title
        product = product_lookup.get(old_title.upper())
        if not product:
            # Try partial match
            matches = [p for key, p in product_lookup.items() if old_title.upper() in key]
            if len(matches) == 1:
                product = matches[0]

        if not product:
            print(f"  ⚠ Not found: \"{old_title}\"")
            not_found += 1
            continue

        # Build update payload
        payload = {}
        if new_title and new_title != product["title"]:
            payload["title"] = new_title

        # Build rich description HTML
        if description:
            body_parts = [f"<p>{description}</p>"]
            if material:
                body_parts.append(f"<h3>Material</h3><p>{material}</p>")
            if care:
                body_parts.append(f"<h3>Care Instructions</h3><p>{care}</p>")
            body_html = "\n".join(body_parts)
            payload["body_html"] = body_html

        if not payload:
            skipped += 1
            continue

        change_desc = []
        if "title" in payload:
            change_desc.append(f"title → \"{new_title}\"")
        if "body_html" in payload:
            change_desc.append("description updated")

        if dry_run:
            print(f"  [DRY RUN] #{product['id']} \"{product['title']}\" → {', '.join(change_desc)}")
        else:
            result = api_request(store, token, f"products/{product['id']}.json", "PUT",
                                {"product": {"id": product["id"], **payload}})
            if result:
                print(f"  ✓ #{product['id']} {', '.join(change_desc)}")
                updated += 1
            else:
                print(f"  ✗ Failed: \"{old_title}\"")
            time.sleep(0.5)  # Rate limiting

    print(f"\nProduct update summary: {updated} updated, {skipped} skipped (no changes), {not_found} not found")
    return updated


def upload_blogs(store, token, dry_run=False):
    """Upload blog articles to Shopify Journal."""
    print("\n═══ BLOG ARTICLE UPLOADS ═══\n")

    # First, find or create the "Journal" blog
    result = api_request(store, token, "blogs.json")
    if not result:
        print("  ✗ Could not fetch blogs")
        return 0

    blogs = result.get("blogs", [])
    journal_blog = None
    for blog in blogs:
        if "journal" in blog["title"].lower() or "news" in blog["title"].lower():
            journal_blog = blog
            break

    if not journal_blog and blogs:
        journal_blog = blogs[0]  # Use first blog as fallback

    if not journal_blog:
        if dry_run:
            print("  [DRY RUN] Would create 'Journal' blog")
            blog_id = "NEW"
        else:
            result = api_request(store, token, "blogs.json", "POST",
                                {"blog": {"title": "Journal"}})
            if result:
                journal_blog = result["blog"]
                print(f"  ✓ Created blog: Journal (#{journal_blog['id']})")
            else:
                print("  ✗ Could not create blog")
                return 0
    else:
        print(f"  Using blog: \"{journal_blog['title']}\" (#{journal_blog['id']})")

    blog_id = journal_blog["id"] if journal_blog else "NEW"

    # Upload each article
    uploaded = 0
    article_files = sorted([f for f in os.listdir(BLOG_ARTICLES_DIR) if f.endswith(".json")])

    for filename in article_files:
        filepath = os.path.join(BLOG_ARTICLES_DIR, filename)
        with open(filepath) as f:
            article_data = json.load(f)

        payload = {
            "article": {
                "title": article_data["title"],
                "body_html": article_data["body_html"],
                "tags": ", ".join(article_data.get("tags", [])),
                "summary_html": f"<p>{article_data.get('excerpt', '')}</p>",
                "published": False,  # Create as draft first
            }
        }

        if dry_run:
            print(f"  [DRY RUN] Would create: \"{article_data['title']}\"")
        else:
            result = api_request(store, token, f"blogs/{blog_id}/articles.json", "POST", payload)
            if result:
                art = result["article"]
                print(f"  ✓ Created: \"{art['title']}\" (#{art['id']}) [DRAFT]")
                uploaded += 1
            else:
                print(f"  ✗ Failed: \"{article_data['title']}\"")
            time.sleep(0.5)

    print(f"\nBlog upload summary: {uploaded}/{len(article_files)} articles created as drafts")
    return uploaded


def main():
    parser = argparse.ArgumentParser(description="Bombay Gothic Shopify Bulk Update")
    parser.add_argument("--store", required=True, help="Shopify store domain (e.g., shop.bombaygothic.com)")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying")
    parser.add_argument("--products-only", action="store_true", help="Only update products")
    parser.add_argument("--blogs-only", action="store_true", help="Only upload blogs")
    args = parser.parse_args()

    token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
    if not token:
        print("Error: Set SHOPIFY_ACCESS_TOKEN environment variable")
        print("  Get it from: Shopify Admin → Settings → Apps → Develop apps")
        sys.exit(1)

    print(f"╔═══════════════════════════════════════════════╗")
    print(f"║  Bombay Gothic — Shopify Bulk Update          ║")
    print(f"║  Store: {args.store:<38}║")
    print(f"║  Mode: {'DRY RUN (preview only)' if args.dry_run else 'LIVE (applying changes)':<38}║")
    print(f"╚═══════════════════════════════════════════════╝")

    if not args.blogs_only:
        update_products(args.store, args.token if hasattr(args, 'token') else token, args.dry_run)

    if not args.products_only:
        upload_blogs(args.store, token, args.dry_run)

    print("\n✓ Done!")


if __name__ == "__main__":
    main()
