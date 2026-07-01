# NoCloudGPT — Artwork Sources v3 (Secondary / Mid-Article Images)

**Purpose**  
Source `secondary.webp` mid-article images for model families that lack Ollama hero artwork.  
Use Wikimedia Commons (CC0 / CC-BY / CC-BY-SA only). Cache processed files under `models/art/<folder>/`.

**Image Roles**
- `hero.webp` — Primary top banner
- `secondary.webp` — Mid-page visual break (left or right aligned, smaller)
- `card.webp` — Catalog / grid use (can reuse hero crop or create dedicated)

**Rules**
- Only families with an existing `index.html` (no new folders).
- Do **not** copy into live family folders until integration step.
- Prefer a different angle/composition from any existing hero.
- Target output: `secondary.webp` ~700–900px wide, under ~150 KB.
- All images: WebP, optimized. Secondary should feel related but not identical.

**HTML Placement Guidance**
- Hero: Top of page (as before)
- Secondary: Insert roughly 40–60% down the article, floated left or right with caption.
- Use the same attribution style as hero but smaller.

---

## Families Needing Secondary Artwork (Batch 3 — Processed)

| # | Folder | Family | Wikimedia Search Link | Search Theme |
|---|--------|--------|----------------------|--------------|
| 1 | airoboros | Airoboros | https://commons.wikimedia.org/w/index.php?search=dragon+mythology&title=Special:MediaSearch&type=image | dragon mythology |
| 2 | alpaca | Alpaca | https://commons.wikimedia.org/w/index.php?search=alpaca+animal+farm&title=Special:MediaSearch&type=image | alpaca animal |
| 3 | aquila | Aquila | https://commons.wikimedia.org/w/index.php?search=aquila+eagle&title=Special:MediaSearch&type=image | aquila eagle |
| 4 | arctic | Arctic | https://commons.wikimedia.org/w/index.php?search=arctic+landscape+ice&title=Special:MediaSearch&type=image | arctic landscape |
| 5 | arctic-llm | Arctic LLM | https://commons.wikimedia.org/w/index.php?search=arctic+glacier&title=Special:MediaSearch&type=image | arctic glacier |
| 6 | bagel | Bagel | https://commons.wikimedia.org/w/index.php?search=bagel+bread&title=Special:MediaSearch&type=image | bagel bread |
| 7 | baichuan | Baichuan | https://commons.wikimedia.org/w/index.php?search=yellow+river+china&title=Special:MediaSearch&type=image | yellow river china |
| 8 | bakllava | BakLLaVA | https://commons.wikimedia.org/w/index.php?search=baklava+pastry&title=Special:MediaSearch&type=image | baklava pastry |
| 9 | chatglm | ChatGLM | https://commons.wikimedia.org/w/index.php?search=chinese+calligraphy&title=Special:MediaSearch&type=image | chinese calligraphy |
| 10 | devstral-2-cloud | Devstral 2 Cloud | https://commons.wikimedia.org/w/index.php?search=software+development+workspace&title=Special:MediaSearch&type=image | software workspace |
| 11 | devstral-small-2-cloud | Devstral Small 2 Cloud | https://commons.wikimedia.org/w/index.php?search=programming+laptop&title=Special:MediaSearch&type=image | programming laptop |
| 12 | gemini-3-flash-preview-cloud | Gemini 3 Flash Cloud | https://commons.wikimedia.org/w/index.php?search=gemini+constellation&title=Special:MediaSearch&type=image | gemini constellation |
| 13 | glm | GLM | https://commons.wikimedia.org/w/index.php?search=tsinghua+university&title=Special:MediaSearch&type=image | tsinghua university |
| 14 | glm-4.7-cloud | GLM 4.7 Cloud | https://commons.wikimedia.org/w/index.php?search=artificial+intelligence+research&title=Special:MediaSearch&type=image | AI research |
| 15 | glm5 | GLM 5 | https://commons.wikimedia.org/w/index.php?search=university+research+laboratory&title=Special:MediaSearch&type=image | research laboratory |
| 16 | glm-5-cloud | GLM 5 Cloud | https://commons.wikimedia.org/w/index.php?search=neural+network+diagram&title=Special:MediaSearch&type=image | neural network |
| 17 | glm-5.1-cloud | GLM 5.1 Cloud | https://commons.wikimedia.org/w/index.php?search=computer+science+server&title=Special:MediaSearch&type=image | computer science |
| 18 | gpt-2 | GPT-2 | https://commons.wikimedia.org/w/index.php?search=vintage+computer+terminal&title=Special:MediaSearch&type=image | vintage computer |
| 19 | granite-embedding | Granite Embedding | https://commons.wikimedia.org/w/index.php?search=granite+rock+texture&title=Special:MediaSearch&type=image | granite rock |
| 20 | granite-guardian | Granite Guardian | https://commons.wikimedia.org/w/index.php?search=cybersecurity+shield&title=Special:MediaSearch&type=image | cybersecurity shield |
| 21 | grok | Grok | https://commons.wikimedia.org/w/index.php?search=cosmos+galaxy+stars&title=Special:MediaSearch&type=image | cosmos galaxy |
| 22 | jamba | Jamba | https://commons.wikimedia.org/w/index.php?search=stack+of+documents&title=Special:MediaSearch&type=image | document stack |
| 23 | laguna | Laguna | https://commons.wikimedia.org/w/index.php?search=lagoon+water&title=Special:MediaSearch&type=image | lagoon water |
| 24 | llama-guard | Llama Guard | https://commons.wikimedia.org/w/index.php?search=security+badge&title=Special:MediaSearch&type=image | security badge |
| 25 | llama-guard-3 | Llama Guard 3 | https://commons.wikimedia.org/w/index.php?search=network+security&title=Special:MediaSearch&type=image | network security |
| 26 | magicoder | Magicoder | https://commons.wikimedia.org/w/index.php?search=magic+wand&title=Special:MediaSearch&type=image | magic wand |
| 27 | mimo | Mimo | https://commons.wikimedia.org/w/index.php?search=mirror+reflection&title=Special:MediaSearch&type=image | mirror reflection |
| 28 | ministral | Ministral | https://commons.wikimedia.org/w/index.php?search=mistral+wind&title=Special:MediaSearch&type=image | mistral wind |
| 29 | mistral-family | Mistral Family | https://commons.wikimedia.org/w/index.php?search=provence+windmill&title=Special:MediaSearch&type=image | provence windmill |
| 30 | moondream | Moondream | https://commons.wikimedia.org/w/index.php?search=moon+night+sky&title=Special:MediaSearch&type=image | moon night sky |
| 31 | mxbai | Mxbai Embed | https://commons.wikimedia.org/w/index.php?search=bakery+bread&title=Special:MediaSearch&type=image | bakery bread |
| 32 | mythomax | MythoMax | https://commons.wikimedia.org/w/index.php?search=greek+mythology+statue&title=Special:MediaSearch&type=image | greek mythology |
| 33 | nemotron-3-nano-cloud | Nemotron 3 Nano Cloud | https://commons.wikimedia.org/w/index.php?search=nvidia+gpu&title=Special:MediaSearch&type=image | nvidia gpu |
| 34 | nemotron-3-super-cloud | Nemotron 3 Super Cloud | https://commons.wikimedia.org/w/index.php?search=supercomputer+data+center&title=Special:MediaSearch&type=image | supercomputer |
| 35 | nemotron4 | Nemotron 4 | https://commons.wikimedia.org/w/index.php?search=server+rack+datacenter&title=Special:MediaSearch&type=image | server rack |
| 36 | noroma | Noroma | https://commons.wikimedia.org/w/index.php?search=rome+colosseum&title=Special:MediaSearch&type=image | rome colosseum |
| 37 | nuextract | NuExtract | https://commons.wikimedia.org/w/index.php?search=document+scanning&title=Special:MediaSearch&type=image | document scanning |
| 38 | obsidian | Obsidian | https://commons.wikimedia.org/w/index.php?search=obsidian+volcanic+glass&title=Special:MediaSearch&type=image | obsidian glass |
| 39 | openclaw | OpenClaw | https://commons.wikimedia.org/w/index.php?search=crab+claw+ocean&title=Special:MediaSearch&type=image | crab claw |
| 40 | orca-mini | Orca Mini | https://commons.wikimedia.org/w/index.php?search=orca+whale+breaching&title=Special:MediaSearch&type=image | orca whale |
| 41 | paligemma | PaliGemma | https://commons.wikimedia.org/w/index.php?search=camera+lens+photography&title=Special:MediaSearch&type=image | camera lens |
| 42 | pangu | Pangu | https://commons.wikimedia.org/w/index.php?search=chinese+mythology+mountain&title=Special:MediaSearch&type=image | chinese mythology |
| 43 | paraphrase-multilingual | Paraphrase Multilingual | https://commons.wikimedia.org/w/index.php?search=world+languages+globe&title=Special:MediaSearch&type=image | world languages |
| 44 | qwen-embedding | Qwen Embedding | https://commons.wikimedia.org/w/index.php?search=semantic+search+diagram&title=Special:MediaSearch&type=image | semantic search |
| 45 | recurrentgemma | RecurrentGemma | https://commons.wikimedia.org/w/index.php?search=spiral+pattern&title=Special:MediaSearch&type=image | spiral pattern |
| 46 | reflection | Reflection | https://commons.wikimedia.org/w/index.php?search=lake+reflection+mountain&title=Special:MediaSearch&type=image | lake reflection |
| 47 | reka | Reka | https://commons.wikimedia.org/w/index.php?search=northern+lights+finland&title=Special:MediaSearch&type=image | northern lights |
| 48 | rnj-1-cloud | RNJ-1 Cloud | https://commons.wikimedia.org/w/index.php?search=neural+network+visualization&title=Special:MediaSearch&type=image | neural network viz |
| 49 | samantha | Samantha | https://commons.wikimedia.org/w/index.php?search=voice+assistant+microphone&title=Special:MediaSearch&type=image | voice assistant |
| 50 | seallm | SeaLLM | https://commons.wikimedia.org/w/index.php?search=southeast+asia+map&title=Special:MediaSearch&type=image | southeast asia |
| 51 | snowball | Snowball | https://commons.wikimedia.org/w/index.php?search=snowball+winter&title=Special:MediaSearch&type=image | snowball winter |
| 52 | sqlcoder | SQLCoder | https://commons.wikimedia.org/w/index.php?search=database+sql&title=Special:MediaSearch&type=image | database sql |
| 53 | tigerbot | TigerBot | https://commons.wikimedia.org/w/index.php?search=tiger+wildlife&title=Special:MediaSearch&type=image | tiger wildlife |
| 54 | whisper | Whisper | https://commons.wikimedia.org/w/index.php?search=microphone+speech+recording&title=Special:MediaSearch&type=image | microphone speech |
| 55 | wizardcoder | WizardCoder | https://commons.wikimedia.org/w/index.php?search=wizard+hat+book&title=Special:MediaSearch&type=image | wizard hat |
| 56 | wizardlm2 | WizardLM 2 | https://commons.wikimedia.org/w/index.php?search=open+book+library&title=Special:MediaSearch&type=image | open book |
| 57 | zamba | Zamba | https://commons.wikimedia.org/w/index.php?search=efficient+energy+lightbulb&title=Special:MediaSearch&type=image | energy efficient |
| 58 | zamba2 | Zamba2 | https://commons.wikimedia.org/w/index.php?search=compact+technology+chip&title=Special:MediaSearch&type=image | compact chip |

**Cache status:** See `models/art/processing-log.md` for source URLs, licenses, and attribution per family.
