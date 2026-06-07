# NoCloudGPT Website

This repository contains the public website for **NoCloudGPT** — a private AI deployment platform that helps businesses and individuals run powerful open-source models on infrastructure they control.

## What is NoCloudGPT?

NoCloudGPT makes private AI simple. It provides a **single-script deployment** experience using Ollama + OpenWebUI, so users can run ChatGPT-style interfaces privately without becoming Linux administrators or paying ongoing API fees.

The platform focuses on:
- True data privacy (nothing leaves your server)
- Simple one-command installation
- Clear guidance on which models to use
- Flexible deployment (on-premise or private cloud)

## Site Structure

| Path                    | Purpose                                      |
|-------------------------|----------------------------------------------|
| `index.html`            | Main homepage                                |
| `/menu/`                | Model family catalog (70+ families)          |
| `/deploy/`              | Deployment guides (including 90-day pilot)   |
| `pricing.html`          | Platform tiers + Compute tiers               |
| `quote.html`            | Interactive quote builder                    |
| `contact.html`          | Contact form                                 |

## Current Focus

We are building a high-quality, **buyer-focused model catalog** under `/menu/`.

Every model family page is designed to answer:
1. What is this model family good at?
2. Who should choose it?
3. What NoCloudGPT deployment tier makes sense?

The site emphasizes **simplicity and honesty**:
- Clear hardware recommendations using intuitive labels (Nano AI, Starter AI, Standard AI, Professional AI, Heavy AI)
- No raw AWS pricing or confusing infrastructure details on family pages
- Strong focus on real-world use cases instead of technical hype

## 90-Day Free Pilot

Small business owners can launch a fully private AI instance on **AWS Lightsail** at no cost for the first 90 days using our guided deployment process.

## Technology

- Static HTML + Tailwind CSS
- Mobile-friendly, clean design
- Formspree for contact handling
- SEO-optimized with proper metadata and canonical URLs

## Important Documentation

Before editing catalog pages, please read:

- `AGENT.md` — Agent / Cursor editing instructions
- `COPYWRITING.md` — Sales voice and preferred language
- `MODEL_MENU_PLAYBOOK.md` — Page structure standards and batch priorities

All model catalog work should be done under the `/menu/` directory.

## Domain

Live site: [https://nocloudgpt.com](https://nocloudgpt.com)

## Status

Active development. The model catalog under `/menu/` is the current priority.
