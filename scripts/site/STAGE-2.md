# Stage 2 public chrome

Existing model pages now take their marked ecosystem bar/navigation and marked
shared footer from `scripts/catalog/chrome.py`. Storefront links point directly
to `https://shop.nocloudgpt.com`; `colorschat.com` is labeled Website. The
deployment and Glass License links retain their terminal.glass destinations.
The shared header CSS also keeps the storefront button's white label above the
general black navigation-link rule and gives header/footer links visible focus.

Run `python3 scripts/catalog/sync_public_chrome.py` after changing shared chrome.
Use `--check` to detect drift without writing. The script only replaces the two
marked regions. It preserves artwork, metadata, editorial and legal footers,
prices, deployment links and other content outside them byte-for-byte. It
validates the full batch before writing and fails on ambiguous marked blocks.

Validation:

```sh
python3 -m unittest discover -s scripts/site -p 'test_*.py' -v
python3 scripts/catalog/sync_public_chrome.py --check --verify-editorial-against 9df242be205013190b6efcb81e0151c73d1726e9
python3 scripts/catalog/test_catalog_build.py
git diff --exit-code -- models/index.html
python3 -m unittest discover -s scripts/site -p 'test_*.py' -v
python3 scripts/catalog/sync_public_chrome.py --check
```

The workflow checks shared chrome before/after regeneration and verifies content
preservation against the PR base for the Stage 2 branch. Catalog regeneration
already updates sitemap dates and legacy font imports on generated pages; those
unrelated outputs are excluded from this Stage 2 commit.

Six pre-existing truncated editorial documents have no marked shared footer:
airoboros, glm, gpt-2, minimax, mxbai and wizardlm. Their existing marked headers
are synchronized; no footer or missing editorial content is invented. Tests
track this exact exception set so new omissions fail. Repairing the truncated
documents needs a separate editorial recovery pass.

The Stage 1 branch was deleted after PR #131 merged. It was restored at its
original head, `9df242be205013190b6efcb81e0151c73d1726e9`, for the requested
stacked PR base. Retarget Stage 2 to main before merging to the public site.
