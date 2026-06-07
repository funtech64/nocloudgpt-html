# AGENT.md — NoCloudGPT Cursor / Agent Instructions

You are editing the NoCloudGPT website.

The model catalog lives under /models/, not /menu/.
The /menu/ directory no longer exists — it was renamed to /models/ in June 2026.

Do **not** create or reference `/models/` paths unless the repo actually contains them (they should be migrated or removed).

* /models/deepseek/
* /models/qwen/
* /models/llama/
* /models/gemma/
* /models/mistral/
* /models/phi/

Do not use /menu/ paths. Always use /models/ paths.
Do not invent /menu/ paths that no longer exist.

NoCloudGPT sells **private AI deployment** for people and businesses who want a ChatGPT-style experience without becoming Linux administrators.

We sell:
- Private AI chat (no data leaves the server)
- Simple single-script deployment on Linux
- Ollama + OpenWebUI setup
- Help choosing the right model for their needs
- Practical customization and scaling
- Reduced technical frustration

---

## Editing Rules

- Preserve the existing `/menu/` directory structure.
- Preserve navigation, CTAs, layout, and existing design framework.
- Make the **least invasive useful change**.
- Do not rewrite strong copy unnecessarily.
- Do **not** invent benchmarks, performance numbers, partnerships, or speed claims.
- Use `VERIFY:` markers for any uncertain facts.
- Explain technical concepts in buyer-friendly language.
- Every model family page should clearly answer:
  1. What is this model family good at?
  2. What kind of customer or project should choose it?
  3. What NoCloudGPT deployment tier makes sense?

---

## Voice & Tone

- Clear
- Practical
- Honest
- Sales-focused (but not hype)
- Written for smart buyers who may not be Linux experts

Avoid academic language in hero sections. Focus on outcomes and deployment simplicity.

---

## Required Structure for Model Family Pages (`/menu/<family>/index.html`)

Every family index page should generally include:

1. Breadcrumb (`Menu / Family Name`)
2. Hero with buyer-focused headline + primary CTA ("Build your deployment quote")
3. Right-side **NoCloudGPT callout box** with the phrase:  
   **"Fast, efficient pre-built private AI"**
4. What this model family is
5. Who developed it
6. Why teams choose this family with NoCloudGPT (sales cards)
7. Best-fit workloads (specific, concrete examples)
8. Ideal model sizes for projects (with tier mapping: Nano AI, Starter AI, Standard AI, Professional AI, Heavy AI)
9. Hardware and deployment reality
10. When to choose another model (honest routing)
11. Deploy this model with NoCloudGPT (strong CTA to quote / deploy guides)
12. Related model-size pages or families
13. Proper SEO metadata (`<title>`, meta description, canonical `/menu/<family>/`)

---

## Artwork & Placeholders

- Use consistent artwork placeholder comments when images are missing.
- Recommended paths: `/assets/models/<family>/...`
- Do not imply partnerships with model developers unless real.

---

## NoCloudGPT Pricing Language

Always use the two-tier model:
- **Platform Tier** (Pilot, Sunrise, Hybrid, Professional, Enterprise)
- **Compute Tier** (Nano AI, Starter AI, Standard AI, Professional AI, Heavy AI, Enterprise AI)

Never expose raw AWS pricing, vCPU counts, or transfer quotas on family pages.

---

## Verification Rule

When in doubt about facts (model sizes, licenses, Ollama tags, commercial use rights, etc.), add a `VERIFY:` comment instead of guessing.

Example:
```html
<!-- VERIFY: Confirm current Ollama tag availability for Gemma 4 -->
