#!/usr/bin/env python3
"""Tests for Phase 4B catalog build against authoritative P4 projection."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "models" / "data" / "P4-Public-Catalog"
BROWSE = ROOT / "models" / "data" / "catalog-browse.json"
BUILD = ROOT / "scripts" / "catalog" / "build.py"
EDITORIAL_BASE = "119508b"

AUTHORITATIVE_COUNTS = {
    "families": 234,
    "models": 437,
    "deployment_variants": 7271,
    "seo_eligible_family_pages": 232,
    "seo_eligible_model_pages": 435,
    "non_indexable_source_exception_families": 2,
}

SOURCE_EXCEPTIONS = frozenset({"kimi-k2.5", "minimax-m2.5"})


def git_show(path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{EDITORIAL_BASE}:{path}"], cwd=ROOT)


def variant_total(models: list[dict]) -> int:
    return sum(len(m.get("deployment_variants") or []) for m in models)


class CatalogBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, check=True)

    def test_authoritative_manifest_counts(self) -> None:
        manifest = json.loads((CATALOG / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["schema_version"], "1.0.0")
        self.assertEqual(manifest["canonical_catalog_version"], "2026.08.01")
        self.assertEqual(manifest["collection_date"], "2026-08-01")
        self.assertIn("source_provenance", manifest)
        self.assertIn("source_commit", manifest["source_provenance"])
        self.assertIn("promotion_receipt", manifest)
        self.assertIn("generator_command", manifest)
        counts = manifest["counts"]
        for key, expected in AUTHORITATIVE_COUNTS.items():
            self.assertEqual(counts[key], expected, key)

    def test_all_deployment_variants_preserved(self) -> None:
        models = json.loads((CATALOG / "index" / "models.json").read_text(encoding="utf-8"))
        self.assertEqual(variant_total(models), AUTHORITATIVE_COUNTS["deployment_variants"])
        multi = [m for m in models if len(m.get("deployment_variants") or []) > 1]
        self.assertGreater(len(multi), 50)

    def test_source_exception_family_and_model_noindex(self) -> None:
        families = json.loads((CATALOG / "index" / "families.json").read_text(encoding="utf-8"))
        models = json.loads((CATALOG / "index" / "models.json").read_text(encoding="utf-8"))
        exc_fams = [f for f in families if f.get("source_status") == "stale_source_exception"]
        self.assertEqual(len(exc_fams), 2)
        exc_fam_ids = {f["id"] for f in exc_fams}
        self.assertEqual(exc_fam_ids, SOURCE_EXCEPTIONS)

        for slug in SOURCE_EXCEPTIONS:
            fam_html = (ROOT / "models" / slug / "index.html").read_text(encoding="utf-8")
            self.assertIn("noindex", fam_html)
            self.assertIn("retained", fam_html.lower())

            model = next(m for m in models if m["id"] == slug)
            model_html = (ROOT / "models" / "model" / slug / "index.html").read_text(encoding="utf-8")
            self.assertIn("noindex", model_html)
            self.assertIn("Stale source exception", model_html)

    def test_source_exceptions_absent_from_sitemap_and_search(self) -> None:
        sitemap = ET.parse(ROOT / "sitemap.xml")
        locs = {el.text for el in sitemap.findall(".//{*}loc")}
        for slug in SOURCE_EXCEPTIONS:
            self.assertNotIn(f"https://nocloudgpt.com/models/{slug}/", locs)
            self.assertNotIn(f"https://nocloudgpt.com/models/model/{slug}/", locs)

        browse = json.loads(BROWSE.read_text(encoding="utf-8"))
        searchable = [b for b in browse if b.get("include_in_search")]
        ids = {b["id"] for b in searchable}
        for slug in SOURCE_EXCEPTIONS:
            self.assertNotIn(slug, ids)

    def test_aliases_searchable_in_browse(self) -> None:
        browse = json.loads(BROWSE.read_text(encoding="utf-8"))
        self.assertTrue(any("capability_filters" in b for b in browse))
        self.assertTrue(any("deployment_modes" in b for b in browse))
        self.assertTrue(any("parameter_count_min" in b for b in browse))
        # dolphin-mistral has aliases in catalog — spot check if present
        models = json.loads((CATALOG / "index" / "models.json").read_text(encoding="utf-8"))
        with_alias = next((m for m in models if m.get("aliases")), None)
        if with_alias:
            entry = next(b for b in browse if b["id"] == with_alias["id"])
            self.assertEqual(entry.get("aliases"), with_alias.get("aliases"))

    def test_browse_filter_fields_present(self) -> None:
        browse = json.loads(BROWSE.read_text(encoding="utf-8"))
        sample = browse[0]
        for field in (
            "capability_filters",
            "local_private_suitable",
            "cloud_jet_suitable",
            "size_buckets",
            "quantizations",
            "source_status",
            "include_in_search",
        ):
            self.assertIn(field, sample)

    def test_editorial_pages_preserved(self) -> None:
        preserved_path = "models/all-minilm/index.html"
        current = (ROOT / preserved_path).read_bytes()
        original = git_show(preserved_path)
        self.assertEqual(current, original)
        # spot-check llama flagship page
        llama_current = (ROOT / "models/llama/index.html").read_bytes()
        llama_original = git_show("models/llama/index.html")
        self.assertEqual(llama_current, llama_original)

    def test_preserved_page_count(self) -> None:
        out = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", EDITORIAL_BASE, "models/"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        preserved = [
            p
            for p in out.stdout.splitlines()
            if p.endswith("/index.html") and "/model/" not in p and p != "models/index.html"
        ]
        self.assertGreaterEqual(len(preserved), 165)
        for rel in preserved:
            current = (ROOT / rel).read_bytes()
            original = git_show(rel)
            self.assertEqual(current, original, rel)

    def test_no_deployment_variant_seo_pages(self) -> None:
        for path in (ROOT / "models" / "model").iterdir():
            if path.is_dir() and ":" in path.name:
                self.fail(f"variant route leaked: {path.name}")

    def test_build_is_deterministic(self) -> None:
        landing = (ROOT / "models" / "index.html").read_text(encoding="utf-8")
        browse = BROWSE.read_text(encoding="utf-8")
        subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, check=True)
        self.assertEqual(landing, (ROOT / "models" / "index.html").read_text(encoding="utf-8"))
        self.assertEqual(browse, BROWSE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
