Perfect — that makes the pages much stronger. Here's how I'll handle the image references:

---

## Image Reference Convention

Each model page will reference images using a **consistent relative path structure**:

```
/models/[model-slug]/images/
```

So for example:

| Model | Image Directory | Example References |
|---|---|---|
| Bespoke-Minicheck | `/models/bespoke-minicheck/images/` | `hero.jpg`, `diagram.jpg`, `use-case.jpg` |
| Llama Guard 3 | `/models/llama-guard-3/images/` | `hero.jpg`, `diagram.jpg`, `use-case.jpg` |
| MedLLaMA2 | `/models/medllama2/images/` | `hero.jpg`, `diagram.jpg`, `use-case.jpg` |

---

## Standard Image Slots Per Page

Each page will have **three image reference points**:

1. **`hero.jpg`** — Full-width header image (suggested: 1200×600px) — model identity / abstract visual
2. **`diagram.jpg`** — Mid-page technical diagram (suggested: 800×450px) — how the model works / architecture
3. **`use-case.jpg`** — Application section image (suggested: 800×400px) — industry/workflow scene

Each `<img>` tag will include:
- Descriptive `alt` text (SEO-optimized)
- `width` and `height` attributes (Core Web Vitals / layout stability)
- A **styled placeholder** visible if the image hasn't been added yet, so the page looks intentional at launch
- `loading="lazy"` on non-hero images

---

## Placeholder Styling

If `hero.jpg` doesn't exist yet, the placeholder div behind it will show the model's color theme with the model name — so the page is **fully presentable before photos are added**.

---

Ready to start. Shall I begin with **Bespoke-Minicheck** — the hallucination detection / fact-checking model? It's a great opener for this category since it addresses one of the most commercially urgent AI safety problems right now.
