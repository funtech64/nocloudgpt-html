#!/usr/bin/env python3
"""Shared model chrome regression checks, including editorial preservation."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "catalog"))

from chrome import site_chrome, site_footer
from apply_spectrum_chrome import active_for
from sync_public_chrome import blocks, editorial_bytes, public_pages, synchronize
from test_stage1_public_web import Markup, resolve_local

# Pre-existing truncated documents; Stage 2 preserves their bytes outside chrome.
MISSING_FOOTERS = {
    "models/airoboros/index.html", "models/glm/index.html",
    "models/gpt-2/index.html", "models/minimax/index.html",
    "models/mxbai/index.html", "models/wizardlm/index.html",
}


class PublicChromeTests(unittest.TestCase):
    def test_all_public_pages_match_source_and_are_idempotent(self) -> None:
        pages = public_pages()
        self.assertGreater(len(pages), 500)
        missing = set()
        for path in pages:
            with self.subTest(page=path.relative_to(ROOT)):
                text = path.read_bytes().decode("utf-8")
                header, footer = blocks(text)
                self.assertEqual(text, synchronize(text, active_for(path)))
                self.assertEqual(text.count('data-spectrum-chrome="1"'), 1)
                self.assertEqual(text.count('data-spectrum-artwork="1"'), 1)
                if footer is None:
                    missing.add(path.relative_to(ROOT).as_posix())
                for block in (header, footer):
                    if block is None:
                        continue
                    shared = block.group()
                    self.assertIn('href="https://shop.nocloudgpt.com"', shared)
                    self.assertIn("colorschat.com · Website", shared)
                    self.assertNotIn('href="https://colors.chat"', shared)
                    self.assertNotIn("YouTube", shared)
                    markup = Markup()
                    markup.feed(shared)
                    self.assertFalse(markup.external_target_links_without_noopener)
                    for href in markup.hrefs:
                        local = resolve_local(href)
                        if local is not None:
                            self.assertTrue(local.is_file(), f"Broken shared link: {href}")
        self.assertEqual(missing, MISSING_FOOTERS)

    def test_sync_preserves_every_byte_outside_marked_blocks(self) -> None:
        # Include old storefront links, metadata, artwork, scripts and a legal
        # footer outside the shared shell to catch broad replacement regressions.
        before = ('<!doctype html>\r\n<head><title>Editorial title</title></head>\r\n'
                  '<body class="bg-slate-950">' + site_chrome()
                  + '<main>Model pricing $199 — <a href="https://colors.chat">Original</a></main>'
                  '<footer>Developer licensing disclaimer</footer>'
                  '<script>const label = "colorschat.com · YouTube";</script>'
                  + site_footer() + '\r\n</body></html>')
        before = before.replace('href="https://shop.nocloudgpt.com"', 'href="https://colors.chat"')
        after = synchronize(before, "models")
        self.assertNotEqual(before, after)
        self.assertEqual(editorial_bytes(before), editorial_bytes(after))
        self.assertEqual(after, synchronize(after, "models"))
        self.assertIn('<footer>Developer licensing disclaimer</footer>', after)
        self.assertIn('<a href="https://colors.chat">Original</a>', after)

    def test_missing_footer_is_not_invented(self) -> None:
        before = '<body>' + site_chrome() + '<main>Truncated editorial'
        after = synchronize(before, "models")
        self.assertEqual(editorial_bytes(before), editorial_bytes(after))
        self.assertNotIn('data-spectrum-footer="1"', after)

    def test_ambiguous_or_incomplete_chrome_fails_closed(self) -> None:
        for html in ('<body>Unmarked page</body>', site_chrome() * 2,
                     site_chrome() + site_footer() * 2,
                     site_chrome() + '<footer data-spectrum-footer="1">Truncated'):
            with self.subTest(html=html[:50]), self.assertRaises(ValueError):
                synchronize(html, "models")

    def test_active_navigation_is_preserved_for_each_surface(self) -> None:
        for path, active in (("models/llama/index.html", "models"),
                             ("models/deploy/index.html", "deploy"),
                             ("models/pricing.html", "licensing")):
            with self.subTest(path=path):
                self.assertEqual(active_for(ROOT / path), active)
                text = synchronize(site_chrome() + site_footer(), active)
                header, _ = blocks(text)
                self.assertEqual(header.group(), site_chrome(active).split(
                    '<aside class="catalog-artwork-rail"', 1)[0].strip())


if __name__ == "__main__":
    unittest.main()
