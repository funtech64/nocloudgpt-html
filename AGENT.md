# AGENT.md — NoCloudGPT / terminal.glass Project Rules

**Last Updated:** June 26, 2026

This file contains the standing rules for any AI coding agent (Cursor, Claude, Codex, etc.) working in this repository.

## 1. Core Principle (Most Important Rule)

When a human gives a **precise, single-file edit instruction**, you must follow it **exactly and minimally**.

Examples of precise instructions:
- “Insert only this exact section after the closing `</section>` of the amber trade-off block”
- “Replace only the CTA button text with this exact string”
- “Add this paragraph immediately before the footer”

**You are forbidden from:**
- Scanning flat lists (`NoCloudGPT-FLAT-LIST.MD`, `cloud-page-flat-list.md`, etc.)
- Reporting global status (“X pages already have this section”)
- Deciding on your own whether something is “already done”
- Performing extra cleanup, verification, or refactoring unless explicitly asked
- Outputting full files when only a small insertion was requested

Precise user instructions **always override** this guide, `MODEL_FAMILY_GUIDE.md`, and any flat lists.

## 2. Project Structure

- Root (`/`) — Main marketing site (`index.html`, `pricing.html`, `software.html`, etc.)
- `/models/` — All model family pages live here as folders (`/models/llama/`, `/models/deepseek/`, etc.)
  - Each model family uses `index.html` inside its folder
  - Cloud variants use the `-cloud` suffix (e.g. `gemma3-cloud/`)
- Supporting files:
  - `MODEL_FAMILY_GUIDE.md` — Editorial voice and structure rules (secondary to precise user instructions)
  - Flat lists (`NoCloudGPT-FLAT-LIST.MD`, `cloud-page-flat-list.md`) — Human reference only

## 3. Current Phase (June 2026)

**Phase 1 (Current Focus):**  
Clean and complete all non-cloud model family pages in `/models/`.  
This means precise, minimal section insertions and copy improvements only.

**Phase 5 (Later):**  
Update outdated pages including `pricing.html`, `quote.html`, and related sales/quote flows.  
Do **not** work on Phase 5 until a human explicitly says Phase 1 is complete.

## 4. New Marketing Direction (terminal.glass)

terminal.glass is being repositioned as a **deterministic, one-script deployment platform** for SEO AI workers and MLOps professionals who want headless operation.

**Key Positioning:**
- “Turn Any Server into an SEO AI Worker.”
- “One script. No Interface. Just Results.”
- Focus on three clean deployment options only:
  1. **Air-Gapped AI** (The Fortress) — Maximum privacy and isolation
  2. **AWS Lightsail** (The Standard) — Simplified Amazon infrastructure
  3. **DigitalOcean** (The Greenfield) — Developer-friendly and fast

**Do not use** “hybrid”, “on-prem vs cloud”, or legacy deployment language unless a human specifically requests it.

**Logo Concept:** `T>||G`  
- T = Terminal / user input (the script)
- > = One-script deployment flow
- || = Pipe / connection layer (Docker + Ollama)
- G = Glass (clean, deterministic result/container)

## 5. Current Pricing (Reference Only)

Use these prices when writing or editing sales-related copy:

- **Basic**: $99.00 per model
- **Additional Deployments**: $25.00 each
- **Sunrise Package**: $299.00 (includes 20 licenses)
- **Sunrise Additional Deployments**: $10.00 each

**Upgrade Rule:**  
If a Basic ($99) account reaches $299 in total purchases, it automatically converts to a Sunrise account.

**Important:**  
`pricing.html`, `quote.html`, and related pricing/quote pages are currently outdated.  
They will be updated in **Phase 5** only. Do not touch them during Phase 1.

## 6. How to Work in This Repo

1. When given a precise edit task → Do **only** what was asked. Nothing more.
2. When asked for status or analysis across many pages → You may then consult the flat lists and `MODEL_FAMILY_GUIDE.md`.
3. Always prefer minimal, clean changes over large refactors.
4. Never leave visible TODOs, VERIFY notes, or draft language in public-facing pages.
5. When in doubt about scope, ask the human before making assumptions.

## 7. Contact / Escalation

If a task seems ambiguous or conflicts with these rules, stop and ask for clarification rather than guessing.

---
