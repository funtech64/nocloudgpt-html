# SEO & Sitemap Audit — NoCloudGPT Pricing Reconciliation

**Date:** 2026-07-17  
**Branch reviewed:** `cursor/reconcile-pricing-seo-5785` (based on `main` @ `11b4b06`)  
**Prior SEO work merged:** PR #122 (`cursor/seo-continuity-audit-9611`, commit `59faf30`)

---

## Conflicting pricing work discovered

Two independent pricing directions existed in the repository:

| Source | Branch / commit | What it attempted |
|--------|-----------------|-------------------|
| **Legacy NoCloudGPT pricing** | `fffa844` on `main` | `/pricing.html` with obsolete checkout-style packages: **$99 per model**, **Sunrise Package $299** (20 licenses), **$25/$10** add-on deployments, CTAs to `/contact.html` |
| **terminal.glass sales refresh** | `origin/tg-sales-content-refresh` (`1a8d87d`–`a18bd3a`) | Rewrote `pricing.html`, `models/pricing.html`, `models/quote.html`, and `models/deploy/index.html` toward Glass Licenses — but used draft prices (**$200/$400**), **Sunrise Group Plan**, complex tiered add-on math, and NoCloudGPT-local sales CTAs |
| **SEO continuity audit** | `59faf30` (merged to `main`) | Fixed 1,200+ broken links, metadata, favicon, sitemap (198 URLs), nav/footer on model pages — **did not reconcile pricing**; left obsolete `/pricing.html` content indexed |

**Conflict type:** Textual and strategic (competing authoritative pricing on NoCloudGPT) plus routing (sales CTAs pointed to NoCloudGPT contact instead of terminal.glass). Not a Git merge-conflict-marker situation.

---

## Final pricing decision

**terminal.glass owns authoritative pricing and sales conversion.**

Current authoritative packages (verified against https://terminal.glass/pricing/):

- **Sunrise Starter** — $199 · 2 portable Glass Licenses  
- **Sunrise Business** — $399 · 6 portable Glass Licenses  
- **Additional Glass License** — $99 · one more active supported deployment  

**NoCloudGPT role:** Educational technical brand within the terminal.glass platform. May summarize packages with clear “confirm on terminal.glass” language; must not present a competing checkout structure.

**Rejected (not restored):**

- $99 per model, $299 Sunrise Package, 20 licenses, $25/$10 deployment add-ons  
- tg-sales draft $200/$400, Sunrise Group Plan, tiered $50→$25 license decay  
- NoCloudGPT “Buy Sunrise” checkout CTAs  

---

## Pages rewritten

| URL | Treatment |
|-----|-----------|
| `/pricing.html` | **Rewritten** as “Deployment & Licensing” explainer: deployment paths, hardware/planning guidance, brief terminal.glass package summary, primary CTA → `https://terminal.glass/pricing/` |
| `/models/pricing.html` | **Rewritten** as model-catalog licensing guidance (capability tiers, Glass License rule, package summary, terminal.glass CTA) |
| `/models/quote.html` | **Rewritten** as “Deployment Fit Planner” (use case / hardware / model selection); sales step → terminal.glass |
| `/models/deploy/index.html` | **Updated** with terminal.glass deployment flow and sales CTAs |
| `/index.html` | Hero, nav, terminal.glass CTA, two-brand messaging |
| `/services.html`, `/software.html`, `/contact.html` | Nav continuity, licensing/sales path language |
| `/models/index.html` | Nav + hero CTAs aligned to deployment fit and terminal.glass pricing |
| `README.md`, `AGENT.md` | Obsolete pricing replaced with terminal.glass authoritative summary |

---

## Pages redirected

None. Established URLs preserved for backlink protection:

- `/pricing.html` — kept (educational, canonical `https://nocloudgpt.com/pricing.html`)  
- `/models/pricing.html` — kept (educational)  
- `/models/quote.html` — kept (planner, not checkout)  

---

## Pages removed from navigation

- Top-level nav item **“Pricing”** (implied NoCloudGPT checkout) removed from `index.html`, `contact.html`, `services.html`, `software.html`  
- Replaced with **Deploy** (`/models/deploy/`) and external **terminal.glass** / **terminal.glass pricing** links  
- Model catalog uses **Licensing** → `/models/pricing.html` instead of “Pricing”

---

## Pages removed from sitemap

**None.** All three legacy pricing URLs remain indexable as educational content after rewrite.

**Sitemap URL count:** 198 before → **198 after** (unchanged; `lastmod` updated to 2026-07-17 sitewide)

---

## Canonical decisions

| Page | Canonical | Notes |
|------|-----------|-------|
| `/pricing.html` | `https://nocloudgpt.com/pricing.html` | Educational; not cross-domain canonicalized to terminal.glass |
| `/models/pricing.html` | `https://nocloudgpt.com/models/pricing.html` | Educational tier guidance |
| `/models/quote.html` | `https://nocloudgpt.com/models/quote.html` | Deployment fit planner |
| All other major pages | Unchanged from SEO audit (`59faf30`) | Own nocloudgpt.com canonicals retained |

No page canonicalizes to terminal.glass solely because it contains a terminal.glass CTA.

---

## Broken links fixed

This pass did not re-run the full 1,200-link repair from PR #122; that work remains on `main`.

**Validated in this pass:**

- `xmllint --noout sitemap.xml` — **PASS**  
- All **198** sitemap `<loc>` URLs resolve to real files — **PASS**  
- No Git conflict markers (`<<<<<<<`, `>>>>>>>`) — **PASS**  
- Key pages contain `https://terminal.glass/pricing/` — **PASS**  
- Obsolete pricing patterns (`$99 per model`, `$299` Sunrise Package, 20 licenses, Sunrise Group Plan, `$200/$400` cards) — **PASS** (not found in HTML/MD)

---

## Cosmetic continuity fixes

- Unified top-level navigation: Home · Services · Models · Software · Deploy · Contact · terminal.glass  
- Footer cross-brand line: “Part of the terminal.glass platform” / terminal.glass pricing links  
- `robots.txt`: removed nonstandard `Host:` directive; kept standard Allow + Sitemap  
- `pricing.html` restyled to match `services.html` design language  
- Model catalog hero CTA: “Plan deployment fit” + “View deployment pricing” (external)

---

## Files changed

```
AGENT.md
README.md
SEO-SITEMAP-AUDIT.md
contact.html
index.html
models/deploy/index.html
models/index.html
models/pricing.html
models/quote.html
pricing.html
robots.txt
services.html
sitemap.xml
software.html
```

---

## Remaining launch blockers

1. **Model page footers** — Many model family pages still link “Get quote →” to `/models/quote.html` (now a fit planner). Acceptable for launch; optional future pass to clarify CTA copy.  
2. **Two visual themes** — Top-level pages use light styling; model catalog uses dark Tailwind. Intentional split from prior SEO audit.  
3. **`models/quote.html` form** — Planner is static (no generated output). Interactive recommendations remain future work.  
4. **Human decision:** Whether `/pricing.html` should eventually 301 to terminal.glass or remain a permanent educational URL. Current decision: **preserve URL** with educational content.

---

## URLs to submit to Google Search Console

Submit sitemap:

```
https://nocloudgpt.com/sitemap.xml
```

Priority URLs after this reconciliation:

```
https://nocloudgpt.com/
https://nocloudgpt.com/pricing.html
https://nocloudgpt.com/models/
https://nocloudgpt.com/models/deploy/
https://nocloudgpt.com/models/pricing.html
https://nocloudgpt.com/models/quote.html
https://nocloudgpt.com/services.html
https://nocloudgpt.com/software.html
https://nocloudgpt.com/contact.html
```

Checkout intent should resolve to:

```
https://terminal.glass/pricing/
```

---

## Validation commands run

```bash
xmllint --noout sitemap.xml
python3  # obsolete pricing scan, conflict markers, sitemap resolution, robots.txt
grep -c '<url>' sitemap.xml  # 198
```
