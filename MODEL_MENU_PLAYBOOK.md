MODEL_MENU_PLAYBOOK.md — NoCloudGPT Model Catalog Standard

Core rule

Family pages persuade and route.

Size pages specify and validate.

A model-family page should answer:

1. What is this model family good at?
2. Who developed it?
3. Who should choose it?
4. What size range makes sense?
5. What NoCloudGPT deployment tier is realistic?

Standard model-family page sections

Every important model-family page should include:

1. Hero
2. What this model family is
3. Who developed it
4. Why teams choose it
5. Best-fit workloads
6. Which size should you choose?
7. Hardware and deployment reality
8. When to choose another model
9. Deploy this model with NoCloudGPT
10. Related pages
11. Artwork checklist

Size language

Use this standard language:

Size class	Buyer explanation	Deployment positioning
Under 1B	Tiny models for experiments and constrained machines	Fast but limited
1B–4B	Lightweight local assistants	Starter private AI
7B–9B	Practical first serious model	Best default for many users
12B–14B	Better writing, reasoning, and coding	Quality upgrade tier
20B–34B	Stronger professional use	Advanced private AI
70B+	Higher-quality output with serious hardware needs	GPU/on-premise recommended
MoE	Specialized efficiency with deployment complexity	Hardware review required
Embeddings	Search/RAG infrastructure, not chatbots	Private knowledge-base model
Vision	Image, screenshot, and document understanding	Multimodal deployment

Required deployment caveat

Use language like:

“Actual RAM use and speed depend on quantization, context length, hardware, active users, and the exact Ollama tag selected. NoCloudGPT helps choose a realistic model before the customer overbuys hardware or installs something too slow for daily use.”

Page update batches

Batch 1 — flagship pages

Heavy rewrite if needed:

* /models/llama/
* /models/deepseek/
* /models/qwen/
* /models/gemma/
* /models/mistral/
* /models/phi/
* /models/gpt-oss/
* /models/granite/
* /models/hermes/
* /models/mixtral/
* /models/codellama/
* /models/qwen-coder/
* /models/deepseek-coder/
* /models/llava/
* /models/embeddings/

Batch 2 — high-value specialty pages

Medium-heavy rewrite:

* /models/llama3-1/
* /models/llama3-2/
* /models/llama3-3/
* /models/llama4/
* /models/gemma2/
* /models/gemma3/
* /models/gemma3n/
* /models/qwen2-5/
* /models/qwen3/
* /models/qwen3-vl/
* /models/mistral-nemo/
* /models/mistral-small/
* /models/mistral-large/
* /models/codestral/
* /models/starcoder2/

Batch 3 — developer, reasoning, enterprise

Medium rewrite:

* /models/deepseek-r1/
* /models/deepseek-v3/
* /models/deepseek-coder-v2/
* /models/phi3/
* /models/phi4/
* /models/phi4-reasoning/
* /models/granite-code/
* /models/granite4/
* /models/command-r/
* /models/nemotron/
* /models/glm/
* /models/kimi/
* /models/minimax/
* /models/cogito/
* /models/magistral/

Batch 4 — lightweight, legacy, niche

Light-to-medium rewrite:

* /models/tinyllama/
* /models/smollm/
* /models/smollm2/
* /models/orca-mini/
* /models/dolphin/
* /models/dolphin-llama3/
* /models/dolphin-mistral/
* /models/zephyr/
* /models/yi/
* /models/falcon/
* /models/olmo/
* /models/moondream/
* /models/minicpm-v/
* /models/bge-m3/
* /models/nomic-embed-text/

Cursor batch instruction

When updating a batch:

* Work page by page.
* Do not skip pages.
* Do not rewrite more than necessary.
* If a page is strong, polish missing sections only.
* If a page is thin, upgrade it to the standard structure.
* Preserve CTAs.
* Preserve design system.
* Add VERIFY: beside uncertain facts.
* Do not invent benchmark numbers.
* Do not invent partnerships.

For each page, provide:

* changed files
* short change summary
* facts needing verification
* artwork TODO
* deployment QA note