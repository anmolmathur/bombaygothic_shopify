# Bombay Gothic — Navigation Setup Guide

The mega menu and footer menus need to be configured in **Shopify Admin → Online Store → Navigation**.

---

## Header Mega Menu (main-menu)

The header already uses `main-menu` with mega menu type. Update it to match:

### Shop (dropdown)
- **By Category**
  - Drinkware
  - Home & Decor
  - Accessories
  - Stationery
  - Games
  - Barware *(new)*
- **By Collection**
  - Bombay Bohemian → `/collections/bombay-bohemian`
  - Where Line Meets Colour → `/collections/where-line-meets-colour`
  - Starry Starry Night → `/collections/starry-starry-night`
  - The Lancet Line → `/collections/the-lancet-line`
- **By Style** (Architecture)
  - Kala Ghoda Kaleidoscope → `/collections/kala-ghoda-kaleidoscope`
  - Victorian Gothic Ensemble → `/collections/victorian-gothic-ensemble`
  - Urbs Prima in Indis → `/collections/urbs-prima-in-indis`
  - The Gateway to India → `/collections/the-gateway-to-india`

### Services
- Heritage Walks → `/pages/heritage-walks`
- Art Installations → `/pages/art-installations`
- Consultancy → `/pages/consultancy`

### Journal
- Stories → `/blogs/news`
- Inspiration Board → `/pages/inspiration`
- Blogs → `/blogs/news`

### About
- Our Story → `/pages/about`
- About the Founder → `/pages/founder`

### Help
- Bulk Order → `/pages/bulk-order`
- FAQs → `/pages/faqs`
- Contact Us → `/pages/contact`

---

## Footer Menus

Three menus referenced by `footer-group.json`:

### footer-about-us
- Our Story → `/pages/about`
- About the Founder → `/pages/founder`
- Journal → `/blogs/news`
- Work with Us → `/pages/contact`

### footer-help
- Bulk Order → `/pages/bulk-order`
- FAQs → `/pages/faqs`
- Contact Us → `/pages/contact`
- Shipping Policy → `/policies/shipping-policy`
- Returns & Exchanges → `/policies/refund-policy`
- Terms & Conditions → `/policies/terms-of-service`
- Privacy Policy → `/policies/privacy-policy`
- My Account → `/account`

### footer-collections
- Bombay Bohemian → `/collections/bombay-bohemian`
- Where Line Meets Colour → `/collections/where-line-meets-colour`
- Starry Starry Night → `/collections/starry-starry-night`
- The Lancet Line → `/collections/the-lancet-line`
- All Products → `/collections/all`

---

## How to Set Up in Shopify Admin

1. Go to **Online Store → Navigation**
2. Edit `main-menu` — restructure per header spec above
3. Create `footer-about-us` menu with items listed above
4. Create `footer-help` menu with items listed above
5. Create `footer-collections` menu with items listed above
6. The theme code (`footer-group.json`) already references these menu handles

**Note:** Some pages (Heritage Walks, Art Installations, FAQs, etc.) may need to be created first under **Online Store → Pages**.
