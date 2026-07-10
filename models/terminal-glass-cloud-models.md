# Terminal Glass Jet Agent Model Lane Inventory

Date: 2026-07-10  
Project: `funtech64/nocloudgpt-html`  
Working directory focus: `/models/`

## Decision

Terminal Glass cloud-backed model content should be framed as **Jet Agent model lanes**.

A Jet Agent is not a separate license type. A Jet Agent is a curated cloud-model capability made available through the customer's terminal.glass package and deployment.

Use this product rule consistently:

```text
Glass Licenses are interchangeable.
Deployment Keys are not.
Jet Agents are not separate licenses.
```

The sellable unit is the **Glass License**. Jet Agents are model lanes and workflows available inside the package.

## Folder strategy

Cloud-backed model lanes should continue to live as their own clean family folders directly inside `/models/`.

Do not make `/models/terminal-glass/<model>/` the primary site structure.  
Do not hide cloud variants inside local NoCloudGPT model family folders.

Use this pattern instead:

```text
/models/gpt-oss-cloud/index.html
/models/qwen3.5-cloud/index.html
/models/gemma4-cloud/index.html
/models/gemma4-cloud/index.html
/models/deepseek-v4-flash-cloud/index.html
/models/kimi-k2.6-cloud/index.html
```

Public-facing terminology:

```text
/models/gpt-oss-cloud/
= GPT-OSS Jet Agent model lane

/models/qwen3.5-cloud/
= Qwen Jet Agent model lane

/models/deepseek-v4-flash-cloud/
= DeepSeek Jet Agent model lane

/models/kimi-k2.6-cloud/
= Kimi Jet Agent model lane

/models/nemotron-3-ultra-cloud/
= Nemotron Jet Agent model lane
```

## Product distinction

| Product lane | Where the model work happens | Sales promise | Folder style |
|---|---|---|---|
| NoCloudGPT Private Instance | Customer-controlled local server, on-prem box, or private cloud server | Private AI that runs on infrastructure the customer controls | `/models/<family>/` |
| YourCloudGPT | Customer-owned cloud deployment | terminal.glass in the customer's cloud account | deployment pages / sales pages |
| Jet Agent model lane | Cloud-backed model computation, surfaced through terminal.glass workflows | Big-model answers, speed, coding, research, and model variety without buying GPU hardware | `/models/<family-or-model>-cloud/` |
| Glass Agent | OpenClaw-based action worker in an approved environment | Approved local action and workflow execution | agent pages / future app UI |
| Alchemist Conductor | Premium coordination layer | Routes work across Glass Agents and Jet Agents | future upgrade pages |

## Sales positioning

Do not sell Jet Agents primarily as privacy or bare-metal infrastructure.

The stronger buyer value is:

- better answers from different models,
- avoiding a corporate monolithic AI experience,
- using private computing for the customer's desired agent work,
- leveraging powerful cloud-backed models without buying expensive GPU servers,
- giving the customer a curated menu instead of raw model chaos.

Suggested copy:

> Jet Agents give your business access to powerful cloud-model workflows without forcing you to buy a large GPU server. Use them for speed, coding, research, drafting, and comparing answers across different model families.

## Official Ollama Cloud behavior to reflect in copy

Ollama Cloud models run through the normal Ollama workflow, but the model computation is offloaded to Ollama Cloud. The local machine does not need the same GPU/RAM profile required for local inference.

Ollama's docs show cloud model usage with names such as:

```bash
ollama run gpt-oss:120b-cloud
ollama pull gpt-oss:120b-cloud
```

Cloud models require the user to sign in with an Ollama account using:

```bash
ollama signin
```

Important copywriting rule:

```text
NoCloudGPT = local/private model lane.
Jet Agent = curated cloud model lane.
Glass Agent = OpenClaw action lane.
Alchemist = coordinator.
```

Terminal Glass cloud-model pages should not describe themselves as fully local or air-gapped. They should be described as cloud-accelerated model lanes inside the terminal.glass ecosystem.

Sources checked earlier:

- https://docs.ollama.com/cloud
- https://ollama.com/library

## Current `/models/` inventory observed

The current `/models/` directory already contains a broad catalog, including local model families, embeddings, coding models, safety models, deployment pages, pricing pages, and comparison pages.

Observed folders / files from the repository view include:

`airoboros`, `all-minilm`, `alpaca`, `aya`, `bakllava`, `bespoke-minicheck`, `bge`, `chatglm`, `chatgpt-alternatives`, `codegeex4`, `codegemma`, `codellama`, `codestral`, `cogito`, `command-r`, `compare`, `deepseek-coder`, `deepseek`, `deploy`, `duckdb-nsql`, `embedding-gemma`, `exaone`, `falcon`, `firefunction`, `gemma`, `glm`, `glm5`, `gpt-2`, `gpt-oss`, `granite-code`, `granite-embedding`, `granite-guardian`, `granite`, `granite4`, `internlm`, `jamba`, `kimi`, `laguna`, `lfm`, `llama-guard-3`, `llama`, `llava`, `magicoder`, `magistral`, `medgemma`, `meditron`, `minicpm-v`, `minimax`, `mistral-family`, `mistral`, `mixtral`, `moondream`, `mxbai`, `mythomax`, `nemotron`, `nemotron4`, `neural-chat`, `nomic-embed`, `nous-hermes`, `nuextract`, `obsidian`, `olmo`, `openchat`, `opencoder`, `openhermes`, `paligemma`, `paraphrase-multilingual`, `phi`, `phind-codellama`, `pixtral`, `qwen-embedding`, `qwen`, `qwen2.5-coder`, `reader-lm`, `recurrentgemma`, `reflection`, `samantha`, `shieldgemma`, `smollm`, `snowflake-arctic-embed`, `solar`, `sqlcoder`, `stablelm`, `starcoder`, `tinyllama`, `translategemma`, `tulu`, `whisper`, `wizardcoder`, `wizardlm`, `yi`, `zamba2`, `zephyr`, plus `index.html`, `note.md`, `note2.md`, `pricing.html`, and `quote.html`.

## Recommended Jet Agent model lane folders

Each one deserves an `index.html` sales page, even if the local family already exists elsewhere.

| Priority | Folder | Model / family | Jet Agent positioning | Relationship to local model catalog |
|---:|---|---|---|---|
| 1 | `/models/gpt-oss-cloud/` | `gpt-oss` | Flagship cloud reasoning and agentic work. | Keep `/models/gpt-oss/` for local/open-weight SEO. |
| 2 | `/models/qwen3.5-cloud/` | `qwen3.5` | Strong all-rounder for thinking, tools, multimodal, and business workflows. | Separate from `/models/qwen/`. |
| 3 | `/models/gemma4-cloud/` | `gemma4` | Google-backed multimodal and general-purpose cloud option. | Separate from `/models/gemma/`. |
| 4 | `/models/qwen3-coder-cloud/` | `qwen3-coder` | Coding agents, long-context development, repository work. | Separate from `/models/qwen2.5-coder/`. |
| 5 | `/models/qwen3-coder-next-cloud/` | `qwen3-coder-next` | Next-generation coding agent lane. | New cloud-only folder. |
| 6 | `/models/qwen3.6-cloud/` | `qwen3.6` | Newer Qwen agentic coding and thinking family. | New cloud-only folder. |
| 7 | `/models/deepseek-v3.2-cloud/` | `deepseek-v3.2` | Efficient reasoning and agent performance. | Separate from `/models/deepseek/`. |
| 8 | `/models/deepseek-v3.1-cloud/` | `deepseek-v3.1` | Hybrid thinking/non-thinking DeepSeek lane. | Separate from `/models/deepseek/`. |
| 9 | `/models/deepseek-v4-pro-cloud/` | `deepseek-v4-pro` | Frontier MoE reasoning, long context, multi-mode reasoning. | New cloud-only folder. |
| 10 | `/models/deepseek-v4-flash-cloud/` | `deepseek-v4-flash` | Fast, efficient DeepSeek reasoning cloud option. | New cloud-only folder. |
| 11 | `/models/glm-5.2-cloud/` | `glm-5.2` | Long-horizon tasks and agentic workflows. | Separate from `/models/glm5/`. |
| 12 | `/models/glm-5.1-cloud/` | `glm-5.1` | Agentic engineering and coding. | Separate from `/models/glm5/`. |
| 13 | `/models/glm-5-cloud/` | `glm-5` | Large reasoning and agentic model. | Separate from `/models/glm5/`. |
| 14 | `/models/glm-4.7-cloud/` | `glm-4.7` | Coding capability and technical work. | Separate from `/models/glm/`. |
| 15 | `/models/minimax-m3-cloud/` | `minimax-m3` | Coding and agentic frontier with multimodality. | Separate from `/models/minimax/`. |
| 16 | `/models/minimax-m2.7-cloud/` | `minimax-m2.7` | Coding, productivity, and agentic workflows. | Separate from `/models/minimax/`. |
| 17 | `/models/minimax-m2.5-cloud/` | `minimax-m2.5` | Productivity and coding cloud option. | Separate from `/models/minimax/`. |
| 18 | `/models/minimax-m2.1-cloud/` | `minimax-m2.1` | Multilingual code engineering. | Separate from `/models/minimax/`. |
| 19 | `/models/kimi-k2.7-code-cloud/` | `kimi-k2.7-code` | Moonshot coding-focused agentic cloud model. | Separate from `/models/kimi/`. |
| 20 | `/models/kimi-k2.6-cloud/` | `kimi-k2.6` | Long-horizon coding, design, and autonomous execution. | Separate from `/models/kimi/`. |
| 21 | `/models/kimi-k2.5-cloud/` | `kimi-k2.5` | Native multimodal agentic model. | Separate from `/models/kimi/`. |
| 22 | `/models/nemotron-3-ultra-cloud/` | `nemotron-3-ultra` | NVIDIA long-running agent workflows and high-throughput reasoning. | Separate from `/models/nemotron/`. |
| 23 | `/models/nemotron-3-super-cloud/` | `nemotron-3-super` | Efficient complex multi-agent work. | Separate from `/models/nemotron/`. |
| 24 | `/models/nemotron-3-nano-cloud/` | `nemotron-3-nano` | Efficient open agentic model with cloud option. | Separate from `/models/nemotron/`. |
| 25 | `/models/nemotron-cascade-2-cloud/` | `nemotron-cascade-2` | Efficient MoE reasoning. | New cloud-only folder. |
| 26 | `/models/devstral-2-cloud/` | `devstral-2` | Large coding agent model. | Separate from Mistral local/coding folders. |
| 27 | `/models/devstral-small-2-cloud/` | `devstral-small-2` | Codebase exploration and multi-file editing. | Separate from Mistral local/coding folders. |
| 28 | `/models/ministral-3-cloud/` | `ministral-3` | Edge-oriented Mistral cloud/vision/tool model. | Separate from `/models/mistral/`. |
| 29 | `/models/mistral-large-3-cloud/` | `mistral-large-3` | Production-grade multimodal MoE cloud model. | Separate from `/models/mistral/`. |
| 30 | `/models/gemini-3-flash-preview-cloud/` | `gemini-3-flash-preview` | Speed-focused frontier cloud model. | New cloud-only folder; needs careful branding review. |
| 31 | `/models/rnj-1-cloud/` | `rnj-1` | 8B code/STEM cloud-supporting model. | New cloud-only folder. |

## Deprecated or risky cloud items

Do not prioritize these as new customer-facing sales pages unless they are retained only as redirect/comparison content:

| Model | Recommended alternative |
|---|---|
| `kimi-k2-thinking` | `kimi-k2.6` |
| `kimi-k2:1t` | `kimi-k2.6` |
| `minimax-m2` | `minimax-m3` |
| `glm-4.6` | `glm-5.1` |
| `qwen3-next:80b` | `qwen3.5` |
| `qwen3-vl:235b` | `qwen3.5` |
| `qwen3-vl:235b-instruct` | `qwen3.5` |
| `cogito-2.1:671b` | `deepseek-v4-flash` |

## Recommended Jet Agent page build order

1. `/models/gpt-oss-cloud/index.html`
2. `/models/qwen3.5-cloud/index.html`
3. `/models/gemma4-cloud/index.html`
4. `/models/qwen3-coder-cloud/index.html`
5. `/models/deepseek-v4-flash-cloud/index.html`
6. `/models/kimi-k2.6-cloud/index.html`
7. `/models/kimi-k2.7-code-cloud/index.html`
8. `/models/minimax-m3-cloud/index.html`
9. `/models/glm-5.2-cloud/index.html`
10. `/models/nemotron-3-ultra-cloud/index.html`
11. `/models/mistral-large-3-cloud/index.html`
12. `/models/devstral-2-cloud/index.html`

## Recommended CTA language

Use this CTA box across Jet Agent model lane pages:

> **Add this Jet Agent model lane to terminal.glass**  
> Use this cloud-backed model lane when your business wants stronger answers, faster reasoning, coding help, or model variety without buying a large GPU server. Jet Agents are available through the customer's terminal.glass package and Glass License capacity.
>
> Button: **Build my terminal.glass launch plan**

## Short sales distinction

Use this plain explanation somewhere near the top of every Jet Agent cloud family page:

> NoCloudGPT is for customers who want AI running on their own server. Jet Agent model lanes are for customers who want powerful cloud-backed model workflows inside terminal.glass without buying GPU hardware first. The strongest value is model choice, speed, and useful agent work, not only privacy.

## Data file

Maintain the cloud family list in:

```text
/models/data/terminal-glass-cloud-models.json
```

Each entry should include:

```json
{
  "slug": "gpt-oss-cloud",
  "displayName": "GPT-OSS Jet Agent Lane",
  "ollamaFamily": "gpt-oss",
  "exampleRun": "ollama run gpt-oss:120b-cloud",
  "category": "reasoning-agentic",
  "priority": 1,
  "folder": "/models/gpt-oss-cloud/",
  "localFamilyFolder": "/models/gpt-oss/",
  "deploymentMode": "jet-agent-model-lane",
  "licenseModel": "Glass License package capacity",
  "status": "priority"
}
```

This gives the site one maintainable list that can feed the cloud model index, quote page, and sidebar CTA boxes while keeping every Jet Agent model lane as its own clean sales family folder.
