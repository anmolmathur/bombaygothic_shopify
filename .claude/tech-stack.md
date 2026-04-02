# BOMBAY GOTHIC — Tech Stack & Dev Reference

## WEBSITES
| Site | URL | Platform |
|---|---|---|
| Main Brand Site | https://bombaygothic.com | Static HTML/CSS |
| Shop | https://shop.bombaygothic.com | Shopify (Dawn Theme — custom) |

---

## SHOPIFY SETUP
- **Theme:** Dawn (Shopify default) with custom modifications
- **Local Code Path:** `/Users/anmolmathur/documents/github/bombaygothic_shopify`
- **Deployment:** Currently manual push via Shopify CLI
- **Key Customized Areas:**
  - `sections/header.liquid` — custom mega menu
  - `sections/announcement-bar.liquid` — custom announcement bar
  - `assets/component-mega-menu.css` — mega menu styling
  - `mega-menu-preview.html` — preview file for custom menu
  - `assets/bombay-bohemian.jpg`, `where-line-meets-colour.jpg` — custom brand assets

### Directory Structure
```
bombaygothic_shopify/
├── assets/          # CSS, JS, SVGs, brand images
├── config/          # Theme settings (settings_schema.json, settings_data.json)
├── layout/          # theme.liquid (base layout)
├── locales/         # Translation strings
├── sections/        # Page sections (header, footer, product, collection, etc.)
├── snippets/        # Reusable Liquid snippets
└── templates/       # Page templates (product, collection, blog, etc.)
```

### Shopify CLI Commands
```bash
# Login and connect to store
shopify auth login --store shop.bombaygothic.com

# Push theme to Shopify (development)
shopify theme push --development

# Push to live theme
shopify theme push

# Watch for changes (live preview)
shopify theme dev --store shop.bombaygothic.com

# Pull latest theme from Shopify
shopify theme pull
```

### Recommended: Switch to GitHub CI/CD
Currently pushing manually. Recommended to set up:
1. Shopify GitHub integration (Settings > Apps > GitHub)
2. Auto-deploy on push to `main` branch
3. Use `shopify theme check` for lint before push

---

## MAIN SITE
- **Code Path:** `/Users/anmolmathur/documents/github/bombaygothic`
- **Tech:** Static HTML + CSS (no framework)
- **Pages:** index, aboutus, consultancy, heritagewalks, journal, contact
- **Images:** `/images/` folder

---

## ANALYTICS & TRACKING
- **Platform:** Shopify built-in analytics
- **TODO:** Set up Google Analytics 4 (GA4)
- **TODO:** Meta Pixel for Instagram/Facebook ad attribution
- **TODO:** Google Search Console for SEO monitoring

---

## SEO OPPORTUNITIES (identified)
- Product pages: improve meta titles and descriptions
- Blog/Journal: more frequent posts with heritage keywords
  - Target keywords: "Bombay heritage gifts", "Mumbai architectural art", "Gothic Mumbai products", "heritage gifts Mumbai"
- Image alt text: most product images likely missing alt text
- Schema markup: add Product schema for rich snippets

---

## INSTAGRAM
- **Handle:** @bombay_gothic
- **Ad Budget:** ₹30,000/month
- **Current Gap:** No structured content calendar or campaign strategy documented
- **TODO:** Build monthly content calendar (product + story + educational posts)

---

## PENDING SHOPIFY TASKS (from Krti voice memo discussion)
1. **Product Images** — standardize across all products (consistent background, sizing, aspect ratio)
2. **Product Tagging** — improve tag taxonomy for filtering and collections
3. **Categories** — review and refine Shopify collection structure
4. **Curated Sets / Bundles** — create gift bundles (e.g., "The Bombay Morning Set", "Heritage Home Kit")
5. **Instagram Campaign** — build campaign structure for ₹30K/month spend

---

## FUTURE TECH CONSIDERATIONS
- **WhatsApp Business API** — for order updates and gifting inquiries
- **Email Marketing** — Klaviyo or Mailchimp integration with Shopify
- **Review App** — Loox or Judge.me for product reviews
- **Wishlist App** — for repeat visitors
- **International Shipping** — configure Shopify shipping zones for UK, USA, UAE
