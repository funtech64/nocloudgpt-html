# Public Website Art Direction — October 2026

## Approved destinations

| Destination | Responsibility |
| --- | --- |
| https://nocloudgpt.com | Corporate and deployment education, model catalog, support navigation |
| https://shop.nocloudgpt.com | Live Shopify storefront for software orders |
| https://colors.chat | Customer-friendly redirect to the Shopify storefront |
| https://colorschat.com | COLORS.chat marketing website: Independent AI and Jets |
| https://terminal.glass | Linux, Glass Agents, Jet Agents, deployment and Glass Licenses |

An earlier September site plan called colorschat.com a YouTube hub; this is stale. YouTube is linked *from* the current marketing site.

## Artwork source of truth

1. The **published Shopify Horizon theme** is the immediate reference for this NoCloudGPT HTML visual refresh. In the live store on October 28, 2026 its settings use Inter fonts, a white (`#ffffff`) background, black (`#000000`) text and controls, dark grey (`#333333`), and light grey dividers (`#DFDFDF`).
2. The shop homepage hero uses the live Shopify file `IMG_1117.png`: https://cdn.shopify.com/s/files/1/0601/5447/8674/files/IMG_1117.png?v=1787376483 . Use the verified public CDN URL until an approved, versioned copy is imported into the static repo. Its presence in Shopify is confirmed; accessibility and visual crop still require a deployed-page check.
3. Preserve the canonical COLORS.chat Spectrum Mark and product-workspace examples in `/brand/`. Canonical SVG/palette source: `funtech64/ncgpt/art/art-manifest.json` and `art/logos/colors-chat-spectrum-mark.svg`. Accent gradient: `#06B6D4 → #0D9488 → #F59E0B`.
4. Avoid replacing the actual product screenshots with generic Shopify art: the Spectrum Mark and workspace remain evidence of the software.

## Implementation in this PR

- Main HTML marketing pages now link to the connected store directly, rather than relying on a redirect.
- The homepage features the verified Shopify hero and retains the existing COLORS.chat workspace image below.
- Shared `styles.css` adopts Horizon's neutral presentation while keeping Spectrum branding in the lockup.
- `brand/chrome.css` applies the same neutral shell to model/catalog headers.
- `scripts/catalog/chrome.py` is the generator source for catalog navigation. Keep it in sync with any changes to checked-in `models/index.html`.
- `README.md` and `AGENT.md` describe the updated site roles.
- No catalog data, model descriptions, deployment scripts, licenses, checkout settings, or advertised prices were intentionally changed.

## Review checklist

- [ ] Preview homepage desktop/mobile: image loads, crop is appropriate, headings and CTAs stay legible.
- [ ] Check the featured hero is visually suitable as a NoCloudGPT corporate-site image, not merely present in Shopify.
- [ ] Confirm the black button, white text, and checkout links meet contrast/keyboard-focus requirements.
- [ ] Visit software, services, contact, pricing, and model landing pages; test mobile header overflow and all storefront CTAs.
- [ ] Run `python3 scripts/catalog/test_catalog_build.py` and confirm catalog rebuild keeps the updated shared chrome.
- [ ] Manually sample an editorial model page and generated model detail page to verify their catalog content was not accidentally overwritten.
- [ ] Validate no accidental 404s in model links, canonical URLs, sitemap or robots behavior.
- [ ] Consider synchronizing branded image files into this repository if reliance on Shopify CDN becomes undesirable.

## Out of scope

Do not infer licensing prices from Shopify product prices: terminal.glass package terms are a separate public offer. Do not rebrand hundreds of model pages, rewrite product promises, or alter the Shopify published theme in this limited art-alignment change. A later messaging pass can align the older `Private AI` headlines on nocloudgpt.com with current `Independent AI` positioning.
