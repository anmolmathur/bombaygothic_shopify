# BOMBAY GOTHIC — Weekly Task Tracker

## HOW TO USE THIS FILE
- Claude updates this file at the start of every Cowork session
- Completed tasks get marked ✅ with date
- New tasks get added with priority: 🔴 High | 🟡 Medium | 🟢 Low
- Source tags: [KM] = Kruti Meeting Mar 29 | [GS] = Google Sheet To Do | [CA] = Code Audit | [AM] = Anmol

---

## CURRENT WEEK: Week of April 2, 2026 (Prep Month — Week 1)

**Context:** Year 1 starts May 1, 2026. April = preparation month. Gold copy for all product data = "Product catalog Jan 2026" (on laptop) + "Product description Jan 2026.docx". Product photos on BombayGothic Google Drive (organized by series).

---

### 🔴 HIGH PRIORITY — Product Display Fixes (Shopify Admin)

These are the most visible customer-facing issues. Most are tagging/collection fixes done in Shopify Admin, not code.

| # | Task | Source | Details |
|---|---|---|---|
| 1 | **Mugs — show color variants as individual products** | [KM][GS] | Red, yellow, green, pink mugs must each appear as separate product cards in collection (not behind "Choose Options"). Split variants into individual products. |
| 2 | **Flasks — add Lancet Line products to Flasks category** | [KM] | Lancet Line flasks (On Civic Duty Flask etc.) not appearing in Flasks collection. Fix tagging. |
| 3 | **Flasks — show all flasks with swatches/names individually** | [GS] | Each flask should appear as its own product in collection page (ref: kinavuliving.com example). |
| 4 | **Notebooks — show as individual products** | [KM][GS] | Split notebook/diary variants into individual product listings. Add "Notes After Dark Diary" + "Between the Lines Journal". |
| 5 | **Notebooks — fix Starry Night notebook tagging** | [KM] | Starry Night notebook not appearing under Notebooks & Notepads category. Fix collection tagging. |
| 6 | **Coasters — fix missing variants** | [KM] | Red coaster and black/white coaster not appearing alongside others. Fix tagging so all coaster variants show. |
| 7 | **Design Series page — add missing 3rd & 4th series** | [KM][GS] | Only 2 of 4 series showing. Add "Starry Starry Night" + "The Lancet Line" to Design Series section and menu. |
| 8 | **Out-of-stock flasks — remove or mark appropriately** | [KM] | Some flasks are out of stock. Either hide them or add "Sold Out" badge. |
| 9 | **Update inventory/stock levels for all products** | [KM] | Ensure stock counts are accurate across all products. |

---

### 🔴 HIGH PRIORITY — Product Data Updates (Bulk)

| # | Task | Source | Details |
|---|---|---|---|
| 10 | **Rename all products to new titles** | [GS] | 55 products have old → new title mapping in Google Sheet "Product Details" tab. |
| 11 | **Update all product descriptions from Jan 2026 gold copy** | [KM][GS] | Use Google Sheet "Product Details" + "Product description Jan 2026.docx" (saved in `.claude/product-descriptions-jan2026.md`). |
| 12 | **Upload 9 new product descriptions from docx** | [GS] | Starry Starry Night (4 products) + Lancet Line (5 products) — full specs, materials, care instructions in `.claude/product-descriptions-jan2026.md`. |
| 13 | **Update product prices** | [GS] | 15 products have updated Selling Price + MRP in Google Sheet. |
| 14 | **Update SKUs for all new products** | [GS] | New SKUs needed for Starry Starry Night, Lancet Line, and other new additions. |
| 15 | **Add 4 collection descriptions** | [GS] | Bombay Bohemian, Where Line Meets Colour, Starry Starry Night, The Lancet Line — full descriptions ready in Google Sheet "Collection Details" tab. |
| 16 | **Check Champagne glass descriptions are complete** | [KM] | Follow-up from meeting — verify City Sparkling Champagne Glasses have full descriptions. |

---

### 🔴 HIGH PRIORITY — Theme Upgrade

| # | Task | Source | Details |
|---|---|---|---|
| 17 | **Upgrade Dawn theme 15.4 → 15.4.1** | [AM] | Update available (shown in Shopify admin). **MUST preserve all customizations:** custom mega menu (`header.liquid`, `header-mega-menu.liquid`, `component-mega-menu.css`), custom announcement bar, brand color schemes (#aa4837 rust, #f8f9f2 cream), Raleway fonts, all settings_data.json config. **Process:** (1) Backup current theme via `shopify theme pull`, (2) Create a duplicate theme in Shopify admin, (3) Apply 15.4.1 update to the duplicate, (4) Diff the updated theme against current to identify conflicts, (5) Re-apply customizations, (6) Test on preview before publishing. |

---

### 🟡 MEDIUM PRIORITY — Store Features & UX

| # | Task | Source | Details |
|---|---|---|---|
| 18 | ✅ **Fix "You may also like" recommendations** | [KM][GS] | DONE Apr 2 — Rewrote `related-products.liquid` + created `collection-based-recommendations.liquid`. Now shows "More from [series]" with Shopify native recs as fallback. |
| 19 | ✅ **Create "Curated Sets" category** | [KM][GS] | DONE Apr 2 — Created `product.curated-set.json` template with Enquire (email) + WhatsApp buttons instead of Add to Cart. Assign template to set products in Shopify admin. |
| 20 | **Add new ceramic mugs under Where Line Meets Colour** | [KM] | Restocked, different size. Add as variants. |
| 21 | **Fix homepage blogs** | [GS] | 2 blogs on shop.bombaygothic.com need review/fix (clarify specifics). |
| 22 | ✅ **Add Instagram feed app to homepage** | [GS] | DONE Apr 2 — Created custom `instagram-feed.liquid` section + CSS. Added to homepage. Upload 4 Instagram images via Shopify theme customizer. |
| 23 | **Change support/contact chat smiley icon** | [GS] | Update chat widget icon. |
| 24 | **Add more blogs to Journal page** | [GS][KM] | Journal section needs fresh content. Also update journal photos from Google Drive (pending 4-6 months). |
| 25 | **Update art frame images** | [KM] | Tegeshi has updated the old images. Replace on Shopify. |
| 26 | **Update notebook/diary main images** | [KM] | Use red diary image with white background from Google Drive. |

---

### 🟡 MEDIUM PRIORITY — Navigation & Menu

| # | Task | Source | Details |
|---|---|---|---|
| 27 | **Implement full navigation structure from Google Sheet** | [GS] | Header mega menu: Shop → By Category / By Collection / By Styles, Services (Heritage Walks, Art Installations, Consultancy), Journal (Stories, Inspiration Board, Blogs), About (Our Story, About the Founder), Help (Bulk Order, FAQs, Shipping, Returns, Contact, My Account). |
| 28 | **Set up footer per Google Sheet** | [GS] | About Us section (Our Story, About the Founder, Journal, Work with Us), Help section (Bulk Order, FAQs, Contact Us, Shipping, Privacy, Returns, T&C, My Account), Collections section (all collections listed), Newsletter signup. |

---

### 🟡 MEDIUM PRIORITY — SEO & Code Improvements

| # | Task | Source | Details |
|---|---|---|---|
| 29 | ✅ **Add Product JSON-LD schema markup** | [CA] | DONE Apr 2 — Enhanced schema added to `main-product.liquid` with brand, images, SKU, offers, availability. |
| 30 | ✅ **Activate related products section** | [CA] | DONE Apr 2 — Rewrote with collection-based matching logic. |
| 31 | ✅ **Update product page meta titles & descriptions** | [CA] | DONE Apr 2 — Created `seo-meta.liquid` snippet with auto-generated optimized meta tags for all page types. Added to `theme.liquid`. |
| 32 | **Install product reviews app** | [CA] | Judge.me recommended (free tier). Adds social proof + review schema. |

---

### 🟡 MEDIUM PRIORITY — Marketing & Outreach

| # | Task | Source | Details |
|---|---|---|---|
| 33 | **Draft Instagram campaign strategy (₹30K/month)** | [KM] | ₹1,000/day budget. Strategy needed for April-May. Extend the March strategy that was already done for one month. |
| 34 | **Send first 5 media pitches** | [CA] | Fiona Fernandez (Mid-Day), Esha Gupta (Design Pataki), The Better India, Payal Khandelwal, Deepali Nandwani. Contacts researched and in outreach-log.md. |

---

### 🟢 LOW PRIORITY — Analytics, Email & Future

| # | Task | Source | Details |
|---|---|---|---|
| 35 | **Set up Google Analytics 4** | [CA] | Not currently on the Shopify store. |
| 36 | **Set up Meta Pixel** | [CA] | Needed for Instagram/Facebook ad attribution. |
| 37 | **Set up Google Search Console** | [CA] | SEO monitoring. |
| 38 | **Draft "Letters from Bombay" newsletter template** | [CA] | Monthly newsletter concept. |
| 39 | **Prepare Lancet Line pipeline products** | [GS] | Teacups & Saucers, Quarter Plates B&W, Tealights — descriptions TBD. |
| 40 | **Review curated sets pricing & bundling strategy** | [KM] | Needs pricing decision before adding to website. |
| 41 | **Review WhatsApp chat (BombayGothic group)** | [KM] | May have additional product updates and instructions. |

---

## APRIL PREP MONTH — WEEKLY PLAN

### Week 1 (Apr 2–6): Audit + Theme Upgrade Prep
- Complete audit (✅ done)
- ✅ Enhanced Product JSON-LD schema added to product pages (Apr 2)
- ✅ Related products "More from [series]" logic implemented (Apr 2) — fixes task #18 & #30
- ✅ Dawn 15.4.1 upgrade guide created with full risk assessment (Apr 2)
- ✅ 6 blog articles extracted, formatted, and ready for upload (Apr 2)
- ✅ Product update data prepared: 49 renames + 40 descriptions (Apr 2)
- ✅ Bulk update script created (`scripts/shopify-bulk-update.py`) (Apr 2)
- ✅ All code changes committed and pushed to GitHub (Apr 2, commits 1fe82c8, c578555, 1cd315d)
- ✅ Instagram feed section created and added to homepage (Apr 2)
- ✅ Curated Sets template with Enquire + WhatsApp buttons (Apr 2)
- ✅ SEO meta snippet for all page types added to theme.liquid (Apr 2)
- ✅ Homepage updated: added Starry Starry Night + Lancet Line featured collections (Apr 2)
- ✅ Bulk update script ready (scripts/shopify-bulk-update.py)
- 🔲 Push theme to Shopify store via CLI
- 🔲 Create Shopify Admin API app for bulk updates
- 🔲 Run product rename + description bulk update (49 renames, 40 descriptions)
- 🔲 Fix collection display (mugs, flasks, notebooks as individual products)
- 🔲 Upload Instagram images to feed section via theme customizer

### Week 2 (Apr 7–13): Product Data & Display Fixes
- Complete all product renames, descriptions, and price updates
- Fix all collection/tagging issues (items 1-9)
- Add missing Design Series to menu
- Install reviews app
- Create Curated Sets collection shell

### Week 3 (Apr 14–20): Features & Content
- Fix "You may also like" (code change)
- Add product schema markup (code change)
- Instagram feed app installation
- Update journal photos + art frame images
- Draft Instagram campaign strategy for April-May

### Week 4 (Apr 21–30): Polish & Launch Prep
- Complete Dawn 15.4.1 upgrade (test + publish)
- Navigation restructure (mega menu + footer per sheet)
- GA4 + Meta Pixel + Search Console live
- Final store QA — checkout, mobile, page speed
- Send media pitches
- Draft May 1 "Year 1 Launch" Instagram campaign

---

## BACKLOG
- Set up Shopify GitHub CI/CD (auto-deploy on push to main)
- Configure international shipping zones (UK, USA, UAE) — Year 1 Q3+
- Install Klaviyo for email marketing
- Apply for Kala Ghoda Arts Festival stall (check next cycle deadline)
- Research TEDx Mumbai application process
- Draft coffee table book concept document — Year 3
- Create corporate gifting catalog PDF — Year 2
- Build Heritage Walk booking page on website
- Add newsletter pop-up (exit intent) to store
- Add inventory countdown ("Only X left") for low-stock items

---

## COMPLETED
- ✅ 2026-04-02: Full Shopify theme code audit (Dawn v15.4.0 — identified schema, reviews, related products as quick wins)
- ✅ 2026-04-02: Revenue roadmap updated — Year 1 starts May 1, 2026; April prep milestones added
- ✅ 2026-04-02: Media contact research — 10+ contacts across 9 publications + 2 freelancers
- ✅ 2026-04-02: Outreach log updated with researched contacts
- ✅ 2026-04-02: Google Sheet "Website Details" ingested — 12 tasks, 55 products, 4 collections, nav structure, Lancet Line pipeline
- ✅ 2026-04-02: Product description docx ingested — 9 products (Starry Starry Night + Lancet Line) with full specs
- ✅ 2026-04-02: Kruti meeting summary (Mar 29) ingested — 15 action items + 5 follow-ups consolidated

---

## DATA SOURCES REFERENCE

| Source | Location | Contents |
|---|---|---|
| Google Sheet (XLSX) | `Bombay Gothic/Website Details_Bombay Gothic.xlsx` | Navigation, 4 collection descriptions, 55 product details, Lancet Line pipeline, 12 To Do tasks |
| Product Description docx | `Bombay Gothic/Product description Jan 2026.docx` | 9 product descriptions with specs (Starry Night + Lancet Line) |
| Kruti Meeting Summary | `.claude/meeting-krti-20260329.pdf` | 15 action items, key decisions, follow-ups |
| Product Descriptions (parsed) | `.claude/product-descriptions-jan2026.md` | Clean markdown of all 9 docx product descriptions |
| Outreach Contacts | `.claude/outreach-log.md` | 10+ media contacts across 9 publications |
| Revenue Roadmap | `.claude/revenue-roadmap.md` | ₹10Cr plan, Year 1 starts May 1 2026 |
| Brand Bible | `.claude/brand-bible.md` | Full brand reference |
| Tech Stack | `.claude/tech-stack.md` | Shopify Dawn setup, CLI commands, dev reference |

---
*Last updated: 2026-04-02*
