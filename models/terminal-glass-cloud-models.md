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

## Recommended Jet Agent model lane folders

Each one deserves an `index.html` sales page, even if the local family already exists elsewhere.

| Priority | Folder | Model / family | Jet Agent positioning | Relationship to local model catalog |
|---:|---|---|---|---|
| 1 | `/models/gpt-oss-cloud/` | `gpt-oss` | Flagship cloud reasoning and agentic work. | Keep `/models/gpt-oss/` for local/open-weight SEO. |
| 2 | `/models/qwen3.5-cloud/` | `qwen3.5` | Strong all-rounder for thinking, tools, multimodal, and business workflows. | Separate from `/models/qwen/`. |
| 3 | `/models/gemma4-cloud/` | `gemma4` | Google-backed multimodal and general-purpose cloud option. | Separate from `/models/gemma/`. |
| 4 | `/models/qwen3-coder-cloud/` | `qwen3-coder` | Coding agents, long-context development, repository work. | Separate from `/models/qwen2.5-coder/`. |
| 5 | `/models/deepseek-v4-flash-cloud/` | `deepseek-v4-flash` | Fast, efficient DeepSeek reasoning cloud option. | New cloud-only folder. |
| 6 | `/models/kimi-k2.6-cloud/` | `kimi-k2.6` | Long-horizon coding, design, and autonomous execution. | Separate from `/models/kimi/`. |
| 7 | `/models/kimi-k2.7-code-cloud/` | `kimi-k2.7-code` | Moonshot coding-focused agentic cloud model. | Separate from `/models/kimi/`. |
| 8 | `/models/minimax-m3-cloud/` | `minimax-m3` | Coding and agentic frontier with multimodality. | Separate from `/models/minimax/`. |
| 9 | `/models/glm-5.2-cloud/` | `glm-5.2` | Long-horizon tasks and agentic workflows. | Separate from `/models/glm5/`. |
| 10 | `/models/nemotron-3-ultra-cloud/` | `nemotron-3-ultra` | NVIDIA long-running agent workflows and high-throughput reasoning. | Separate from `/models/nemotron/`. |
| 11 | `/models/mistral-large-3-cloud/` | `mistral-large-3` | Production-grade multimodal MoE cloud model. | Separate from `/models/mistral/`. |
| 12 | `/models/devstral-2-cloud/` | `devstral-2` | Large coding agent model. | Separate from Mistral local/coding folders. |

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
