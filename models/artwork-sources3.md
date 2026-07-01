# NoCloudGPT — Artwork Sources v3 (Multi-Image Expansion)

**Purpose**  
Expanded manifest supporting **hero + secondary/mid-article** artwork for richer model family pages. Builds on v2 (Wikimedia focus for families without Ollama heroes).

**Image Roles**
- `hero.webp` — Primary top banner
- `secondary.webp` — Mid-page visual break (left or right aligned, smaller)
- `card.webp` — Catalog / grid use (can reuse hero crop or create dedicated)
- Keep `og.webp` and `brand.webp` as before when needed.

**Naming & Optimization Rules**
- All images: WebP, optimized, < 150KB preferred for secondary.
- Hero remains the largest/most impactful.
- Secondary should feel related but not identical (different angle, close-up, or complementary scene from same Wikimedia search).

**HTML Placement Guidance**
- Hero: Top of page (as before)
- Secondary: Insert roughly 40–60% down the article, floated left or right with caption.
- Use the same attribution style as hero but smaller.

---

## Multi-Image Table (Sample — Starting from granite-embedding)

| Folder Name            | Family Name            | Hero Search / Example                          | Secondary Search / Example                              | Recommended Secondary Role                  | Notes |
|------------------------|------------------------|------------------------------------------------|---------------------------------------------------------|---------------------------------------------|-------|
| granite-embedding     | Granite Embedding     | [Granite rock / data wide](link from v2)      | [Granite texture close-up or vector embedding viz](https://commons.wikimedia.org/w/index.php?search=granite+texture+close-up+OR+data+embedding+diagram+wide&type=image) | Material detail + tech overlay             | Good pair |
| granite-guardian      | Granite Guardian      | [Granite shield wide](link)                   | [Security / shield icon or guardian animal close](search link) | Protection / safety detail                 | — |
| grok                  | Grok                  | [Cosmic / understanding abstract](link)       | [Deeper insight or book / Heinlein related conceptual](search) | Thoughtful / understanding moment          | Abstract pair works well |
| jamba                 | Jamba                 | [River / flow landscape](link)                | [River close-up or flowing water detail](search)       | Dynamic flow detail                        | Nature pair |
| laguna                | Laguna                | [Lagoon / lake wide](link)                    | [Water reflection or lakeside detail](search)          | Serene water detail                        | Excellent |
| llama-guard           | Llama Guard           | [Llama + protection wide](link)               | [Llama face close-up or shield detail](search)         | Guard / protective animal focus            | Strong |
| llama-guard-3         | Llama Guard 3         | Same as above                                 | Same as above or variant                              | —                                          | — |
| magicoder             | Magicoder             | [Magic + code wide](link)                     | [Spellbook / code + magic close-up](search)            | Magical coding moment                      | Fun pair |
| mistral-family        | Mistral Family        | [Wind / storm coast wide](link)               | [Wind-swept landscape or storm detail](search)         | Atmospheric detail                         | Brand strong |
| moondream             | Moondream             | [Moon / night sky wide](link)                 | [Moon surface close or dreamy night detail](search)    | Lunar / dream focus                        | Beautiful pair |
| orca-mini             | Orca Mini             | [Orca ocean wide](link)                       | [Orca close-up or breaching detail](search)            | Majestic animal focus                      | Excellent |
| reflection            | Reflection            | [Mirror / thoughtful wide](link)              | [Mirror reflection close-up or philosophical detail](search) | Introspective moment                       | Conceptual gold |
| sqlcoder              | SQLCoder              | [Database / query wide](link)                 | [Code snippet or database schema close](search)        | Technical coding detail                    | Tech pair |
| tigerbot              | TigerBot              | [Tiger wide](link)                            | [Tiger face / eyes close-up](search)                   | Powerful animal detail                     | Strong |
| whisper               | Whisper               | [Sound / voice wide](link)                    | [Sound wave or listening / ear detail](search)         | Audio / voice intimacy                     | Thematic |
| wizardcoder           | WizardCoder           | [Wizard + code wide](link)                    | [Wizard staff + terminal close or spell effect](search)| Magical coding focus                       | Fun |

*(Continue this pattern for the rest of the families. For families with weaker visual themes, secondary can be a tighter crop of the hero search or a related abstract.)*

---

**Next Steps I Recommend**

1. Create `models/artwork-sources3.md` with the structure above.
2. Decide on exact filename for the mid-article image (`secondary.webp` is clear; we could also use `feature.webp` or `inline.webp` if you prefer).
3. Run a new Cursor batch focused on adding `secondary.webp` for the highest-priority families first (the ones with strong pairs above).
4. Update a few model `index.html` files with the new mid-article placement as a template.

Would you like me to:

- Generate the **full expanded table** for all remaining families in v3 format?
- Draft a complete starter `artwork-sources3.md` file (with intro + full sample table)?
- Focus first on the **top 10–12 families** with the strongest secondary opportunities and give specific search + example links?

Just tell me which direction to go and I’ll produce it right away. This is going to make the model pages feel much richer and more polished.