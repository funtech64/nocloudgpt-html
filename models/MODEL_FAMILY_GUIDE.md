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
* Confirm `/models/` canonical strategy after removing the legacy `/menu/` branch.

Pass 4: Fact Verification

* Verify licenses.
* Verify model availability.
* Verify model names and variants.
* Verify hardware/tier recommendations.
* Verify benchmark or performance claims.
⸻

June 2026 Public Draft Artifact Cleanup Audit

Scope of this pass: `/models/**/*.html` and this guide only. This pass cleaned public-facing draft markers; it did not verify model facts, licenses, benchmark claims, pricing, partnerships, or current Ollama availability.

Status updates from this pass:

* Draft / noindex pages found or retained: Aquila (`/models/aquila/`), Bagel (`/models/bagel/`), Math (`/models/math/`), Nomic (`/models/nomic/`), Noroma (`/models/noroma/`), OpenClaw (`/models/openclaw/`), Pangu (`/models/pangu/`), Reka (`/models/reka/`), Snowball (`/models/snowball/`), TigerBot (`/models/tigerbot/`). These pages remain too thin, uncertain, or stub-like for public indexing.
* Needs verification: broad family pages where visible verification text was softened into buyer-facing caution copy or standardized internal comments. These pages still need human fact-checking before anyone treats their model facts as verified.
* Needs polish: pages where visible artwork/source instructions were removed or moved to internal comments but fallback artwork classes remain in the page implementation.

Missing model family pages discovered under `/models/` during this pass:

* `/models/airoboros/` — Needs verification.
* `/models/all-minilm/` — Needs verification.
* `/models/alpaca/` — Needs verification.
* `/models/aquila/` — Draft / noindex.
* `/models/arctic/` — Needs verification.
* `/models/arctic-llm/` — Needs verification.
* `/models/aya/` — Needs verification.
* `/models/bagel/` — Draft / noindex.
* `/models/bakllava/` — Needs verification.
* `/models/bespoke-minicheck/` — Needs polish.
* `/models/bge/` — Needs verification.
* `/models/chatglm/` — Needs verification.
* `/models/codegeex4/` — Needs verification.
* `/models/codegemma/` — Needs verification.
* `/models/codellama/` — Needs verification.
* `/models/codestral/` — Needs verification.
* `/models/cogito/` — Needs verification.
* `/models/command-r/` — Needs verification.
* `/models/command-r-plus/` — Needs verification.
* `/models/dbrx/` — Needs verification.
* `/models/deepseek-coder/` — Needs verification.
* `/models/deepseek-r1/` — Needs verification.
* `/models/deepseek-v3/` — Needs verification.
* `/models/devstral/` — Needs verification.
* `/models/dolphin/` — Needs verification.
* `/models/duckdb-nsql/` — Needs verification.
* `/models/embedding-gemma/` — Needs verification.
* `/models/exaone/` — Needs verification.
* `/models/falcon/` — Needs verification.
* `/models/firefunction/` — Needs verification.
* `/models/gemma/` — Needs verification.
* `/models/gemma3/` — Needs verification.
* `/models/gemma4/` — Needs verification.
* `/models/glm/` — Needs verification.
* `/models/glm5/` — Needs verification.
* `/models/gpt-2/` — Needs verification.
* `/models/gpt-oss/` — Needs polish.
* `/models/granite/` — Needs verification.
* `/models/granite-code/` — Needs verification.
* `/models/granite-embedding/` — Needs verification.
* `/models/granite-guardian/` — Needs polish.
* `/models/granite4/` — Needs verification.
* `/models/grok/` — Needs verification.
* `/models/internlm/` — Needs verification.
* `/models/jamba/` — Needs verification.
* `/models/kimi/` — Needs verification.
* `/models/laguna/` — Needs verification.
* `/models/lfm/` — Needs verification.
* `/models/lfm2/` — Needs verification.
* `/models/llama-3.1-405b/` — Needs verification.
* `/models/llama-3.2/` — Needs verification.
* `/models/llama-3.2-vision/` — Needs verification.
* `/models/llama-guard/` — Needs verification.
* `/models/llama-guard-3/` — Needs polish.
* `/models/llama3.3/` — Needs verification.
* `/models/llama4/` — Needs verification.
* `/models/llava/` — Needs verification.
* `/models/magicoder/` — Needs verification.
* `/models/magistral/` — Needs verification.
* `/models/math/` — Draft / noindex.
* `/models/medgemma/` — Needs verification.
* `/models/meditron/` — Needs verification.
* `/models/mimo/` — Needs verification.
* `/models/minicpm-v/` — Needs verification.
* `/models/minimax/` — Needs verification.
* `/models/ministral/` — Needs verification.
* `/models/mistral/` — Needs verification.
* `/models/mistral-family/` — Needs verification.
* `/models/mistral-large/` — Needs verification.
* `/models/mistral-small/` — Needs verification.
* `/models/mixtral/` — Needs verification.
* `/models/moondream/` — Needs verification.
* `/models/mxbai/` — Needs verification.
* `/models/mythomax/` — Needs verification.
* `/models/nemotron/` — Needs verification.
* `/models/nemotron4/` — Needs verification.
* `/models/neural-chat/` — Needs verification.
* `/models/nomic/` — Draft / noindex.
* `/models/nomic-embed/` — Needs verification.
* `/models/noroma/` — Draft / noindex.
* `/models/nous/` — Needs verification.
* `/models/nous-hermes/` — Needs verification.
* `/models/nuextract/` — Needs verification.
* `/models/obsidian/` — Needs verification.
* `/models/olmo/` — Needs verification.
* `/models/openchat/` — Needs verification.
* `/models/opencoder/` — Needs verification.
* `/models/openhermes/` — Needs verification.
* `/models/orca-mini/` — Needs verification.
* `/models/paligemma/` — Needs verification.
* `/models/pangu/` — Draft / noindex.
* `/models/paraphrase-multilingual/` — Needs verification.
* `/models/phi/` — Needs verification.
* `/models/phi4/` — Needs verification.
* `/models/phind-codellama/` — Needs verification.
* `/models/pixtral/` — Needs verification.
* `/models/qwen-embedding/` — Needs verification.
* `/models/qwen-vl/` — Needs verification.
* `/models/qwen2.5-coder/` — Needs verification.
* `/models/qwen3.5/` — Needs verification.
* `/models/reader-lm/` — Needs verification.
* `/models/recurrentgemma/` — Needs verification.
* `/models/reflection/` — Needs verification.
* `/models/reka/` — Draft / noindex.
* `/models/sailor2/` — Needs verification.
* `/models/samantha/` — Needs verification.
* `/models/seallm/` — Needs verification.
* `/models/shieldgemma/` — Needs verification.
* `/models/smollm/` — Needs verification.
* `/models/snowball/` — Draft / noindex.
* `/models/snowflake-arctic-embed/` — Needs verification.
* `/models/solar/` — Needs verification.
* `/models/sqlcoder/` — Needs verification.
* `/models/stablelm/` — Needs verification.
* `/models/starcoder/` — Needs verification.
* `/models/starcoder2/` — Needs verification.
* `/models/starling/` — Needs verification.
* `/models/tigerbot/` — Draft / noindex.
* `/models/translategemma/` — Needs verification.
* `/models/tulu/` — Needs verification.
* `/models/vicuna/` — Needs verification.
* `/models/whisper/` — Needs verification.
* `/models/wizardcoder/` — Needs verification.
* `/models/wizardlm/` — Needs verification.
* `/models/wizardlm2/` — Needs verification.
* `/models/yi/` — Needs verification.
* `/models/zamba/` — Needs verification.
* `/models/zamba2/` — Needs verification.
* `/models/zephyr/` — Needs verification.

Notes from cleanup:

* Visible verification labels were removed from rendered copy and replaced with safer NoCloudGPT review language across affected HTML pages.
* Useful asset and follow-up comments were standardized as internal verification comments where they still help maintainers.
* Visible source/artwork instructions and visible asset-path text were removed where they appeared in page content.
* Stub language was changed from public draft phrasing to deployment-review phrasing, and thin/uncertain stub pages were kept or marked `noindex`.
* Risky exact deployment and availability statements were softened where they were attached to visible verification labels. This pass did not independently verify the underlying facts.

Remaining human decisions:

* Decide whether uncertain families such as OpenClaw, Noroma, Snowball, TigerBot, Reka, Pangu, Nomic, Math, Bagel, and Aquila should remain in the catalog after factual review.
* Decide whether fallback artwork class names containing the word `placeholder` should be renamed in a separate style-safe cleanup. They are implementation names, not public editorial copy, but the verification grep still reports them.
* Verify current model availability, license terms, tags, hardware fit, and commercial suitability before marking any broad family page `Publish-ready`.
