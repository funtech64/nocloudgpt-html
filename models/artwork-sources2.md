# NoCloudGPT — Artwork Sources v2 (Wikimedia + Enhanced Fallbacks)

**Purpose**  
Wikimedia Commons-focused manifest for the 52 model families without usable Ollama hero artwork (from Batch 3).  

**How to use with Cursor**  
1. Click the **Wikimedia Search Link** for a family.  
2. Pick the best wide/landscape, high-quality, properly licensed image (prefer CC0, CC-BY, CC-BY-SA).  
3. Download → optimize → save as `hero.webp` in `/models/<folder>/`.  
4. Update `index.html` with clickable link + visible attribution (same pattern as Batch 3).  
5. Add the chosen file reference to this manifest.

**HTML Pattern Reminder** (use near hero image):
```html
<!-- Artwork sourced from Wikimedia Commons (illustrative fallback). See artwork-sources2.md -->
<a href="[WIKIMEDIA_FILE_PAGE_URL]" target="_blank" rel="noopener">
  <img src="hero.webp" alt="[Model Family] hero image" loading="lazy">
</a>
<p style="font-size:0.75em; opacity:0.75; margin-top:4px;">
  Source: <a href="[WIKIMEDIA_FILE_PAGE_URL]">Wikimedia Commons</a> ([LICENSE] by [AUTHOR])
</p>

 ## Enhanced Table with Hyperlinks (Sample — First 15 from the 52)

| Folder Name              | Family Name              | Wikimedia Search Link                                                                 | Example Recommended File                                                                 | License (example)     | Notes |
|--------------------------|--------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------------------|-------|
| airoboros               | Airoboros               | [Search wide AI / robotics imagery](https://commons.wikimedia.org/w/index.php?search=ai+robot+OR+futuristic+wide+OR+landscape+photo&type=image) | — | CC-BY-SA | Abstract tech theme |
| alpaca                  | Alpaca                  | [Search alpaca wide/landscape](https://commons.wikimedia.org/w/index.php?search=alpaca+wide+OR+landscape+OR+hero+photo&type=image) | [Alpaca in mountainous landscape (CC BY 4.0)](https://commons.wikimedia.org/wiki/File:two_alpacas_standing_in_a_moun_Wellcome_V0023090.jpg) | CC BY 4.0 | Excellent hero candidate |
| aquila                  | Aquila                  | [Search eagle OR aquila bird wide](https://commons.wikimedia.org/w/index.php?search=aquila+OR+eagle+bird+wide+OR+landscape+photo&type=image) | — | CC-BY-SA | Strong bird theme |
| arctic                  | Arctic                  | [Search arctic landscape wide](https://commons.wikimedia.org/w/index.php?search=arctic+landscape+OR+ice+wide+OR+panoramic+photo&type=image) | — | CC0 / CC-BY | Nature hero potential |
| arctic-llm              | Arctic LLM              | [Search arctic landscape wide](https://commons.wikimedia.org/w/index.php?search=arctic+landscape+OR+ice+wide+OR+panoramic+photo&type=image) | — | CC0 / CC-BY | Same as above |
| bagel                   | Bagel                   | [Search bagel food wide OR artistic](https://commons.wikimedia.org/w/index.php?search=bagel+food+OR+bakery+wide+photo&type=image) | — | CC-BY | Playful / low priority |
| baichuan                | Baichuan                | [Search Chinese river OR mountain wide](https://commons.wikimedia.org/w/index.php?search=baichuan+OR+chinese+river+mountain+landscape&type=image) | — | CC-BY-SA | Cultural theme |
| bakllava                | Bakllava                | [Search baklava OR middle eastern dessert wide](https://commons.wikimedia.org/w/index.php?search=baklava+OR+dessert+food+wide+photo&type=image) | — | CC-BY | Low priority |
| chatglm                 | ChatGLM                 | [Search neural network OR conversation abstract wide](https://commons.wikimedia.org/w/index.php?search=neural+network+OR+ai+conversation+wide+abstract&type=image) | — | CC-BY-SA | Tech abstract |
| chatgpt-alternatives    | ChatGPT Alternatives    | [Search ai chat interface OR comparison wide](https://commons.wikimedia.org/w/index.php?search=ai+chat+interface+OR+multiple+ai+models+wide&type=image) | — | CC-BY | Meta / low priority |
| deploy                  | Deploy                  | [Search data center OR cloud infrastructure wide](https://commons.wikimedia.org/w/index.php?search=data+center+OR+server+room+OR+cloud+infrastructure+wide+photo&type=image) | — | CC0 / CC-BY | High practical value |
| firefunction            | Firefunction            | [Search fire OR flame OR function abstract wide](https://commons.wikimedia.org/w/index.php?search=fire+flame+OR+abstract+code+wide+photo&type=image) | — | CC-BY-SA | — |
| glm                     | GLM                     | [Search Chinese tech OR ai research wide](https://commons.wikimedia.org/w/index.php?search=chinese+ai+OR+tech+research+wide+photo&type=image) | — | CC-BY-SA | — |
| glm5                    | GLM 5                   | [Search Chinese tech OR ai research wide](https://commons.wikimedia.org/w/index.php?search=chinese+ai+OR+tech+research+wide+photo&type=image) | — | CC-BY-SA | — |
| gpt-2                   | GPT-2                   | [Search vintage computer OR early ai OR transformer diagram wide](https://commons.wikimedia.org/w/index.php?search=vintage+computer+OR+early+ai+OR+transformer+diagram+wide+photo&type=image) | — | Public domain / CC0 | Historical |


| granite-embedding       | Granite Embedding       | [Search granite rock OR embedding vector wide landscape](https://commons.wikimedia.org/w/index.php?search=granite+rock+OR+embedding+vector+OR+data+wide+landscape+photo&type=image) | — | CC-BY / CC0 | Tech + nature hybrid |
| granite-guardian        | Granite Guardian        | [Search granite shield OR guardian security wide](https://commons.wikimedia.org/w/index.php?search=granite+shield+OR+guardian+security+OR+protection+wide+photo&type=image) | — | CC-BY | Safety / enterprise |
| grok                    | Grok                    | [Search grok understanding OR cosmic insight OR abstract wide](https://commons.wikimedia.org/w/index.php?search=grok+OR+understanding+OR+cosmic+insight+abstract+wide+photo&type=image) | — | CC-BY-SA | Thematic (use abstract) |
| jamba                   | Jamba                   | [Search jamba river OR flow OR african landscape wide](https://commons.wikimedia.org/w/index.php?search=jamba+river+OR+flow+OR+african+landscape+wide+photo&type=image) | — | CC-BY | Nature / flow theme |
| laguna                  | Laguna                  | [Search laguna lake OR lagoon landscape wide](https://commons.wikimedia.org/w/index.php?search=laguna+OR+lagoon+lake+landscape+wide+photo&type=image) | — | CC0 / CC-BY | Strong nature hero |
| llama-guard             | Llama Guard             | [Search llama guard OR llama shield OR protection animal wide](https://commons.wikimedia.org/w/index.php?search=llama+guard+OR+llama+shield+OR+protection+wide+photo&type=image) | — | CC-BY | Strong thematic match |
| llama-guard-3           | Llama Guard 3           | [Search llama guard OR llama shield OR protection animal wide](https://commons.wikimedia.org/w/index.php?search=llama+guard+OR+llama+shield+OR+protection+wide+photo&type=image) | — | CC-BY | Same as above |
| magicoder               | Magicoder               | [Search magic coder OR wizard code OR magical programming wide](https://commons.wikimedia.org/w/index.php?search=magic+OR+wizard+code+OR+programming+abstract+wide+photo&type=image) | — | CC-BY-SA | Fun coding theme |
| mimo                    | Mimo                    | [Search mimo antenna OR communication wide abstract](https://commons.wikimedia.org/w/index.php?search=mimo+antenna+OR+communication+wide+abstract+photo&type=image) | — | CC-BY | Tech abstract |
| ministral               | Ministral               | [Search ministral OR small storm OR wind mistral wide](https://commons.wikimedia.org/w/index.php?search=ministral+OR+small+storm+OR+wind+mistral+wide+photo&type=image) | — | CC-BY | Mistral wind theme |
| mistral-family          | Mistral Family          | [Search mistral wind OR storm OR french coast landscape wide](https://commons.wikimedia.org/w/index.php?search=mistral+wind+OR+storm+OR+french+coast+landscape+wide+photo&type=image) | — | CC-BY-SA | Strong brand/nature match |
| moondream               | Moondream               | [Search moon dream OR night sky OR lunar landscape wide](https://commons.wikimedia.org/w/index.php?search=moon+dream+OR+night+sky+OR+lunar+landscape+wide+photo&type=image) | — | CC0 / CC-BY | Excellent hero potential |
| mxbai                   | Mixedbread              | [Search mixed bread OR bakery OR embedding mix abstract wide](https://commons.wikimedia.org/w/index.php?search=mixed+bread+OR+bakery+OR+embedding+mix+wide+photo&type=image) | — | CC-BY | Playful / low priority |
| mythomax                | MythoMax                | [Search mythology OR myth max OR legendary hero wide](https://commons.wikimedia.org/w/index.php?search=mythology+OR+myth+max+OR+legendary+hero+wide+photo&type=image) | — | CC-BY-SA | Mythic theme |
| nemotron4               | Nemotron 4              | [Search nemotron OR nvidia robot OR neural trooper wide](https://commons.wikimedia.org/w/index.php?search=nemotron+OR+nvidia+robot+OR+neural+trooper+wide+photo&type=image) | — | CC-BY | Tech / robot |
| noroma                  | Noroma                  | [Search abstract OR noroma concept wide](https://commons.wikimedia.org/w/index.php?search=abstract+OR+noroma+concept+wide+photo&type=image) | — | — | Low priority / placeholder likely |
| nuextract               | Nuextract               | [Search data extraction OR mining OR document wide](https://commons.wikimedia.org/w/index.php?search=data+extraction+OR+mining+OR+document+wide+photo&type=image) | — | CC-BY | Tech / data |
| obsidian                | Obsidian                | [Search obsidian stone OR volcanic glass OR black stone wide](https://commons.wikimedia.org/w/index.php?search=obsidian+stone+OR+volcanic+glass+OR+black+stone+wide+photo&type=image) | — | CC-BY | Strong material theme |
| openclaw                | OpenClaw                | [Search open claw OR animal claw OR open source wide](https://commons.wikimedia.org/w/index.php?search=open+claw+OR+animal+claw+OR+open+source+wide+photo&type=image) | — | CC-BY | Low priority |
| orca-mini               | Orca Mini               | [Search orca OR "killer whale" wide landscape ocean](https://commons.wikimedia.org/w/index.php?search=orca+OR+%22killer+whale%22+wide+OR+landscape+OR+ocean+photo&type=image) | — | CC-BY / CC0 | Excellent animal hero |
| paligemma               | PaliGemma               | [Search pali gemma OR vision multimodal OR gem landscape wide](https://commons.wikimedia.org/w/index.php?search=pali+gemma+OR+vision+multimodal+OR+gem+landscape+wide+photo&type=image) | — | CC-BY | Vision / gem theme |
| pangu                   | Pangu                   | [Search pangu chinese mythology OR creator cosmic wide](https://commons.wikimedia.org/w/index.php?search=pangu+chinese+mythology+OR+creator+cosmic+wide+photo&type=image) | — | CC-BY-SA | Cultural / mythic |
| paraphrase-multilingual | Paraphrase Multilingual | [Search language translation OR multilingual globe wide](https://commons.wikimedia.org/w/index.php?search=language+translation+OR+multilingual+globe+OR+text+layers+wide+photo&type=image) | — | CC-BY | Language theme |
| qwen-embedding          | Qwen Embedding          | [Search qwen embedding OR chinese tech vector wide](https://commons.wikimedia.org/w/index.php?search=qwen+embedding+OR+chinese+tech+vector+wide+photo&type=image) | — | CC-BY | Tech embedding |
| recurrentgemma          | RecurrentGemma          | [Search recurrent gemma OR loop OR cycle abstract wide](https://commons.wikimedia.org/w/index.php?search=recurrent+gemma+OR+loop+OR+cycle+abstract+wide+photo&type=image) | — | CC-BY | Abstract / loop |
| reflection              | Reflection              | [Search reflection mirror OR thoughtful self wide](https://commons.wikimedia.org/w/index.php?search=reflection+mirror+OR+thoughtful+self+OR+philosophical+wide+photo&type=image) | — | CC-BY-SA | Strong conceptual hero |
| reka                    | Reka                    | [Search reka abstract OR concept wide](https://commons.wikimedia.org/w/index.php?search=reka+abstract+OR+concept+wide+photo&type=image) | — | — | Low priority / placeholder |
| samantha                | Samantha                | [Search samantha ai companion OR sci-fi character wide](https://commons.wikimedia.org/w/index.php?search=samantha+ai+companion+OR+sci-fi+character+wide+photo&type=image) | — | CC-BY | Low priority |
| seallm                  | SeaLLM                  | [Search sea llm OR ocean ai OR marine wide](https://commons.wikimedia.org/w/index.php?search=sea+llm+OR+ocean+ai+OR+marine+wide+photo&type=image) | — | CC-BY | Ocean theme |
| snowball                | Snowball                | [Search snowball OR avalanche OR compounding wide](https://commons.wikimedia.org/w/index.php?search=snowball+OR+avalanche+OR+compounding+wide+photo&type=image) | — | CC0 / CC-BY | Nature / effect theme |
| sqlcoder                | SQLCoder                | [Search sql coder OR database query OR code wide](https://commons.wikimedia.org/w/index.php?search=sql+coder+OR+database+query+OR+code+wide+photo&type=image) | — | CC-BY | Strong tech / code |
| tigerbot                | TigerBot                | [Search tiger bot OR tiger animal wide landscape](https://commons.wikimedia.org/w/index.php?search=tiger+bot+OR+tiger+animal+wide+OR+landscape+photo&type=image) | — | CC-BY | Excellent animal hero |
| whisper                 | Whisper                 | [Search whisper sound OR audio speech OR voice wide](https://commons.wikimedia.org/w/index.php?search=whisper+sound+OR+audio+speech+OR+voice+wide+photo&type=image) | — | CC-BY-SA | Strong audio / voice theme |
| wizardcoder             | WizardCoder             | [Search wizard coder OR magical code OR programming wizard wide](https://commons.wikimedia.org/w/index.php?search=wizard+coder+OR+magical+code+OR+programming+wizard+wide+photo&type=image) | — | CC-BY | Fun coding + magic |
| wizardlm2               | WizardLM 2              | [Search wizard lm OR magical language model wide](https://commons.wikimedia.org/w/index.php?search=wizard+lm+OR+magical+language+model+wide+photo&type=image) | — | CC-BY | Same wizard theme |
| zamba                   | Zamba                   | [Search zamba zebra OR efficiency abstract wide](https://commons.wikimedia.org/w/index.php?search=zamba+zebra+OR+efficiency+abstract+wide+photo&type=image) | — | CC-BY | Animal / efficiency |
| zamba2                  | Zamba 2                 | [Search zamba zebra OR efficiency abstract wide](https://commons.wikimedia.org/w/index.php?search=zamba+zebra+OR+efficiency+abstract+wide+photo&type=image) | — | CC-BY | Same as above |