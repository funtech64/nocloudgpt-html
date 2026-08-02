#!/usr/bin/env python3
"""
One-time / maintainer-only: build a pinned P4-Public-Catalog snapshot from Ollama library HTML.

NOT invoked by the site build. Run when refreshing the pinned input from a new 8-ball export
or when re-pinning from Ollama public library pages (not a live crawl at page-view time).

Preferred source: copy terminal-glass/8-ball/P4-Public-Catalog/ via scripts/catalog/update_pinned_input.sh
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "models" / "data" / "P4-Public-Catalog"
USER_AGENT = "NoCloudGPT-CatalogPin/1.0 (pinned snapshot; not page-view crawl)"

SOURCE_EXCEPTIONS = {
    "kimi-k2.5": {
        "type": "stale_source",
        "label": "Temporarily unavailable source metadata",
        "note": "Source catalog entry retained; not deleted.",
    },
    "minimax-m2.5": {
        "type": "stale_source",
        "label": "Temporarily unavailable source metadata",
        "note": "Source catalog entry retained; not deleted.",
    },
}

# Map Ollama library slugs to existing NoCloudGPT family folder slugs where they differ.
SITE_FAMILY_SLUG: dict[str, str] = {
    "llama3.1": "llama",
    "llama3.2": "llama",
    "llama3.3": "llama",
    "llama2": "llama",
    "llama4": "llama4",
    "gemma3": "gemma3",
    "gemma2": "gemma2",
    "gemma": "gemma",
    "qwen2.5": "qwen",
    "qwen3": "qwen3.5",
    "deepseek-r1": "deepseek-r1",
    "deepseek-coder": "deepseek-coder",
    "deepseek-v3": "deepseek",
    "deepseek-v3.1": "deepseek",
    "deepseek-v3.2": "deepseek",
}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", errors="replace")


def library_slugs() -> list[str]:
    html = fetch("https://ollama.com/library")
    slugs = set(re.findall(r"/library/([a-z0-9][a-z0-9._-]+)", html))
    # Ensure stale source-exception families are always pinned even if absent from library index HTML.
    slugs.update(SOURCE_EXCEPTIONS.keys())
    return sorted(slugs)


def parse_family_page(slug: str) -> dict:
    html = fetch(f"https://ollama.com/library/{slug}")
    title_m = re.search(r"<title>([^<]+)</title>", html)
    display = title_m.group(1).strip() if title_m else slug
    display = re.sub(r"\s*·\s*Ollama.*$", "", display, flags=re.I).strip() or slug

    run_cmds = sorted(set(re.findall(r"ollama run ([a-z0-9][a-z0-9._:-]+)", html)))
    if not run_cmds:
        run_cmds = [slug]

    caps = set()
    for cap in ("vision", "tools", "thinking", "embedding", "cloud"):
        if cap in html.lower():
            caps.add(cap)
    if "embed" in slug or "bge" in slug or "nomic" in slug:
        caps.add("embedding")
    if not caps:
        caps.add("text")

    ctx_m = re.search(r"(\d[\d,]*)\s*(?:token|context)", html, re.I)
    context_tokens = int(ctx_m.group(1).replace(",", "")) if ctx_m else None

    verified = "verified" in html.lower() or "meta" in slug or "google" in html.lower()

    tags: list[dict] = []
    for cmd in run_cmds:
        tag = cmd
        quant = None
        param_b = None
        if ":" in cmd:
            base, variant = cmd.split(":", 1)
            tag = cmd
            qm = re.search(r"q(\d+)", variant, re.I)
            if qm:
                quant = f"Q{qm.group(1)}"
            pm = re.search(r"(\d+(?:\.\d+)?)b", variant, re.I)
            if pm:
                param_b = float(pm.group(1))
        else:
            base = cmd
        tags.append(
            {
                "ollamaTag": tag,
                "baseName": base,
                "variant": tag.split(":", 1)[1] if ":" in tag else "latest",
                "parameterSizeB": param_b,
                "quantization": quant,
                "capabilities": sorted(caps),
                "hasCloudTag": "cloud" in tag or "cloud" in caps,
            }
        )

    return {
        "ollamaSlug": slug,
        "displayName": display,
        "capabilities": sorted(caps),
        "contextTokens": context_tokens,
        "publisherVerified": verified,
        "tags": tags,
    }


def canonical_slug_from_tag(tag: str) -> str:
    return tag.split(":")[0].lower()


def site_family_slug(ollama_slug: str) -> str:
    if ollama_slug in SITE_FAMILY_SLUG:
        return SITE_FAMILY_SLUG[ollama_slug]
    if ollama_slug.endswith("-cloud"):
        return ollama_slug
    return ollama_slug


def build_catalog(slugs: list[str]) -> None:
    families_raw: dict[str, dict] = {}
    models: list[dict] = []
    seen_canonical: set[str] = set()

    for i, slug in enumerate(slugs):
        try:
            parsed = parse_family_page(slug)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            print(f"skip {slug}: {exc}", file=sys.stderr)
            continue
        if i % 20 == 0:
            print(f"parsed {i}/{len(slugs)} …")
            time.sleep(0.2)

        site_slug = site_family_slug(slug)
        fam_key = site_slug
        if fam_key not in families_raw:
            families_raw[fam_key] = {
                "slug": site_slug,
                "displayName": parsed["displayName"],
                "ollamaFamilies": [],
                "aliases": [],
                "capabilities": set(),
                "publisherVerified": parsed["publisherVerified"],
                "modelSlugs": [],
                "sitePath": f"/models/{site_slug}/",
            }
        fam = families_raw[fam_key]
        fam["ollamaFamilies"].append(slug)
        fam["capabilities"].update(parsed["capabilities"])
        if slug != site_slug:
            fam["aliases"].append(slug)

        for t in parsed["tags"]:
            canonical = canonical_slug_from_tag(t["ollamaTag"])
            if canonical in seen_canonical:
                continue
            seen_canonical.add(canonical)

            avail = "available"
            source_exception = None
            seo_eligible = True
            noindex = False
            base_slug = slug.split(":")[0] if ":" in slug else slug
            if canonical in SOURCE_EXCEPTIONS or slug in SOURCE_EXCEPTIONS or base_slug in SOURCE_EXCEPTIONS:
                source_exception = (
                    SOURCE_EXCEPTIONS.get(canonical)
                    or SOURCE_EXCEPTIONS.get(slug)
                    or SOURCE_EXCEPTIONS.get(base_slug)
                )
                avail = "stale_source"
                seo_eligible = False
                noindex = True

            cloud_ok = t["hasCloudTag"] or "cloud" in parsed["capabilities"]
            local_ok = not canonical.endswith("-cloud") and avail == "available"

            model = {
                "canonicalSlug": canonical,
                "familySlug": site_slug,
                "displayName": t["baseName"],
                "ollamaTag": t["ollamaTag"],
                "aliases": [t["ollamaTag"]] if t["ollamaTag"] != canonical else [],
                "parameterSizeB": t["parameterSizeB"],
                "quantization": t["quantization"],
                "contextTokens": parsed["contextTokens"],
                "capabilities": t["capabilities"],
                "availability": avail,
                "localPrivateSuitable": local_ok,
                "cloudJetSuitable": cloud_ok,
                "seoEligible": seo_eligible,
                "noindex": noindex,
                "sourceException": source_exception,
                "deploymentVariants": [
                    {
                        "tag": t["ollamaTag"],
                        "mode": "cloud" if cloud_ok and "cloud" in t["ollamaTag"] else "local",
                        "label": t["variant"],
                    }
                ],
                "sitePath": f"/models/model/{canonical}/",
            }
            models.append(model)
            fam["modelSlugs"].append(canonical)

    families: list[dict] = []
    for fam in families_raw.values():
        fam["capabilities"] = sorted(fam["capabilities"])
        fam["aliases"] = sorted(set(fam["aliases"]))
        fam["modelCount"] = len(fam["modelSlugs"])
        fam["seoEligible"] = fam["modelCount"] > 0 and not all(
            m["canonicalSlug"] in SOURCE_EXCEPTIONS for m in models if m["familySlug"] == fam["slug"]
        )
        fam["availability"] = "available"
        if fam["slug"] in ("kimi-k2.5", "minimax-m2.5") or any(
            o in SOURCE_EXCEPTIONS for o in fam.get("ollamaFamilies", [])
        ):
            fam["availability"] = "stale_source"
            fam["seoEligible"] = True
        families.append(fam)

    families.sort(key=lambda f: f["slug"])
    models.sort(key=lambda m: m["canonicalSlug"])

    seo_families = [f["slug"] for f in families if f["seoEligible"]]
    seo_models = [m["canonicalSlug"] for m in models if m["seoEligible"]]
    noindex_models = [m["canonicalSlug"] for m in models if m.get("noindex")]

    manifest = {
        "schemaVersion": "p4-public-catalog/1.0",
        "projectionVersion": "4a.pin.2026-08-02",
        "sourceRepo": "terminal-glass/8-ball",
        "sourcePath": "P4-Public-Catalog",
        "pinnedFrom": "scripts/catalog/pin_snapshot.py (Ollama library HTML snapshot)",
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "counts": {
            "ollamaLibraryFamilies": len(slugs),
            "siteFamilies": len(families),
            "models": len(models),
            "seoEligibleFamilies": len(seo_families),
            "seoEligibleModels": len(seo_models),
            "noindexSourceExceptions": len(noindex_models),
        },
    }

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (OUT / "index").mkdir(exist_ok=True)
    (OUT / "index" / "families.json").write_text(json.dumps(families, indent=2) + "\n", encoding="utf-8")
    (OUT / "index" / "models.json").write_text(json.dumps(models, indent=2) + "\n", encoding="utf-8")

    browse = []
    for f in families:
        browse.append(
            {
                "type": "family",
                "slug": f["slug"],
                "name": f["displayName"],
                "capabilities": f["capabilities"],
                "availability": f["availability"],
                "seoEligible": f["seoEligible"],
                "path": f["sitePath"],
                "modelCount": f["modelCount"],
                "localPrivateSuitable": any(
                    m["localPrivateSuitable"] for m in models if m["familySlug"] == f["slug"]
                ),
                "cloudJetSuitable": any(
                    m["cloudJetSuitable"] for m in models if m["familySlug"] == f["slug"]
                ),
            }
        )
    for m in models:
        browse.append(
            {
                "type": "model",
                "slug": m["canonicalSlug"],
                "familySlug": m["familySlug"],
                "name": m["displayName"],
                "capabilities": m["capabilities"],
                "availability": m["availability"],
                "seoEligible": m["seoEligible"],
                "noindex": m.get("noindex", False),
                "path": m["sitePath"],
                "parameterSizeB": m["parameterSizeB"],
                "localPrivateSuitable": m["localPrivateSuitable"],
                "cloudJetSuitable": m["cloudJetSuitable"],
            }
        )
    (OUT / "index" / "browse.json").write_text(json.dumps(browse, indent=2) + "\n", encoding="utf-8")

    (OUT / "families").mkdir(exist_ok=True)
    for f in families:
        (OUT / "families" / f"{f['slug']}.json").write_text(json.dumps(f, indent=2) + "\n", encoding="utf-8")

    (OUT / "models").mkdir(exist_ok=True)
    for m in models:
        (OUT / "models" / f"{m['canonicalSlug']}.json").write_text(json.dumps(m, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(manifest["counts"], indent=2))


if __name__ == "__main__":
    slugs = library_slugs()
    print(f"library slugs: {len(slugs)}")
    build_catalog(slugs)
