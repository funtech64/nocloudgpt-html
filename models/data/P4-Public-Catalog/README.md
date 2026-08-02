# P4 Public Catalog (pinned input)

This directory is the **sole catalog input** for the NoCloudGPT `/models` experience (Phase 4B). It is a read-only pin of the Phase 4A public projection from `terminal-glass/8-ball/P4-Public-Catalog/`.

The live website **never** calls Ollama at build or page-view time.

## Layout

| Path | Purpose |
|------|---------|
| `manifest.json` | Schema version, projection version, counts |
| `index/families.json` | Family index |
| `index/models.json` | Canonical model index |
| `index/browse.json` | Compact search index for `/models/` |
| `families/*.json` | Per-family records |
| `models/*.json` | Per-model records |

## Current pin

See `manifest.json` for `projectionVersion` and `generatedAt`.

## Updating the pinned input

### Preferred: copy from terminal-glass/8-ball

When Phase 4A publishes a new projection:

```bash
# From a sibling checkout of terminal-glass/8-ball (do not modify 8-ball in this repo)
./scripts/catalog/update_pinned_input.sh /path/to/terminal-glass/8-ball/P4-Public-Catalog
npm run build
npm test
```

### Fallback: re-pin from Ollama library HTML (maintainer only)

Only when 8-ball output is unavailable. This is a **one-time snapshot**, not a live crawl at runtime:

```bash
npm run pin-catalog
npm run build
npm test
```

Then commit `models/data/P4-Public-Catalog/` and regenerated HTML.

## Source exceptions

`kimi-k2.5` and `minimax-m2.5` remain in the catalog as stale source metadata:

- `noindex` on model pages
- excluded from `sitemap.xml`
- labeled as temporarily unavailable (not deleted)
