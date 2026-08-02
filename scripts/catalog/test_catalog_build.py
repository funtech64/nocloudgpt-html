#!/usr/bin/env python3
"""Tests for pinned P4 catalog and catalog site build."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "models" / "data" / "P4-Public-Catalog"
BUILD = ROOT / "scripts" / "catalog" / "build.py"
PIN = ROOT / "scripts" / "catalog" / "pin_snapshot.py"


class CatalogBuildTests(unittest.TestCase):
    def test_pinned_manifest_present(self) -> None:
        manifest = json.loads((CATALOG / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["schemaVersion"], "p4-public-catalog/1.0")
        self.assertIn("projectionVersion", manifest)
        self.assertGreater(manifest["counts"]["models"], 200)

    def test_build_is_deterministic(self) -> None:
        r1 = subprocess.run([sys.executable, str(BUILD)], capture_output=True, text=True, check=True)
        landing = (ROOT / "models" / "index.html").read_text(encoding="utf-8")
        r2 = subprocess.run([sys.executable, str(BUILD)], capture_output=True, text=True, check=True)
        self.assertEqual(landing, (ROOT / "models" / "index.html").read_text(encoding="utf-8"))
        self.assertIn("familyPages", r1.stdout)

    def test_no_thousands_of_model_pages(self) -> None:
        model_pages = list((ROOT / "models" / "model").glob("*/index.html"))
        self.assertLess(len(model_pages), 500)
        self.assertGreater(len(model_pages), 100)

    def test_source_exceptions_noindex_not_in_sitemap(self) -> None:
        models = json.loads((CATALOG / "index" / "models.json").read_text(encoding="utf-8"))
        exceptions = [m for m in models if m.get("noindex")]
        self.assertEqual(len(exceptions), 2)
        slugs = {m["canonicalSlug"] for m in exceptions}
        self.assertIn("kimi-k2.5", slugs)
        self.assertIn("minimax-m2.5", slugs)

        sitemap = ET.parse(ROOT / "sitemap.xml")
        locs = {el.text for el in sitemap.findall(".//{*}loc")}
        for m in exceptions:
            self.assertNotIn(f"https://nocloudgpt.com/models/model/{m['canonicalSlug']}/", locs)

        for slug in ("kimi-k2.5", "minimax-m2.5"):
            page = ROOT / "models" / "model" / slug / "index.html"
            self.assertTrue(page.is_file())
            self.assertIn("noindex", page.read_text(encoding="utf-8"))
            self.assertIn("Temporarily unavailable", page.read_text(encoding="utf-8"))

    def test_seo_eligible_in_sitemap(self) -> None:
        families = json.loads((CATALOG / "index" / "families.json").read_text(encoding="utf-8"))
        models = json.loads((CATALOG / "index" / "models.json").read_text(encoding="utf-8"))
        sitemap = ET.parse(ROOT / "sitemap.xml")
        locs = {el.text for el in sitemap.findall(".//{*}loc")}

        sample_family = next(f for f in families if f.get("seoEligible"))
        self.assertIn(f"https://nocloudgpt.com/models/{sample_family['slug']}/", locs)

        sample_model = next(m for m in models if m.get("seoEligible") and not m.get("noindex"))
        self.assertIn(
            f"https://nocloudgpt.com/models/model/{sample_model['canonicalSlug']}/",
            locs,
        )

    def test_catalog_landing_has_search(self) -> None:
        html = (ROOT / "models" / "index.html").read_text(encoding="utf-8")
        self.assertIn("catalog-search", html)
        self.assertIn("filter-availability", html)
        self.assertIn("catalog-browse-data", html)

    def test_no_deployment_variant_seo_pages(self) -> None:
        # Deployment variant tags should not become separate /models/model/ routes.
        for path in (ROOT / "models" / "model").iterdir():
            if path.is_dir() and ":" in path.name:
                self.fail(f"unexpected variant route: {path.name}")


if __name__ == "__main__":
    unittest.main()
