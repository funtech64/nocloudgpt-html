#!/usr/bin/env python3
"""Stage 1 static smoke tests for NoCloudGPT's public HTML and storefront parity.

No network requests or third-party dependencies are required. These tests
deliberately target the marketing shell and catalog generator, not the
editorial content of hundreds of individual model-family pages.
"""

from __future__ import annotations

import re
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
MARKETING = ("index.html", "software.html", "services.html", "contact.html", "pricing.html")
CATALOG_LANDING = "models/index.html"
STORE = "https://shop.nocloudgpt.com"
MARKETING_SITE = "https://colorschat.com"


class Markup(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hrefs: list[str] = []
        self.images_without_alt: list[str] = []
        self.external_target_links_without_noopener: list[str] = []
        self.ids: set[str] = set()
        self.duplicate_ids: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        if "id" in attr and attr["id"]:
            name = attr["id"]
            if name in self.ids:
                self.duplicate_ids.append(name)
            self.ids.add(name)
        if tag == "img" and "alt" not in attr:
            self.images_without_alt.append(attr.get("src") or "(missing src)")
        if tag == "a":
            href = attr.get("href")
            if href:
                self.hrefs.append(href)
            if attr.get("target") == "_blank" and "noopener" not in (attr.get("rel") or "").split():
                self.external_target_links_without_noopener.append(href or "(empty href)")


def html(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def markup(path: str) -> Markup:
    parser = Markup()
    parser.feed(html(path))
    parser.close()
    return parser


def resolve_local(href: str) -> Path | None:
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or not href.startswith("/"):
        return None
    path = unquote(parsed.path).lstrip("/")
    if ".." in Path(path).parts:
        raise ValueError(f"Unexpected parent traversal in {href!r}")
    local = ROOT / path
    if href.endswith("/") or not path:
        local = local / "index.html"
    return local


class PublicWebsiteStage1Tests(unittest.TestCase):
    def test_marketing_pages_exist_and_use_connected_store(self) -> None:
        for page in MARKETING:
            with self.subTest(page=page):
                text = html(page)
                self.assertIn(f'href="{STORE}"', text)
                self.assertIn(f'href="{MARKETING_SITE}"', text)
                self.assertNotIn('href="https://colors.chat"', text)
                self.assertNotIn("colorschat.com · YouTube", text)
                self.assertIn("</html>", text)
                self.assertIn('href="/styles.css"', text)
                self.assertIn('class="spectrum-mark"', text)

    def test_navigation_and_local_assets_resolve(self) -> None:
        for page in (*MARKETING, CATALOG_LANDING):
            with self.subTest(page=page):
                p = markup(page)
                self.assertFalse(p.images_without_alt, p.images_without_alt)
                self.assertFalse(p.duplicate_ids, p.duplicate_ids)
                self.assertFalse(p.external_target_links_without_noopener, p.external_target_links_without_noopener)
                for href in p.hrefs:
                    local = resolve_local(href)
                    if local is not None:
                        self.assertTrue(local.is_file(), f"{page}: broken internal link {href} -> {local}")

    def test_homepage_uses_shop_hero_and_preserves_software_art(self) -> None:
        home = html("index.html")
        self.assertIn("https://cdn.shopify.com/s/files/1/0601/5447/8674/files/IMG_1117.png", home)
        self.assertIn("/brand/colors-chat-workspace.jpg", home)
        self.assertIn("fetchpriority=\"high\"", home)
        self.assertTrue((ROOT / "brand" / "colors-chat-workspace.jpg").is_file())
        self.assertTrue((ROOT / "brand" / "brand-mark.svg").is_file())

    def test_shared_horizon_shell_retains_spectrum(self) -> None:
        css = html("styles.css")
        chrome = html("brand/chrome.css")
        self.assertIn("--ink: #000000;", css)
        self.assertIn("--bg: #ffffff;", css)
        self.assertIn("--line: #DFDFDF;", css)
        self.assertIn("font-family: Inter", css)
        self.assertIn("@media (max-width: 980px)", css)
        for color in ("#06B6D4", "#0D9488", "#F59E0B"):
            self.assertIn(color, css)
            self.assertIn(color, chrome)
        self.assertIn("background: #000000", chrome)

    def test_catalog_landing_and_generator_have_new_storefront_chrome(self) -> None:
        landing = html(CATALOG_LANDING)
        generated = html("scripts/catalog/chrome.py")
        for name, source in (("landing", landing), ("generator", generated)):
            with self.subTest(name=name):
                self.assertIn(STORE, source)
                self.assertNotIn('href="https://colors.chat"', source)
                self.assertNotIn("colorschat.com · YouTube", source)
                self.assertIn("data-spectrum-chrome", source)
                self.assertIn("colors-chat-workspace.jpg", source)
        self.assertIn('id="catalog-search"', landing)

    def test_static_urls_present_in_sitemap(self) -> None:
        root = ET.parse(ROOT / "sitemap.xml").getroot()
        urls = {node.text for node in root.findall(".//{*}loc")}
        for path in ("/", "/software.html", "/services.html", "/contact.html", "/pricing.html", "/models/"):
            with self.subTest(path=path):
                self.assertIn("https://nocloudgpt.com" + path, urls)


if __name__ == "__main__":
    unittest.main()
