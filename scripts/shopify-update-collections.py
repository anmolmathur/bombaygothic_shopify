#!/usr/bin/env python3
"""
Bombay Gothic — Update Collection Descriptions via Shopify Admin API.

Usage:
  export SHOPIFY_ACCESS_TOKEN="your-token-here"
  python3 shopify-update-collections.py --store shop.bombaygothic.com [--dry-run]
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
import time

# Collection descriptions from Kruti's gold copy (Collections.docx)
COLLECTION_UPDATES = {
    "bombay-bohemian": {
        "title": "Bombay Bohemian",
        "body_html": "<p>Bombay Bohemian reflects a sense of freedom, creativity, and individuality that has long defined Bombay and finds resonance in its evolving urban fabric. This series presents a vibrant and eclectic visual language that mirrors the city's energy and bohemian character.</p><p>Layered in lively and earthy colours with pastel hues of terracotta, beige and coral, each product in this collection is a celebration of the city's creative spirit.</p>"
    },
    "where-line-meets-colour": {
        "title": "Where Lines Meet Colour",
        "body_html": "<p>Where Lines Meet Colour brings together historic architectural illustrations of Bombay with a contemporary, graphic sensibility. The series is defined by an architectural line drawing base punctuated with carefully placed pops of colour, unconstrained by formal artistic boundaries.</p><p>By blending the city's rich architectural legacy with the vibrancy of pop colours — yellow, green, and red accents — this series creates thoughtful, stylish products that seamlessly integrate art into everyday life.</p>"
    },
    "starry-starry-night": {
        "title": "Starry Starry Night",
        "body_html": "<p>Inspired by Vincent van Gogh's The Starry Night, reimagined through the lens of Bombay's winter evenings under clear, starlit skies. Set against deep midnight blues evoking cool sea breezes, softly lit heritage buildings, and quiet streets.</p><p>Calm, nostalgic, and quietly festive, this collection captures the magic of Kala Ghoda after dark — where warmth comes not from fireplaces, but from architecture, light, and memory.</p>"
    },
    "the-lancet-line": {
        "title": "The Lancet Line",
        "body_html": "<p>Inspired by Gothic lancet windows and Bombay's historic facades, The Lancet Line is a study in structure and restraint. Hand-sketched illustrations explore rhythm, order, and proportion through a linear, monochrome lens.</p><p>Architectural language reimagines everyday objects as quiet, considered design statements and conversation pieces.</p>"
    },
    "kala-ghoda-kaleidoscope": {
        "title": "Kala Ghoda Kaleidoscope",
        "body_html": "<p>A vibrant celebration of Mumbai's most iconic art district — Watson's Hotel, Army & Navy Building, David Sassoon Library, and Elphinstone College. This architectural cityscape captures the creative convergence that defines Kala Ghoda.</p>"
    },
    "victorian-gothic-ensemble": {
        "title": "Victorian Gothic Ensemble",
        "body_html": "<p>A continuous panorama along the Esplanade — the Old Secretariat, University of Mumbai, Rajabai Clock Tower, and the Bombay High Court. This illustration celebrates the most concentrated stretch of Victorian Gothic architecture in all of India.</p>"
    },
    "urbs-prima-in-indis": {
        "title": "Urbs Prima in Indis",
        "body_html": "<p>Victoria Terminus (CSMT), BMC Headquarters, and the Times of India Building — the landmarks that earned Bombay the title 'Urbs Prima in Indis' (First City of India). This cityscape captures the monumental ambition of 19th-century Bombay.</p>"
    },
    "the-gateway-to-india": {
        "title": "The Gateway to India",
        "body_html": "<p>The Taj Mahal Palace Hotel, Gateway of India, Prince of Wales Museum (CSMVS), and the Royal Alfred Sailors' Home — the waterfront landmarks that welcome visitors to Bombay. A cityscape where history meets the sea.</p>"
    }
}


def api_request(store, token, endpoint, method="GET", data=None):
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
        print(f"  ✗ API Error {e.code}: {e.read().decode()[:200]}")
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--store", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
    if not token:
        print("Error: Set SHOPIFY_ACCESS_TOKEN"); sys.exit(1)

    print(f"Fetching collections from {args.store}...")
    result = api_request(args.store, token, "custom_collections.json?limit=250")
    if not result:
        print("Failed to fetch collections"); sys.exit(1)

    collections = result.get("custom_collections", [])
    # Also get smart collections
    smart = api_request(args.store, token, "smart_collections.json?limit=250")
    if smart:
        collections.extend(smart.get("smart_collections", []))

    print(f"Found {len(collections)} collections.\n")

    updated = 0
    for col in collections:
        handle = col.get("handle", "")
        if handle in COLLECTION_UPDATES:
            update = COLLECTION_UPDATES[handle]
            payload = {"custom_collection": {"id": col["id"], "body_html": update["body_html"]}}

            if args.dry_run:
                print(f"  [DRY RUN] Would update: \"{col['title']}\" ({handle})")
            else:
                endpoint = f"custom_collections/{col['id']}.json"
                result = api_request(args.store, token, endpoint, "PUT", payload)
                if not result:
                    # Try smart collection endpoint
                    payload = {"smart_collection": {"id": col["id"], "body_html": update["body_html"]}}
                    result = api_request(args.store, token, f"smart_collections/{col['id']}.json", "PUT", payload)
                if result:
                    print(f"  ✓ Updated: \"{col['title']}\"")
                    updated += 1
                time.sleep(0.5)

    print(f"\nDone: {updated} collections updated.")


if __name__ == "__main__":
    main()
