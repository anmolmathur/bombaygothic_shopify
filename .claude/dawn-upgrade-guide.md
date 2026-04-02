# Dawn 15.4 → 15.4.1 Upgrade Guide — Bombay Gothic

## Overview
Current: Dawn 15.4 (last saved Feb 15, 2026)
Target: Dawn 15.4.1
This is a minor patch upgrade, so changes should be minimal. But we have significant customizations to protect.

---

## STEP-BY-STEP UPGRADE PROCESS

### Step 1: Backup (BEFORE anything)
```bash
cd /Users/anmolmathur/documents/github/bombaygothic_shopify
git add -A && git commit -m "Pre-upgrade backup: Dawn 15.4 with all customizations"
shopify theme pull --store shop.bombaygothic.com
git add -A && git commit -m "Pulled latest live theme state before upgrade"
```

### Step 2: Duplicate Theme in Shopify Admin
1. Go to Online Store → Themes
2. Click "..." on Dawn 15.4 → Duplicate
3. Name it "Dawn 15.4 — Backup (DO NOT DELETE)"

### Step 3: Apply Update to a TEST Copy
1. Create another duplicate of the live theme
2. Apply the 15.4.1 update to this duplicate only
3. Preview it — check all pages before publishing

### Step 4: Pull Updated Theme & Diff
```bash
# Create a branch for the upgrade
git checkout -b upgrade-15.4.1

# Pull the updated (test) theme
shopify theme pull --theme [TEST-THEME-ID] --store shop.bombaygothic.com

# Diff against main to see what 15.4.1 changed
git diff main -- . ':!.claude' ':!Bombay Gothic'
```

### Step 5: Re-apply Customizations if Overwritten
Check each file below and restore customizations if the upgrade overwrote them.

### Step 6: Test & Publish
1. Preview every page type (home, product, collection, cart, blog)
2. Test mega menu on desktop + mobile
3. Test checkout flow
4. If all good → publish

---

## CUSTOM FILES ADDED (safe — won't be affected by upgrade)

| File | Purpose |
|---|---|
| `snippets/collection-based-recommendations.liquid` | Collection-based "You may also like" |
| `snippets/header-mega-menu.liquid` | Custom mega menu snippet |
| `sections/collection-grid.liquid` | Homepage collection grid |
| `sections/announcement-bar-backup.liquid` | Backup of original announcement bar |
| `assets/bombay-bohemian.jpg` | Brand image |
| `assets/where-line-meets-colour.jpg` | Brand image |
| `assets/icon-cart1.svg` | Alternative cart icon |
| `assets/icon-cart-empty1.svg` | Alternative empty cart icon |
| `assets/component-mega-menu.css` | Mega menu styling |
| `mega-menu-preview.html` | Dev preview file |
| `test-announcement.html` | Dev test file |

---

## MODIFIED STOCK FILES (need careful merge)

### CRITICAL — Must Preserve These Customizations:

**`sections/header.liquid`** (3 commits of changes)
- Custom mega menu implementation
- Logo URL update
- Renders `header-mega-menu.liquid` snippet
- Organization + WebSite JSON-LD schema
- **Risk: HIGH** — if 15.4.1 updates header.liquid, manual merge needed

**`snippets/header-drawer.liquid`**
- Custom mobile drawer menu
- **Risk: MEDIUM**

**`sections/main-product.liquid`**
- Enhanced Product JSON-LD schema (our new addition)
- **Risk: LOW** — our changes are at the end of file, unlikely to conflict

**`sections/related-products.liquid`**
- Collection-based recommendations (our new addition)
- **Risk: LOW** — significant rewrite but self-contained

**`assets/icon-cart.svg` + `icon-cart-empty.svg`**
- Custom cart icons
- **Risk: LOW** — unlikely to change in patch

**`config/settings_data.json`**
- All brand colors (#aa4837 rust, #f8f9f2 cream)
- Raleway fonts
- Logo, favicon
- Section configurations
- **Risk: MEDIUM** — settings structure might change, values must be preserved

**`config/settings_schema.json`**
- Custom schema definitions
- **Risk: LOW**

### Lower Risk Modified Files:
- 30 section files (mostly stock with minor theme config)
- 11 snippet files
- 13 CSS files
- 7 JS files
- 5 template JSON files
- 30+ locale files

Most of these were bulk-updated during the 15.0→15.4 upgrade and are likely stock. The 15.4→15.4.1 patch should only touch a handful.

---

## POST-UPGRADE VERIFICATION CHECKLIST

- [ ] Homepage loads correctly with announcement bar
- [ ] Mega menu works on desktop (all dropdowns)
- [ ] Mobile hamburger menu works
- [ ] Product pages show correct layout
- [ ] "More from [collection]" recommendations appear
- [ ] Product JSON-LD schema present (check page source)
- [ ] Collection pages display correctly
- [ ] Cart drawer / notification works
- [ ] Checkout flow completes
- [ ] Brand colors correct (rust #aa4837, cream #f8f9f2)
- [ ] Raleway font loads for headings and body
- [ ] Logo displays correctly
- [ ] Footer renders correctly
- [ ] Blog/Journal pages work
- [ ] Mobile responsive on all page types
