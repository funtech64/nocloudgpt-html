NoCloudGPT Model Family Guide

This file is the working editorial guide for the NoCloudGPT model catalog.

Its purpose is to help humans, Cursor, and Codex keep the /models/ pages consistent, clean, and buyer-friendly.

This is not a public sales page. It is an internal guide for organizing and improving model family pages.

Catalog Rules

Each model family page should answer:

1. What is this model family good at?
2. Who should choose it?
3. What kind of private AI deployment does it fit?
4. What are the licensing or availability cautions?
5. What NoCloudGPT action should the visitor take next?

Page Status Labels

Use one of these status labels for each model family:

* Publish-ready — page is clean, polished, and suitable for public visitors.
* Needs polish — page is useful but needs cleanup, CTA work, consistency, or minor copy improvements.
* Needs verification — page includes claims about license, hardware fit, benchmarks, model availability, or developer details that need confirmation.
* Draft / noindex — page should not be treated as a finished public landing page.
* Legacy / duplicate — page appears to be old, duplicated, or superseded by another page.

Editorial Rules

* Do not leave visible VERIFY, TODO, or internal notes in rendered page copy.
* Useful internal notes may remain as HTML comments only.
* Do not invent benchmarks, speed claims, license terms, pricing claims, partnerships, or hardware requirements.
* Use buyer-friendly language instead of raw infrastructure language when possible.
* Prefer NoCloudGPT deployment tier language over raw server specs.
* Keep model pages honest: small models are fast but limited; larger models are more capable but need stronger hardware.
* Every page should have a clear CTA.

Recommended CTA Phrases

* Build your deployment quote
* Request a NoCloudGPT quote
* Start a private AI pilot
* Plan an on-premise installation
* Compare model families
* Choose the right model for your workload

⸻

Model Family List

Llama

* Path: /models/llama/
* Status: Needs polish
* Best fit: General private AI assistant, business assistant, internal knowledge assistant, balanced starting point.
* Audience: Small businesses, teams, private AI buyers, general-purpose users.
* Deployment fit: Strong default family for NoCloudGPT pilots and business deployments.
* Cautions:
    * Verify current Meta license terms.
    * Avoid unsupported ROI/payback claims.
    * Avoid overpromising performance.
* Recommended action:
    * Keep as one of the flagship family pages.

DeepSeek

* Path: /models/deepseek/
* Status: Needs verification
* Best fit: Reasoning, coding, technical analysis, structured problem-solving.
* Audience: Developers, technical teams, research-heavy users, advanced private AI users.
* Deployment fit: Strong candidate for technical private AI deployments.
* Cautions:
    * Verify current license terms and model availability.
    * Avoid unsupported benchmark claims.
    * Avoid promising hidden chain-of-thought access. Prefer “step-by-step reasoning style” or “visible reasoning output” where appropriate.
* Recommended action:
    * Keep, polish, and fact-check.

Qwen

* Path: /models/qwen/
* Status: Needs polish
* Best fit: Scalable private AI family, coding, multilingual work, general assistant use.
* Audience: Teams that may start small and grow into larger deployments.
* Deployment fit: Good model ladder from small pilots to larger private deployments.
* Cautions:
    * Verify model variant names, license terms, and links to coder/vision pages.
    * Fix any broken links to related Qwen family pages.
* Recommended action:
    * Keep as a major catalog page.

Gemma 2

* Path: /models/gemma2/
* Status: Needs polish
* Best fit: Efficient private AI, smaller deployments, cost-conscious pilots.
* Audience: Small businesses, schools, ministries, individuals, lightweight private AI users.
* Deployment fit: Good starter/pilot candidate.
* Cautions:
    * Remove visible verification notes.
    * Verify Ollama tags and current model availability.
    * Avoid raw server specs where tier language would be clearer.
* Recommended action:
    * Use as a model for clean, practical family-page structure after cleanup.

Baichuan

* Path: /models/baichuan/
* Status: Needs verification
* Best fit: Chinese/English bilingual work, Chinese-language document handling, multilingual private AI.
* Audience: Teams with Chinese-language or bilingual needs.
* Deployment fit: Niche but useful catalog page.
* Cautions:
    * Verify license terms.
    * Verify current model availability.
    * Resolve any inconsistent deployment tier recommendations.
* Recommended action:
    * Keep if verified; otherwise mark as noindex until cleaned.

TinyLlama

* Path: /models/tinyllama/
* Status: Needs polish
* Best fit: Tiny local experiments, education, simple demos, constrained hardware.
* Audience: Developers, learners, hobbyists, ultra-light deployment users.
* Deployment fit: Educational or experimental, not a flagship business assistant.
* Cautions:
    * Page style may not match newer family pages.
    * Avoid making it sound more capable than it is.
    * Remove visible artwork/source/TODO notes.
* Recommended action:
    * Either modernize the page or move it into a lightweight/experimental category.

OpenClaw

* Path: /models/openclaw/
* Status: Draft / noindex
* Best fit: Unknown until verified.
* Audience: Unknown until verified.
* Deployment fit: Unknown until verified.
* Cautions:
    * Do not present as a finished deployable model family.
    * Verify whether this model family should exist in the catalog.
    * Remove visible “Page under development” language.
* Recommended action:
    * Mark noindex or remove from public catalog listings until verified.

⸻

Non-Family Supporting Pages

Model Catalog Index

* Path: /models/
* Status: Needs polish
* Purpose: Main navigation and model family discovery page.
* Cautions:
    * Verify model count claims.
    * Verify “latest” language.
    * Avoid unsupported benchmark/performance comparisons.
* Recommended action:
    * Keep and clean after individual family page statuses are known.

Quote Builder

* Path: /models/quote.html
* Status: Needs expansion
* Purpose: Lead capture / deployment quote entry point.
* Cautions:
    * Currently thin.
    * Should not feel like a placeholder.
* Recommended action:
    * Improve after model family pages are cleaned.

Deployment Index

* Path: /models/deploy/
* Status: Needs expansion
* Purpose: Explain deployment options.
* Cautions:
    * Keep language aligned with model family CTAs.
* Recommended action:
    * Improve after catalog cleanup.

Lightsail Deployment Guide

* Path: /models/deploy/lightsail-guide.html
* Status: Needs polish
* Purpose: Practical starter deployment guide.
* Cautions:
    * Avoid raw specs/pricing where NoCloudGPT tier language is better.
* Recommended action:
    * Keep; likely one of the stronger support pages.

On-Premise Deployment Guide

* Path: /models/deploy/on-premise.html
* Status: Needs expansion
* Purpose: Explain on-premise/private hardware deployment.
* Cautions:
    * Currently thin compared to stronger pages.
* Recommended action:
    * Expand later.

Private Cloud Deployment Guide

* Path: /models/deploy/private-cloud.html
* Status: Needs polish
* Purpose: Explain private cloud deployment.
* Cautions:
    * Keep buyer-friendly; avoid making it too homelab-heavy.
* Recommended action:
    * Keep and polish.

⸻

Cleanup Priority

Pass 1: Public Polish

* Remove visible VERIFY, TODO, and draft language.
* Convert useful notes to clean internal HTML comments.
* Remove visible placeholder/source/artwork notes.
* Soften unsupported claims.
* Fix obvious broken links and weak CTAs.

Pass 2: Status Classification

* Mark each page as publish-ready, needs polish, needs verification, draft/noindex, or legacy/duplicate.
* Remove draft pages from catalog grids if needed.
* Add noindex to pages that should not be indexed yet.

Pass 3: Consistency

* Normalize family page structure.
* Normalize CTAs.
* Normalize tier language.
* Resolve /models/ versus /menu/ canonical strategy.

Pass 4: Fact Verification

* Verify licenses.
* Verify model availability.
* Verify model names and variants.
* Verify hardware/tier recommendations.
* Verify benchmark or performance claims.