# NoCloudGPT Website

This repository contains the public website for **NoCloudGPT** — a private AI deployment platform that helps businesses and individuals run powerful open-source models on infrastructure they control.

## What is NoCloudGPT?

NoCloudGPT makes private AI simple. It provides a **single-script deployment** experience using Ollama + OpenWebUI, so users can run ChatGPT-style interfaces privately without becoming Linux administrators or paying ongoing API fees.

The platform focuses on:
- True data privacy (nothing leaves your server)
- Simple one-command installation
- Clear guidance on which models to use
- Flexible deployment across three clean options

## Deployment Options

NoCloudGPT supports three straightforward deployment paths:

| Option              | Name              | Best For                              | Positioning                  |
|---------------------|-------------------|---------------------------------------|------------------------------|
| Air-Gapped          | The Fortress      | Maximum privacy & compliance          | Zero outbound dependencies   |
| AWS Lightsail       | The Standard      | Reliability with simplicity           | Simplified Amazon power      |
| DigitalOcean        | The Greenfield    | Speed and developer experience        | Clean, fast infrastructure   |

These replace older “hybrid / on-prem / cloud” language. The goal is clarity and reduced decision fatigue for buyers.

## Site Structure

| Path              | Purpose                                      |
|-------------------|----------------------------------------------|
| `index.html`      | Main homepage                                |
| `/models/`        | Model family catalog (70+ families)          |
| `/deploy/`        | Deployment guides (including 90-day pilot)   |
| `pricing.html`    | Platform tiers + Compute tiers               |
| `quote.html`      | Interactive quote builder                    |
| `contact.html`    | Contact form                                 |

## Current Focus (Phase 1)

We are currently focused on building a high-quality, **buyer-focused model catalog** under `/models/`.

**Phase 1 Priority:** Complete and polish all non-cloud model family pages with precise, minimal edits.

Every model family page should answer:
1. What is this model family good at?
2. Who should choose it?
3. What NoCloudGPT deployment tier makes sense?

The site emphasizes **simplicity and honesty**:
- Clear hardware recommendations using intuitive labels (Nano AI, Starter AI, Standard AI, Professional AI, Heavy AI)
- No raw AWS pricing or confusing infrastructure details on family pages
- Strong focus on real-world use cases

**Note:** `pricing.html`, `quote.html`, and related sales pages are currently outdated and will be updated in **Phase 5** after Phase 1 is complete.

## 90-Day Free Pilot

Small business owners can launch a fully private AI instance on **AWS Lightsail** at no cost for the first 90 days using our guided deployment process.

## Technology

- Static HTML + Tailwind CSS
- Mobile-friendly, clean design
- Formspree for contact handling
- SEO-optimized with proper metadata and canonical URLs

## Important Documentation

Before editing catalog pages, please read:

- `AGENT.md` — Primary agent instructions and project rules (this overrides older files)
- `MODEL_FAMILY_GUIDE.md` — Editorial voice, structure, and buyer-friendly language
- `COPYWRITING.md` — Sales voice and preferred language (if present)

All model catalog work should be done under the `/models/` directory.

## Related Project: terminal.glass

`terminal.glass` is the **licensing, pricing, and deployment sales destination** for supported private AI installations, including NoCloudGPT on customer-owned infrastructure.

- Authoritative pricing: [https://terminal.glass/pricing/](https://terminal.glass/pricing/)
- NoCloudGPT explains technical fit, models, and deployment guides
- Glass Licenses enable supported NoCloudGPT deployments

## Pricing (Authoritative Source: terminal.glass)

Do not publish competing checkout or package structures on NoCloudGPT pages. Current terminal.glass packages (summary):

- **Sunrise Starter**: $199 — 2 portable Glass Licenses
- **Sunrise Business**: $399 — 6 portable Glass Licenses
- **Additional Glass License**: $99 — one more active supported deployment

Confirm current offers on [terminal.glass/pricing](https://terminal.glass/pricing/).

## Domain

Live site: [https://nocloudgpt.com](https://nocloudgpt.com)

## Status

Active development.  
**Current priority:** Phase 1 — completing the non-cloud model catalog under `/models/`.
