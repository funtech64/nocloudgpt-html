# Terminal Glass Cloud Model Inventory

Date: 2026-06-18
Project: `funtech64/nocloudgpt-html`
Working directory focus: `/models/`

## Purpose

This planning note separates two different offerings that should not be mixed together in the sales copy:

1. **NoCloudGPT local / private-server instances** — models run on the customer's Linux server, on-premise machine, or private cloud instance.
2. **Terminal Glass cloud instances** — the user still gets an Ollama-compatible workflow, but the actual inference is offloaded to Ollama Cloud. This gives very fast response speed and very low local hardware requirements.

Terminal Glass should be presented as the speed-and-simplicity lane: the customer gets the familiar private AI dashboard and workflow, while the heavy model computation happens through Ollama's cloud backend. This is not the same promise as fully local air-gapped AI, so the branding should be distinct.

## Official Ollama Cloud behavior to reflect in copy

Ollama documentation says cloud models can run without a powerful GPU because they are offloaded to Ollama's cloud service while preserving the same local tools and model workflow. Cloud models require signing in with an Ollama account through `ollama signin`. The docs show local CLI usage with a cloud suffix such as:

```bash
ollama run gpt-oss:120b-cloud
ollama pull gpt-oss:120b-cloud
```

Ollama also documents direct API access through `https://ollama.com` using an `OLLAMA_API_KEY`, where the model name may be used without the `-cloud` suffix in direct remote API mode.

Important positioning note: Ollama documentation also says cloud models can be retired or deprecated. Do not hard-code this lineup as permanent. The website should treat the list below as a maintained product catalog.

Sources checked:

- https://docs.ollama.com/cloud
- https://ollama.com/library

## Current `/models/` inventory observed

The current `/models/` directory already contains a broad catalog, including local model families, embeddings, coding models, safety models, deployment pages, pricing pages, and comparison pages.

Observed folders / files from the repository view include:

`airoboros`, `all-minilm`, `alpaca`, `aya`, `bakllava`, `bespoke-minicheck`, `bge`, `chatglm`, `chatgpt-alternatives`, `codegeex4`, `codegemma`, `codellama`, `codestral`, `cogito`, `command-r`, `compare`, `deepseek-coder`, `deepseek`, `deploy`, `duckdb-nsql`, `embedding-gemma`, `exaone`, `falcon`, `firefunction`, `gemma`, `glm`, `glm5`, `gpt-2`, `gpt-oss`, `granite-code`, `granite-embedding`, `granite-guardian`, `granite`, `granite4`, `internlm`, `jamba`, `kimi`, `laguna`, `lfm`, `llama-guard-3`, `llama`, `llava`, `magicoder`, `magistral`, `medgemma`, `meditron`, `minicpm-v`, `minimax`, `mistral-family`, `mistral`, `mixtral`, `moondream`, `mxbai`, `mythomax`, `nemotron`, `nemotron4`, `neural-chat`, `nomic-embed`, `nous-hermes`, `nuextract`, `obsidian`, `olmo`, `openchat`, `opencoder`, `openhermes`, `paligemma`, `paraphrase-multilingual`, `phi`, `phind-codellama`, `pixtral`, `qwen-embedding`, `qwen`, `qwen2.5-coder`, `reader-lm`, `recurrentgemma`, `reflection`, `samantha`, `shieldgemma`, `smollm`, `snowflake-arctic-embed`, `solar`, `sqlcoder`, `stablelm`, `starcoder`, `tinyllama`, `translategemma`, `tulu`, `whisper`, `wizardcoder`, `wizardlm`, `yi`, `zamba2`, `zephyr`, plus `index.html`, `note.md`, `note2.md`, `pricing.html`, and `quote.html`.

## Inventory comparison: local catalog vs Ollama offered families

The `/models/` directory is strong on classic local Ollama families and useful specialty groupings. It already covers many major customer-searchable names: Llama, DeepSeek, Qwen, Gemma, Mistral, Phi, Granite, Nemotron, Command-R, OLMo, Yi, Falcon, CodeGemma, CodeLlama, StarCoder, LLaVA, embeddings, safety/guard models, medical models, SQL models, and small models.

The gap is that the folder set does not clearly separate **Ollama Cloud** as its own product lane. Several cloud-capable model families are present as local family folders, but cloud use is not obvious from the directory names. For example, `gpt-oss`, `gemma`, `gemma4`, `qwen`, `glm5`, `kimi`, `minimax`, `nemotron`, `devstral`, and `mistral` should have a cloud branding treatment if sold through Terminal Glass.

Recommended structural addition:

```text
/models/terminal-glass/
  index.html
  cloud-models.md
  gpt-oss/
  gemma4/
  qwen3.5/
  qwen3-coder/
  deepseek-cloud/
  glm-cloud/
  kimi-cloud/
  minimax-cloud/
  nemotron-cloud/
  mistral-cloud/
  devstral-cloud/
```

This keeps `/models/gpt-oss/` as the general model-family SEO page, while `/models/terminal-glass/gpt-oss/` becomes the cloud instance sales page.

## Terminal Glass naming convention

Use this language consistently:

- **Terminal Glass Cloud Instance** — cloud-offloaded Ollama compute, very low local hardware burden.
- **NoCloudGPT Private Instance** — local/private server compute, good for privacy and ownership.
- **NoCloudGPT On-Prem Instance** — business/home office Linux server.
- **NoCloudGPT Private Cloud Instance** — AWS Lightsail, VPS, or customer-controlled Linux cloud.

Avoid calling Terminal Glass fully private or air-gapped. It is better to sell it as:

> Fast, efficient, pre-built private AI workflow with Ollama Cloud acceleration.

## Hardware positioning for Terminal Glass

Because inference is offloaded, Terminal Glass should not be tied to the heavy local RAM/VRAM ladder.

Recommended sales language:

| Terminal Glass level | Local requirement | Customer-friendly explanation |
|---|---:|---|
| TG Cloud Starter | 2 GB RAM Linux host | Runs the dashboard, Ollama client, and routing layer. Good for pilots. |
| TG Cloud Standard | 4 GB RAM Linux host | Better for OpenWebUI, small RAG, multiple users, and smoother admin work. |
| TG Cloud Business | 8 GB RAM Linux host | Better for teams, plugins, automations, and document workflows. |
| TG Cloud Pro | 16 GB+ RAM Linux host | For heavier dashboards, local fallback models, hybrid cloud/local use. |

This lets us keep the normal NoCloudGPT compute ladder for local inference while creating a clean Terminal Glass cloud ladder for cloud-backed inference.

## Cloud-tagged Ollama models to index under Terminal Glass

These are the cloud-tagged model families visible in the Ollama model library and/or cloud docs during this inventory pass. Treat these as priority sales pages for Terminal Glass.

| Priority | Terminal Glass page slug | Ollama family / model | Suggested positioning | Existing `/models/` coverage | Action |
|---:|---|---|---|---|---|
| 1 | `/models/terminal-glass/gpt-oss/` | `gpt-oss` | OpenAI open-weight reasoning and agentic work; flagship cloud demo. | `gpt-oss` exists | Add Terminal Glass cloud page. |
| 2 | `/models/terminal-glass/gemma4/` | `gemma4` | Google multimodal, tools, thinking, audio, cloud; strong general-purpose cloud page. | `gemma` exists; check `gemma4` | Add or normalize cloud page. |
| 3 | `/models/terminal-glass/qwen3.5/` | `qwen3.5` | Alibaba multimodal, tools, thinking, cloud; strong all-rounder. | `qwen` exists | Add Qwen cloud page. |
| 4 | `/models/terminal-glass/qwen3-coder/` | `qwen3-coder` | Agentic coding and long-context development. | `qwen2.5-coder` exists | Add current Qwen3 coder cloud page. |
| 5 | `/models/terminal-glass/qwen3-coder-next/` | `qwen3-coder-next` | Coding-focused local development and agentic coding. | missing explicit folder | Add page if still active. |
| 6 | `/models/terminal-glass/qwen3.6/` | `qwen3.6` | Newer Qwen agentic coding / thinking model family. | missing explicit folder | Add page. |
| 7 | `/models/terminal-glass/deepseek-v3.2/` | `deepseek-v3.2` | Efficient reasoning + agent performance. | `deepseek` exists | Add cloud-specific DeepSeek page. |
| 8 | `/models/terminal-glass/deepseek-v3.1/` | `deepseek-v3.1` | Hybrid thinking/non-thinking DeepSeek cloud lane. | `deepseek` exists | Add only if not retired. |
| 9 | `/models/terminal-glass/deepseek-v4-pro/` | `deepseek-v4-pro` | Frontier MoE, long context, multiple reasoning modes. | missing explicit folder | Add page. |
| 10 | `/models/terminal-glass/deepseek-v4-flash/` | `deepseek-v4-flash` | Efficient long-context reasoning cloud model; good replacement candidate for retired huge models. | missing explicit folder | Add page. |
| 11 | `/models/terminal-glass/glm-5.2/` | `glm-5.2` | Z.ai flagship for long-horizon tasks. | `glm`, `glm5` exist | Add cloud version page. |
| 12 | `/models/terminal-glass/glm-5.1/` | `glm-5.1` | Agentic engineering and coding. | `glm5` exists | Add Terminal Glass page. |
| 13 | `/models/terminal-glass/glm-5/` | `glm-5` | Large reasoning/agentic model. | `glm5` exists | Add or fold into GLM cloud hub. |
| 14 | `/models/terminal-glass/glm-4.7/` | `glm-4.7` | Coding capability. | `glm` exists | Add if active. |
| 15 | `/models/terminal-glass/minimax-m3/` | `minimax-m3` | Coding and agentic frontier with multimodality. | `minimax` exists | Add current MiniMax cloud page. |
| 16 | `/models/terminal-glass/minimax-m2.7/` | `minimax-m2.7` | Coding, agentic workflows, productivity. | `minimax` exists | Add only if active. |
| 17 | `/models/terminal-glass/minimax-m2.5/` | `minimax-m2.5` | Productivity and coding. | `minimax` exists | Add only if active. |
| 18 | `/models/terminal-glass/minimax-m2.1/` | `minimax-m2.1` | Multilingual code engineering. | `minimax` exists | Add only if active. |
| 19 | `/models/terminal-glass/kimi-k2.7-code/` | `kimi-k2.7-code` | Moonshot coding-focused agentic cloud model. | `kimi` exists | Add current page. |
| 20 | `/models/terminal-glass/kimi-k2.6/` | `kimi-k2.6` | Long-horizon coding, design, autonomous execution, swarm-style workflows. | `kimi` exists | Add page. |
| 21 | `/models/terminal-glass/kimi-k2.5/` | `kimi-k2.5` | Native multimodal agentic model. | `kimi` exists | Add only if active. |
| 22 | `/models/terminal-glass/nemotron-3-ultra/` | `nemotron-3-ultra` | NVIDIA long-running agent workflows and high-throughput reasoning. | `nemotron`, `nemotron4` exist | Add page. |
| 23 | `/models/terminal-glass/nemotron-3-super/` | `nemotron-3-super` | 120B MoE, 12B active; efficient complex multi-agent work. | `nemotron` exists | Add page. |
| 24 | `/models/terminal-glass/nemotron-3-nano/` | `nemotron-3-nano` | Efficient open agentic model; cloud available despite smaller sizes. | `nemotron` exists | Add page. |
| 25 | `/models/terminal-glass/nemotron-cascade-2/` | `nemotron-cascade-2` | 30B MoE with 3B active; efficient reasoning. | missing explicit folder | Add page. |
| 26 | `/models/terminal-glass/devstral-2/` | `devstral-2` | 123B coding agent model. | missing explicit folder; `mistral` exists | Add page. |
| 27 | `/models/terminal-glass/devstral-small-2/` | `devstral-small-2` | 24B codebase exploration and multi-file editing; cloud available. | missing explicit folder | Add page. |
| 28 | `/models/terminal-glass/ministral-3/` | `ministral-3` | Edge-oriented Mistral cloud/vision/tool model. | `mistral`, `mistral-family` exist | Add or link to Mistral cloud hub. |
| 29 | `/models/terminal-glass/mistral-large-3/` | `mistral-large-3` | Production-grade multimodal MoE cloud model. | `mistral` exists | Add cloud flagship page. |
| 30 | `/models/terminal-glass/gemini-3-flash-preview/` | `gemini-3-flash-preview` | Speed-focused frontier cloud model. | missing explicit folder | Add with careful branding/licensing review. |
| 31 | `/models/terminal-glass/rnj-1/` | `rnj-1` | 8B code/STEM model with cloud support. | missing explicit folder | Add page. |

## Deprecated or risky cloud items

Do not prioritize these as new customer-facing pages unless they are retained only as redirect/comparison content:

| Model | Recommended alternative from Ollama docs |
|---|---|
| `kimi-k2-thinking` | `kimi-k2.6` |
| `kimi-k2:1t` | `kimi-k2.6` |
| `minimax-m2` | `minimax-m3` |
| `glm-4.6` | `glm-5.1` |
| `qwen3-next:80b` | `qwen3.5` |
| `qwen3-vl:235b` | `qwen3.5` |
| `qwen3-vl:235b-instruct` | `qwen3.5` |
| `cogito-2.1:671b` | `deepseek-v4-flash` |

## Recommended build order

1. `/models/terminal-glass/index.html` — explain the Terminal Glass concept and how it differs from NoCloudGPT local/on-prem.
2. `/models/terminal-glass/gpt-oss/` — easiest demo because Ollama docs show `gpt-oss:120b-cloud` directly.
3. `/models/terminal-glass/qwen3.5/` — strong general cloud page.
4. `/models/terminal-glass/gemma4/` — Google family + multimodal story.
5. `/models/terminal-glass/deepseek-v4-flash/` — efficient reasoning story.
6. `/models/terminal-glass/kimi-k2.6/` and `/models/terminal-glass/kimi-k2.7-code/` — coding/agentic story.
7. `/models/terminal-glass/minimax-m3/` — coding & agentic frontier story.
8. `/models/terminal-glass/glm-5.2/` — long-horizon tasks.
9. `/models/terminal-glass/nemotron-3-ultra/` — NVIDIA multi-agent / high-throughput story.
10. `/models/terminal-glass/mistral-large-3/` and `/models/terminal-glass/devstral-2/` — Mistral enterprise/coding lane.

## Recommended CTA language

Use this CTA box across Terminal Glass pages:

> **Fast, efficient pre-built private AI workflow**  
> Run a familiar Ollama/OpenWebUI experience without buying a workstation GPU. Terminal Glass connects your small private server to Ollama Cloud-backed models for speed, simplicity, and a clean upgrade path.
>
> Button: **Deploy a Terminal Glass Cloud Instance**

## Short sales distinction

Use this plain explanation somewhere near the top of the Terminal Glass hub:

> NoCloudGPT is for customers who want their AI running on their own server. Terminal Glass is for customers who want the same simple private AI workflow, but with the heavy model computation handled by Ollama Cloud. It is the fast lane for small teams that want capability first and hardware complexity later.

## Next technical task

Create a reusable data file so the Terminal Glass list can be updated without rewriting every page:

```text
/models/data/terminal-glass-cloud-models.json
```

Suggested schema:

```json
[
  {
    "slug": "gpt-oss",
    "displayName": "GPT-OSS Cloud",
    "ollamaFamily": "gpt-oss",
    "exampleRun": "ollama run gpt-oss:120b-cloud",
    "category": "reasoning-agentic",
    "priority": 1,
    "existingLocalFolder": "/models/gpt-oss/",
    "terminalGlassFolder": "/models/terminal-glass/gpt-oss/",
    "status": "priority"
  }
]
```

This gives the site one maintainable list that can feed the Terminal Glass index, quote page, and sidebar CTA blocks.
