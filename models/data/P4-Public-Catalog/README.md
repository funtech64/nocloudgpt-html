# P4 Public Catalog (pinned input)

Read-only pin of `terminal-glass/8-ball/P4-Public-Catalog/`. **Do not hand-edit.**

The live site never calls Ollama at build or page-view time.

## Update

Copy the exact projection from 8-ball (not `pin_snapshot.py`):

```bash
./scripts/catalog/update_pinned_input.sh /path/to/terminal-glass/8-ball/P4-Public-Catalog
npm run build
npm test
```

## Consumption

See `CONSUMPTION.md` and `CLASSIFICATIONS.md` from the 8-ball projection for field contracts.

Derived at build time (not pinned): `models/data/catalog-browse.json`
