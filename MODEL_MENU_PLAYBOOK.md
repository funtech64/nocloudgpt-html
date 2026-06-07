# MODEL_MENU_PLAYBOOK.md — NoCloudGPT /menu/ Catalog Standard

## Critical Path Rule

The model catalog lives under **`/menu/`**, **not** `/models/`.

Use paths like:
- `/menu/llama/`
- `/menu/deepseek/`
- `/menu/qwen/`
- `/menu/gemma/`

Never create or reference `/models/` paths.

---

## Core Rule

- **Family pages** persuade and route buyers.
- **Size/detail pages** specify technical details and validate deployment fit.

Every `/menu/` family page should clearly answer:

1. What is this model family good at?
2. Who developed it?
3. Who should choose it?
4. What size range makes sense for different workloads?
5. What NoCloudGPT deployment tier is realistic?

---

## Standard Page Sections (Recommended Order)

Strong `/menu/` family pages should generally include:

1. **Hero** — Buyer-focused headline + primary CTA
2. **What this model family is** — Plain-English explanation
3. **Who developed it** — Company / research group background
4. **Why teams choose it** — 3–5 sales cards linking capability to buyer outcome
5. **Best-fit workloads** — Specific, concrete examples
6. **Which size should you choose?** — Tiered size guidance with NoCloudGPT mapping
7. **Hardware and deployment reality** — Practical hardware guidance using Compute Tiers
8. **When to choose another model** — Honest routing to better alternatives
9. **Deploy this model with NoCloudGPT** — Strong CTA to quote + deployment options
10. **Related pages** — Links to related families or important size pages
11. **Artwork checklist** — Hero, sidebar, and developer artwork placeholders

---

## NoCloudGPT Two-Tier Language (Use Consistently)

Always distinguish between:

- **Platform Tier** (Pilot, Sunrise, Hybrid, Professional, Enterprise)
- **Compute Tier** (Nano AI, Starter AI, Standard AI, Professional AI, Heavy AI, Enterprise AI)

Never expose raw AWS pricing, vCPU counts, or transfer quotas on family pages.

---

## Batch Priorities

### Batch 1 — Flagship Pages (Highest Impact)
These should be brought to full standard first:

- `/menu/llama/`
- `/menu/deepseek/`
- `/menu/qwen/`
- `/menu/gemma/`
- `/menu/mistral/`
- `/menu/phi/`
- `/menu/granite/`
- `/menu/mixtral/`
- `/menu/command-r/`
- `/menu/llava/`
- `/menu/nomic/`
- `/menu/codellama/`
- `/menu/qwen2.5-coder/`
- `/menu/deepseek-coder/`

### Batch 2 — High-Value Specialty Pages
Medium priority:

- `/menu/gemma4/`
- `/menu/gemma2/`
- `/menu/phi4/`
- `/menu/mistral-large/`
- `/menu/mistral-small/`
- `/menu/ministral/`
- `/menu/pixtral/`
- `/menu/qwen-vl/`
- `/menu/qwen3.5/`
- `/menu/starcoder2/`
- `/menu/devstral/`
- `/menu/llama4/`
- `/menu/llama3.3/`

### Batch 3 — Developer, Reasoning & Enterprise
Medium rewrite priority:

- `/menu/granite4/`
- `/menu/nemotron/`
- `/menu/nemotron4/`
- `/menu/glm/`
- `/menu/glm5/`
- `/menu/kimi/`
- `/menu/minimax/`
- `/menu/cogito/`
- `/menu/jamba/`
- `/menu/tulu/`
- `/menu/dolphin/`

### Batch 4 — Lightweight, Legacy & Niche
Light-to-medium rewrite (many are currently thin or stub pages):

- `/menu/tiny/`
- `/menu/smollm/`
- `/menu/tinyllama/`
- `/menu/zephyr/`
- `/menu/yi/`
- `/menu/falcon/`
- `/menu/olmo/`
- `/menu/aya/`
- `/menu/solar/`
- `/menu/wizardlm/`
- `/menu/vicuna/`
- `/menu/openhermes/`
- `/menu/mythomax/`
- `/menu/llama-guard/`
- `/menu/nous/`
- `/menu/baichuan/`
- `/menu/internlm/`
- `/menu/exaone/`
- `/menu/zamba/`
- `/menu/lfm2/`
- `/menu/reka/`
- `/menu/paligemma/`
- `/menu/recurrentgemma/`
- `/menu/seallm/`
- `/menu/openclaw/`
- `/menu/snowball/`
- `/menu/noroma/`
- `/menu/bagel/`
- `/menu/aquila/`
- `/menu/pangu/`
- `/menu/tigerbot/`
- `/menu/airoboros/`
- `/menu/samantha/`

---

## Cursor / Agent Workflow Instruction

Before editing any page:

1. Read `AGENT.md`, `COPYWRITING.md`, and this playbook.
2. Inspect the actual folder under `/menu/`.
3. Do **not** assume a page exists just because it is listed here.

For every page you edit:

- Preserve existing structure when possible (least invasive useful change).
- Improve weak or missing sections.
- Add buyer guidance and deployment caveats.
- Preserve working CTAs and navigation.
- Mark uncertain facts with `VERIFY:` comments.
- **Do not invent benchmark numbers or partnerships.**
- Use the voice defined in `COPYWRITING.md`.

---

## Definition of Done for a Family Page

A `/menu/` family page is considered complete when it:

- Clearly answers the five core questions above
- Uses the standard section structure
- Has correct `/menu/` paths and canonicals
- Contains honest routing in the “When to choose another model” section
- Has a strong NoCloudGPT deployment CTA
- Uses the two-tier pricing language correctly
- Has artwork placeholders where images are missing
- Contains no invented benchmarks or claims
