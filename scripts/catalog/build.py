#!/usr/bin/env python3
"""Generate catalog browse data, model pages, and sitemap from pinned P4-Public-Catalog."""

from __future__ import annotations

import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import date
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "models" / "data" / "P4-Public-Catalog"
BROWSE_OUT = ROOT / "models" / "data" / "catalog-browse.json"
SITE = "https://nocloudgpt.com"
EDITORIAL_BASE = "119508b"

STATIC_SITEMAP_PATHS = [
    "/",
    "/services.html",
    "/software.html",
    "/pricing.html",
    "/contact.html",
    "/models/",
    "/models/pricing.html",
    "/models/quote.html",
    "/models/deploy/",
    "/models/deploy/index.html",
    "/models/deploy/lightsail-guide.html",
    "/models/deploy/on-premise.html",
    "/models/deploy/ollama-openwebui.html",
    "/models/compare/",
    "/models/compare/index.html",
    "/models/compare/llama-vs-mistral.html",
    "/models/compare/llama-vs-deepseek.html",
    "/models/compare/llama-vs-qwen.html",
    "/models/compare/local-vs-cloud-ai.html",
    "/models/chatgpt-alternatives/",
    "/models/chatgpt-alternatives/index.html",
]

SOURCE_EXCEPTION_IDS = frozenset({"kimi-k2.5", "minimax-m2.5"})


def normalize_html(html: str) -> str:
    return "\n".join(line.rstrip() for line in html.splitlines()) + "\n"


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def preserved_editorial_paths() -> set[str]:
    out = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", EDITORIAL_BASE, "models/"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    paths = set()
    for line in out.stdout.splitlines():
        if line.endswith("/index.html") and "/model/" not in line:
            if line == "models/index.html":
                continue  # catalog landing is generated, not editorial
            paths.add(line)
    return paths


def restore_editorial_pages(paths: set[str]) -> int:
    if not paths:
        return 0
    rel = sorted(paths)
    subprocess.run(
        ["git", "checkout", EDITORIAL_BASE, "--", *rel],
        cwd=ROOT,
        check=True,
    )
    return len(rel)


def nav_html() -> str:
    return """
  <div class="border-b border-slate-800 bg-slate-950/95">
    <div class="mx-auto flex max-w-7xl items-center justify-between px-6 py-3 text-sm">
      <a href="/" class="font-bold text-cyan-300 hover:text-cyan-200">NoCloudGPT</a>
      <nav class="flex flex-wrap gap-4 text-slate-400">
        <a href="/models/" class="text-white">Models</a>
        <a href="/models/deploy/" class="hover:text-white">Deploy</a>
        <a href="/services.html" class="hover:text-white">Services</a>
        <a href="/models/pricing.html" class="hover:text-white">Licensing</a>
        <a href="/contact.html" class="hover:text-white">Contact</a>
        <a href="https://terminal.glass/pricing/" class="hover:text-white" target="_blank" rel="noopener">terminal.glass pricing</a>
      </nav>
    </div>
  </div>"""


def footer_html() -> str:
    return """
  <footer class="border-t border-slate-800 bg-slate-950 px-6 py-10 text-center text-sm text-slate-500">
    <p>NoCloudGPT helps you select and deploy open models on infrastructure you control. terminal.glass does not sell model weights.</p>
    <p class="mt-2"><a href="/models/quote.html" class="text-cyan-400 hover:text-cyan-300">Plan deployment fit</a> · <a href="/models/deploy/index.html" class="text-cyan-400 hover:text-cyan-300">Deployment options</a></p>
  </footer>"""


def head_block(
    title: str,
    description: str,
    canonical: str,
    robots: str = "index, follow",
    json_ld: dict | None = None,
) -> str:
    ld = ""
    if json_ld:
        ld = f"\n  <script type=\"application/ld+json\">{json.dumps(json_ld)}</script>"
    return f"""  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{escape(canonical)}">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{escape(canonical)}">
  <script src="https://cdn.tailwindcss.com"></script>{ld}"""


def fmt_param_count(count: int | None) -> str:
    if count is None:
        return "—"
    if count >= 1_000_000_000:
        return f"{count / 1_000_000_000:g}B"
    if count >= 1_000_000:
        return f"{count / 1_000_000:g}M"
    return str(count)


def capability_list(cap_map: dict | None) -> list[str]:
    if not cap_map:
        return []
    return sorted(k for k, v in cap_map.items() if v == "true")


def variant_modes(variants: list[dict]) -> list[str]:
    modes = set()
    for v in variants:
        avail = v.get("availability") or ""
        if avail in ("local", "cloud", "both", "cloud_only"):
            modes.add(avail)
    return sorted(modes)


def deployment_cta(classifications: dict) -> str:
    parts = []
    if classifications.get("local_private_suitable"):
        parts.append(
            '<a href="/models/quote.html" class="rounded-xl bg-cyan-300 px-5 py-3 font-bold text-slate-950 hover:bg-cyan-200">Plan private deployment</a>'
        )
        parts.append(
            '<a href="/models/deploy/on-premise.html" class="rounded-xl border border-slate-700 px-5 py-3 font-bold text-white hover:bg-slate-900">On-premise guide</a>'
        )
    if classifications.get("cloud_jet_suitable"):
        parts.append(
            '<a href="https://terminal.glass/jet-agents/" class="rounded-xl border border-cyan-500/50 px-5 py-3 font-bold text-cyan-100 hover:bg-slate-900" target="_blank" rel="noopener">Jet Agents (cloud lane)</a>'
        )
    if not parts:
        parts.append(
            '<a href="/contact.html" class="rounded-xl border border-slate-700 px-5 py-3 font-bold text-white hover:bg-slate-900">Contact for availability</a>'
        )
    return "\n        ".join(parts)


def build_browse_index(families: list[dict], models: list[dict]) -> list[dict]:
    browse: list[dict] = []
    for f in families:
        cls = f.get("classifications") or {}
        include = f.get("source_status") != "stale_source_exception"
        browse.append(
            {
                "type": "family",
                "id": f["id"],
                "name": f.get("name") or f["id"],
                "aliases": f.get("aliases") or [],
                "source_status": f.get("source_status"),
                "capability_filters": cls.get("capability_filters") or [],
                "local_private_suitable": bool(cls.get("local_private_suitable")),
                "cloud_jet_suitable": bool(cls.get("cloud_jet_suitable")),
                "size_buckets": cls.get("size_buckets") or [],
                "quantizations": cls.get("quantizations") or [],
                "deployment_modes": [],
                "seo_eligible": bool((f.get("page") or {}).get("seo_eligible")),
                "include_in_search": include,
                "path": f"/models/{f['id']}/",
            }
        )
    for m in models:
        cls = m.get("classifications") or {}
        variants = m.get("deployment_variants") or []
        include = m.get("source_status") != "stale_source_exception"
        param_min = None
        for v in variants:
            pc = v.get("parameter_count")
            if isinstance(pc, int) and pc > 0:
                param_min = pc if param_min is None else min(param_min, pc)
        browse.append(
            {
                "type": "model",
                "id": m["id"],
                "family_id": m.get("family_id"),
                "name": m.get("display_name") or m["id"],
                "aliases": m.get("aliases") or [],
                "source_status": m.get("source_status"),
                "capability_filters": cls.get("capability_filters") or [],
                "local_private_suitable": bool(cls.get("local_private_suitable")),
                "cloud_jet_suitable": bool(cls.get("cloud_jet_suitable")),
                "size_buckets": cls.get("size_buckets") or [],
                "quantizations": cls.get("quantizations") or [],
                "deployment_modes": variant_modes(variants),
                "variant_count": len(variants),
                "parameter_count_min": param_min,
                "seo_eligible": bool((m.get("page") or {}).get("seo_eligible")),
                "include_in_search": include,
                "path": f"/models/model/{m['id']}/",
            }
        )
    return browse


def write_source_exception_family(family: dict) -> Path:
    slug = family["id"]
    out_dir = ROOT / "models" / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.html"
    explanation = family.get("source_exception_explanation") or "Retained catalog metadata; not deleted."
    title = f"{family.get('name', slug)} — source metadata retained | NoCloudGPT"
    desc = "Stale source exception record retained in the public catalog projection."
    canonical = f"{SITE}/models/{slug}/"
    html = f"""<!doctype html>
<html lang="en">
<head>
{head_block(title, desc, canonical, robots="noindex, follow")}
</head>
<body class="bg-slate-950 text-slate-100">
{nav_html()}
  <header class="border-b border-slate-800 bg-slate-950/90">
    <div class="mx-auto max-w-6xl px-6 py-12">
      <a href="/models/" class="text-sm font-semibold text-cyan-300 hover:text-cyan-200">← Model catalog</a>
      <p class="mt-6 text-sm font-bold uppercase tracking-[0.3em] text-amber-300">Stale source exception</p>
      <h1 class="mt-3 text-4xl font-black">{escape(family.get('name', slug))}</h1>
      <p class="mt-4 rounded-xl border border-amber-500/40 bg-amber-950/40 px-4 py-3 text-amber-100">{escape(explanation)}</p>
      <p class="mt-4 text-slate-400">This family record is retained in structured catalog data but excluded from search and sitemap.</p>
    </div>
  </header>
{footer_html()}
</body>
</html>
"""
    out_path.write_text(normalize_html(html), encoding="utf-8")
    return out_path


def write_catalog_family_page(family: dict, family_models: list[dict]) -> Path:
    slug = family["id"]
    out_dir = ROOT / "models" / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.html"
    cls = family.get("classifications") or {}
    caps = ", ".join(cls.get("capability_filters") or []) or "—"
    pub = (family.get("publisher") or {}).get("verification_status") or "unknown"
    rows = ""
    for m in family_models:
        mpath = f"/models/model/{m['id']}/"
        rows += f"""
        <tr class="border-t border-slate-800">
          <td class="py-3 pr-4"><a href="{escape(mpath)}" class="font-semibold text-cyan-300">{escape(m.get('display_name', m['id']))}</a></td>
          <td class="py-3 pr-4 text-slate-400">{len(m.get('deployment_variants') or [])} variants</td>
          <td class="py-3 text-sm text-slate-400">{escape(m.get('source_status', ''))}</td>
        </tr>"""
    title = f"{family.get('name', slug)} — Model family catalog | NoCloudGPT"
    desc = f"Catalog projection for {family.get('name', slug)}: {len(family_models)} canonical model(s)."
    canonical = f"{SITE}/models/{slug}/"
    html = f"""<!doctype html>
<html lang="en">
<head>
{head_block(title, desc, canonical)}
</head>
<body class="bg-slate-950 text-slate-100">
{nav_html()}
  <header class="border-b border-slate-800 bg-slate-950/90">
    <div class="mx-auto max-w-6xl px-6 py-12">
      <a href="/models/" class="text-sm font-semibold text-cyan-300 hover:text-cyan-200">← Model catalog</a>
      <h1 class="mt-6 text-4xl font-black">{escape(family.get('name', slug))}</h1>
      <p class="mt-4 text-slate-300">Factual catalog summary from pinned Phase 4A projection. Publisher verification: {escape(pub)}.</p>
      <p class="mt-2 text-slate-400">Capabilities: {escape(caps)}</p>
    </div>
  </header>
  <main class="mx-auto max-w-6xl px-6 py-12">
    <h2 class="text-2xl font-bold">Canonical models</h2>
    <table class="mt-6 w-full text-left text-sm">
      <thead class="text-slate-400"><tr><th class="pb-3">Model</th><th class="pb-3">Variants</th><th class="pb-3">Status</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </main>
{footer_html()}
</body>
</html>
"""
    out_path.write_text(normalize_html(html), encoding="utf-8")
    return out_path


def write_model_page(model: dict, family: dict) -> Path:
    slug = model["id"]
    out_dir = ROOT / "models" / "model" / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.html"
    cls = model.get("classifications") or {}
    seo = bool((model.get("page") or {}).get("seo_eligible"))
    robots = "index, follow" if seo else "noindex, follow"
    stale = ""
    if model.get("source_status") == "stale_source_exception":
        expl = model.get("source_exception_explanation") or family.get("source_exception_explanation") or ""
        stale = (
            f'<div class="mt-4 rounded-xl border border-amber-500/40 bg-amber-950/40 px-4 py-3 text-amber-100">'
            f"<strong>Stale source exception — retained, not deleted.</strong> {escape(expl)}</div>"
        )
    variant_rows = ""
    for v in model.get("deployment_variants") or []:
        variant_rows += f"""
        <tr class="border-t border-slate-800 text-sm">
          <td class="py-2 pr-3 font-mono text-cyan-200">{escape(v.get('ollama_identifier') or '')}</td>
          <td class="py-2 pr-3 text-slate-400">{escape(fmt_param_count(v.get('parameter_count')))}</td>
          <td class="py-2 pr-3 text-slate-400">{escape(v.get('quantization') or '—')}</td>
          <td class="py-2 pr-3 text-slate-400">{escape(str(v.get('context_window_tokens') or '—'))}</td>
          <td class="py-2 pr-3 text-slate-400">{escape(v.get('availability') or '—')}</td>
          <td class="py-2 text-slate-500 text-xs">{escape(v.get('pull_command') or '')}</td>
        </tr>"""
    caps = ", ".join(capability_list((model.get("deployment_variants") or [{}])[0].get("capabilities"))) if model.get("deployment_variants") else "—"
    title = f"{model.get('display_name', slug)} — Catalog model | NoCloudGPT"
    desc = f"Catalog model {slug} with {len(model.get('deployment_variants') or [])} deployment variants from pinned projection."
    canonical = f"{SITE}/models/model/{slug}/"
    json_ld = None
    if seo:
        json_ld = {
            "@context": "https://schema.org",
            "@type": "SoftwareApplication",
            "name": model.get("display_name", slug),
            "applicationCategory": "AI model",
            "description": desc,
            "url": canonical,
        }
    fam_slug = family.get("id", model.get("family_id", ""))
    html = f"""<!doctype html>
<html lang="en">
<head>
{head_block(title, desc, canonical, robots=robots, json_ld=json_ld)}
</head>
<body class="bg-slate-950 text-slate-100">
{nav_html()}
  <header class="border-b border-slate-800 bg-slate-950/90">
    <div class="mx-auto max-w-6xl px-6 py-12">
      <a href="/models/" class="text-sm font-semibold text-cyan-300 hover:text-cyan-200">← Model catalog</a>
      <a href="/models/{escape(fam_slug)}/" class="ml-4 text-sm text-slate-400 hover:text-white">{escape(family.get('name', fam_slug))}</a>
      <h1 class="mt-6 text-4xl font-black">{escape(model.get('display_name', slug))}</h1>
      <p class="mt-4 text-slate-300">Ollama name: <code class="text-cyan-200">{escape(model.get('ollama_name', ''))}</code></p>
      {stale}
      <div class="mt-8 flex flex-wrap gap-3">{deployment_cta(cls)}</div>
    </div>
  </header>
  <main class="mx-auto max-w-6xl px-6 py-12 space-y-8">
    <section>
      <h2 class="text-xl font-bold">Deployment variants ({len(model.get('deployment_variants') or [])})</h2>
      <p class="mt-2 text-sm text-slate-500">Variants are nested catalog data — not separate SEO pages.</p>
      <div class="mt-4 overflow-x-auto">
        <table class="w-full text-left text-sm">
          <thead class="text-slate-400">
            <tr>
              <th class="pb-2 pr-3">Tag</th>
              <th class="pb-2 pr-3">Params</th>
              <th class="pb-2 pr-3">Quant</th>
              <th class="pb-2 pr-3">Context</th>
              <th class="pb-2 pr-3">Availability</th>
              <th class="pb-2">Pull</th>
            </tr>
          </thead>
          <tbody>{variant_rows}</tbody>
        </table>
      </div>
    </section>
    <section class="text-sm text-slate-400">
      <p>Capability filters: {escape(', '.join(cls.get('capability_filters') or []) or '—')}</p>
      <p>Size buckets: {escape(', '.join(cls.get('size_buckets') or []) or '—')}</p>
    </section>
  </main>
{footer_html()}
</body>
</html>
"""
    out_path.write_text(normalize_html(html), encoding="utf-8")
    return out_path


def write_catalog_landing(manifest: dict) -> Path:
    counts = manifest.get("counts") or {}
    version = manifest.get("canonical_catalog_version") or manifest.get("schema_version")
    collection = manifest.get("collection_date") or ""
    out_path = ROOT / "models" / "index.html"
    title = "Private AI Model Catalog — Search & deploy with NoCloudGPT"
    desc = (
        f"Search {counts.get('families', 0)} families and {counts.get('models', 0)} canonical models "
        f"from pinned catalog {version}."
    )
    canonical = f"{SITE}/models/"
    html = f"""<!doctype html>
<html lang="en">
<head>
{head_block(title, desc, canonical)}
</head>
<body class="bg-slate-950 text-slate-100">
{nav_html()}
  <header class="border-b border-slate-800 bg-slate-950/90">
    <div class="mx-auto max-w-7xl px-6 py-10">
      <p class="text-sm font-semibold uppercase tracking-[0.3em] text-cyan-300">Catalog · pinned projection</p>
      <h1 class="mt-3 text-4xl font-bold tracking-tight md:text-5xl">Find a model, plan a deployment.</h1>
      <p class="mt-5 max-w-3xl text-lg text-slate-300">Search families, models, and aliases from the pinned Phase 4A public catalog. No live Ollama requests at page load.</p>
      <p class="mt-2 text-sm text-slate-500">Catalog {escape(str(version))} · collection {escape(collection)}</p>
    </div>
  </header>
  <main class="mx-auto max-w-7xl px-6 py-10">
    <section class="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <div class="flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
        <div class="flex-1">
          <label for="catalog-search" class="text-sm font-semibold text-slate-400">Search families, models, aliases</label>
          <input id="catalog-search" type="search" placeholder="Name, alias, capability…"
            class="mt-2 w-full rounded-xl border border-slate-700 bg-slate-950 px-4 py-3 text-white placeholder:text-slate-500 focus:border-cyan-400 focus:outline-none" autocomplete="off">
        </div>
        <button type="button" id="clear-filters" class="rounded-xl border border-slate-700 px-4 py-3 text-sm font-semibold text-slate-200 hover:bg-slate-800">Show all</button>
      </div>
      <div class="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <label class="text-sm text-slate-400">Availability
          <select id="filter-availability" class="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-1.5 text-sm">
            <option value="">Any</option>
            <option value="live">live</option>
            <option value="stale_source_exception">stale source exception</option>
          </select>
        </label>
        <label class="text-sm text-slate-400">Local / private
          <select id="filter-local" class="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-1.5 text-sm">
            <option value="">Any</option>
            <option value="yes">Suitable</option>
          </select>
        </label>
        <label class="text-sm text-slate-400">Cloud / Jet
          <select id="filter-cloud" class="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-1.5 text-sm">
            <option value="">Any</option>
            <option value="yes">Supported</option>
          </select>
        </label>
        <label class="text-sm text-slate-400">Capability
          <select id="filter-capability" class="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-1.5 text-sm">
            <option value="">Any</option>
            <option value="text_generation">text_generation</option>
            <option value="coding">coding</option>
            <option value="reasoning">reasoning</option>
            <option value="vision">vision</option>
            <option value="embeddings">embeddings</option>
            <option value="tool_use">tool_use</option>
            <option value="multilingual">multilingual</option>
            <option value="cloud">cloud</option>
          </select>
        </label>
        <label class="text-sm text-slate-400">Size bucket
          <select id="filter-size" class="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-1.5 text-sm">
            <option value="">Any</option>
            <option value="micro">micro</option>
            <option value="small">small</option>
            <option value="medium">medium</option>
            <option value="large">large</option>
            <option value="xlarge">xlarge</option>
          </select>
        </label>
        <label class="text-sm text-slate-400">Quantization
          <select id="filter-quant" class="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-1.5 text-sm">
            <option value="">Any</option>
            <option value="q4_0">q4_0</option>
            <option value="q4_1">q4_1</option>
            <option value="q5_0">q5_0</option>
            <option value="q5_1">q5_1</option>
            <option value="q8_0">q8_0</option>
            <option value="q2_K">q2_K</option>
            <option value="q3_K_S">q3_K_S</option>
            <option value="q4_K_M">q4_K_M</option>
            <option value="q5_K_M">q5_K_M</option>
            <option value="q6_K">q6_K</option>
            <option value="q8_0">q8_0</option>
          </select>
        </label>
        <label class="text-sm text-slate-400">Deployment mode
          <select id="filter-deployment" class="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-1.5 text-sm">
            <option value="">Any</option>
            <option value="local">local</option>
            <option value="cloud">cloud</option>
            <option value="both">both</option>
            <option value="cloud_only">cloud_only</option>
          </select>
        </label>
        <label class="text-sm text-slate-400">Min params (B)
          <input id="filter-params" type="number" min="0" step="0.5" placeholder="e.g. 7"
            class="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-1.5 text-sm">
        </label>
      </div>
      <p id="result-count" class="mt-4 text-sm text-slate-400"></p>
      <div id="empty-state" class="mt-8 hidden rounded-xl border border-dashed border-slate-700 p-8 text-center text-slate-400">
        <p>No matches. <button type="button" class="text-cyan-300 underline" id="empty-reset">Reset filters</button></p>
      </div>
      <div id="results" class="mt-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-3"></div>
    </section>
    <p class="mt-8 text-sm text-slate-500">{counts.get('seo_eligible_family_pages', 0)} SEO family pages · {counts.get('seo_eligible_model_pages', 0)} SEO model pages · {counts.get('deployment_variants', 0)} deployment variants in data</p>
  </main>
{footer_html()}
  <script>
    const BROWSE = fetch('/models/data/catalog-browse.json').then(r => r.json());
    BROWSE.then(items => {{
      const resultsEl = document.getElementById('results');
      const emptyEl = document.getElementById('empty-state');
      const countEl = document.getElementById('result-count');

      function card(item) {{
        const type = item.type === 'family' ? 'Family' : 'Model';
        const badges = [];
        if (item.local_private_suitable) badges.push('<span class="text-emerald-400">local</span>');
        if (item.cloud_jet_suitable) badges.push('<span class="text-cyan-300">cloud</span>');
        if (item.source_status === 'stale_source_exception') badges.push('<span class="text-amber-300">stale</span>');
        return `<a href="${{item.path}}" class="rounded-xl border border-slate-800 bg-slate-950 p-4 hover:border-cyan-500/50 block">
          <div class="text-xs uppercase tracking-wider text-slate-500">${{type}}</div>
          <div class="mt-1 font-bold text-white">${{item.name}}</div>
          <div class="mt-2 text-xs text-slate-400">${{(item.capability_filters || []).join(', ')}}</div>
          <div class="mt-2 text-xs flex gap-2">${{badges.join(' ')}}</div>
        </a>`;
      }}

      function applyFilters() {{
        const q = document.getElementById('catalog-search').value.trim().toLowerCase();
        const avail = document.getElementById('filter-availability').value;
        const local = document.getElementById('filter-local').value;
        const cloud = document.getElementById('filter-cloud').value;
        const cap = document.getElementById('filter-capability').value;
        const size = document.getElementById('filter-size').value;
        const quant = document.getElementById('filter-quant').value;
        const deploy = document.getElementById('filter-deployment').value;
        const minB = parseFloat(document.getElementById('filter-params').value) || 0;

        let filtered = items.filter(item => {{
          if (!item.include_in_search) return false;
          if (avail && item.source_status !== avail) return false;
          if (local === 'yes' && !item.local_private_suitable) return false;
          if (cloud === 'yes' && !item.cloud_jet_suitable) return false;
          if (cap && !(item.capability_filters || []).includes(cap)) return false;
          if (size && !(item.size_buckets || []).includes(size)) return false;
          if (quant && !(item.quantizations || []).includes(quant)) return false;
          if (deploy && !(item.deployment_modes || []).includes(deploy)) return false;
          if (minB && item.parameter_count_min) {{
            const b = item.parameter_count_min / 1e9;
            if (b < minB) return false;
          }}
          if (q) {{
            const hay = [item.name, item.id, item.family_id, (item.aliases || []).join(' '), (item.capability_filters || []).join(' ')].join(' ').toLowerCase();
            if (!hay.includes(q)) return false;
          }}
          return true;
        }});

        filtered.sort((a, b) => (a.type === 'family' ? 0 : 1) - (b.type === 'family' ? 0 : 1) || a.name.localeCompare(b.name));
        const display = filtered.slice(0, 60);
        countEl.textContent = `${{filtered.length}} match(es) — showing ${{display.length}}`;
        resultsEl.innerHTML = display.map(card).join('');
        emptyEl.classList.toggle('hidden', filtered.length > 0);
      }}

      ['catalog-search','filter-availability','filter-local','filter-cloud','filter-capability','filter-size','filter-quant','filter-deployment','filter-params'].forEach(id => {{
        const el = document.getElementById(id);
        el.addEventListener('input', applyFilters);
        el.addEventListener('change', applyFilters);
      }});
      document.getElementById('clear-filters').onclick = () => {{
        document.getElementById('catalog-search').value = '';
        ['filter-availability','filter-local','filter-cloud','filter-capability','filter-size','filter-quant','filter-deployment'].forEach(id => document.getElementById(id).value = '');
        document.getElementById('filter-params').value = '';
        applyFilters();
      }};
      document.getElementById('empty-reset').onclick = () => document.getElementById('clear-filters').click();
      applyFilters();
    }});
  </script>
</body>
</html>
"""
    out_path.write_text(normalize_html(html), encoding="utf-8")
    return out_path


def write_sitemap(
    manifest: dict,
    families: list[dict],
    models: list[dict],
    preserved_paths: set[str],
) -> Path:
    today = date.today().isoformat()
    urls: set[str] = set()

    for p in STATIC_SITEMAP_PATHS:
        urls.add(f"{SITE}{p if p.startswith('/') else '/' + p}")

    for rel in preserved_paths:
        if rel.endswith("/index.html"):
            slug = rel.replace("models/", "").replace("/index.html", "")
            urls.add(f"{SITE}/models/{slug}/")

    for f in families:
        if (f.get("page") or {}).get("seo_eligible"):
            urls.add(f"{SITE}/models/{f['id']}/")

    for m in models:
        if (m.get("page") or {}).get("seo_eligible"):
            urls.add(f"{SITE}/models/model/{m['id']}/")

    alt_dir = ROOT / "models" / "chatgpt-alternatives"
    if alt_dir.is_dir():
        for child in sorted(alt_dir.iterdir()):
            if child.is_dir() and (child / "index.html").is_file():
                urls.add(f"{SITE}/models/chatgpt-alternatives/{child.name}/")

    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for loc in sorted(urls):
        url_el = ET.SubElement(urlset, "url")
        ET.SubElement(url_el, "loc").text = loc
        ET.SubElement(url_el, "lastmod").text = today

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    out = ROOT / "sitemap.xml"
    tree.write(out, encoding="utf-8", xml_declaration=True)
    return out


def cleanup_stale_model_pages(valid_ids: set[str]) -> None:
    model_root = ROOT / "models" / "model"
    if not model_root.is_dir():
        return
    for child in model_root.iterdir():
        if child.is_dir() and child.name not in valid_ids:
            for f in child.rglob("*"):
                if f.is_file():
                    f.unlink()
            for d in sorted(child.rglob("*"), reverse=True):
                if d.is_dir():
                    d.rmdir()
            try:
                child.rmdir()
            except OSError:
                pass


def main() -> int:
    if not CATALOG.is_dir():
        print(f"Missing pinned catalog: {CATALOG}", file=sys.stderr)
        return 1

    manifest = load_json(CATALOG / "manifest.json")
    families = load_json(CATALOG / "index" / "families.json")
    models = load_json(CATALOG / "index" / "models.json")

    preserved = preserved_editorial_paths()
    restored = restore_editorial_pages(preserved)

    family_by_id = {f["id"]: f for f in families}
    models_by_family: dict[str, list[dict]] = {}
    for m in models:
        models_by_family.setdefault(m.get("family_id", ""), []).append(m)

    browse = build_browse_index(families, models)
    BROWSE_OUT.write_text(json.dumps(browse, indent=2) + "\n", encoding="utf-8")

    exception_family_pages = []
    catalog_family_pages = []
    model_pages = []

    for f in families:
        rel = f"models/{f['id']}/index.html"
        if f.get("source_status") == "stale_source_exception":
            exception_family_pages.append(write_source_exception_family(f))
        elif (f.get("page") or {}).get("seo_eligible") and rel not in preserved:
            catalog_family_pages.append(
                write_catalog_family_page(f, models_by_family.get(f["id"], []))
            )

    for m in models:
        fam = family_by_id.get(m.get("family_id", ""), {"id": m.get("family_id", ""), "name": m.get("family_id", "")})
        model_pages.append(write_model_page(m, fam))

    cleanup_stale_model_pages({m["id"] for m in models})

    landing = write_catalog_landing(manifest)
    sitemap = write_sitemap(manifest, families, models, preserved)

    summary = {
        "restoredEditorialPages": restored,
        "exceptionFamilyPages": len(exception_family_pages),
        "catalogFamilyPages": len(catalog_family_pages),
        "modelPages": len(model_pages),
        "browseEntries": len(browse),
        "manifest": manifest.get("canonical_catalog_version"),
        "counts": manifest.get("counts"),
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
