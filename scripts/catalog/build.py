#!/usr/bin/env python3
"""Generate catalog HTML pages and sitemap from pinned P4-Public-Catalog."""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from datetime import date
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "models" / "data" / "P4-Public-Catalog"
SITE = "https://nocloudgpt.com"
TEMPLATES = Path(__file__).resolve().parent / "templates"

# Static site paths always included in sitemap (not generated).
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


def normalize_html(html: str) -> str:
    return "\n".join(line.rstrip() for line in html.splitlines()) + "\n"


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


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


def fmt_param(b: float | None) -> str:
    if b is None:
        return "—"
    if b >= 1:
        return f"{b:g}B"
    return f"{b}B"


def deployment_cta(model: dict) -> str:
    parts = []
    if model.get("localPrivateSuitable") and model.get("availability") == "available":
        parts.append(
            '<a href="/models/quote.html" class="rounded-xl bg-cyan-300 px-5 py-3 font-bold text-slate-950 hover:bg-cyan-200">Plan private deployment</a>'
        )
        parts.append(
            '<a href="/models/deploy/on-premise.html" class="rounded-xl border border-slate-700 px-5 py-3 font-bold text-white hover:bg-slate-900">On-premise guide</a>'
        )
    if model.get("cloudJetSuitable"):
        parts.append(
            '<a href="https://terminal.glass/jet-agents/" class="rounded-xl border border-cyan-500/50 px-5 py-3 font-bold text-cyan-100 hover:bg-slate-900" target="_blank" rel="noopener">Jet Agents (cloud lane)</a>'
        )
    if not parts:
        parts.append(
            '<a href="/contact.html" class="rounded-xl border border-slate-700 px-5 py-3 font-bold text-white hover:bg-slate-900">Contact for availability</a>'
        )
    return "\n        ".join(parts)


# Families with dedicated Terminal Glass cloud marketing pages — do not overwrite with catalog template.
PRESERVE_FAMILY_PAGES = frozenset(
    {p.name for p in (ROOT / "models").iterdir() if p.is_dir() and p.name.endswith("-cloud")}
)


def write_family_page(family: dict, models: list[dict]) -> Path | None:
    slug = family["slug"]
    if slug in PRESERVE_FAMILY_PAGES:
        return None
    out_dir = ROOT / "models" / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.html"

    fam_models = [m for m in models if m["familySlug"] == slug]
    verified = "verified publisher" if family.get("publisherVerified") else "unverified publisher metadata"
    caps = ", ".join(family.get("capabilities") or []) or "text"
    stale_banner = ""
    if family.get("availability") == "stale_source":
        stale_banner = (
            '<p class="mt-4 rounded-xl border border-amber-500/40 bg-amber-950/40 px-4 py-3 text-amber-100">'
            "Some source metadata for this family is temporarily unavailable in the upstream catalog. "
            "Entries are retained, not deleted.</p>"
        )

    model_rows = ""
    for m in fam_models:
        avail = m["availability"]
        if avail == "stale_source":
            badge = '<span class="text-amber-300">stale source</span>'
        elif avail == "available":
            badge = '<span class="text-emerald-400">available</span>'
        else:
            badge = escape(avail)
        model_rows += f"""
        <tr class="border-t border-slate-800">
          <td class="py-3 pr-4"><a href="{escape(m['sitePath'])}" class="font-semibold text-cyan-300 hover:text-cyan-200">{escape(m['displayName'])}</a></td>
          <td class="py-3 pr-4 text-slate-400">{fmt_param(m.get('parameterSizeB'))}</td>
          <td class="py-3 pr-4 text-slate-400">{escape(m.get('quantization') or '—')}</td>
          <td class="py-3 pr-4 text-slate-400">{escape(', '.join(m.get('capabilities') or []))}</td>
          <td class="py-3 text-sm">{badge}</td>
        </tr>"""

    title = f"{family['displayName']} — Model family catalog | NoCloudGPT"
    desc = (
        f"Catalog facts for {family['displayName']}: capabilities ({caps}), "
        f"{len(fam_models)} catalog model(s), deployment variants. terminal.glass helps deploy; weights are not sold here."
    )
    canonical = f"{SITE}/models/{slug}/"
    json_ld = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": family["displayName"],
        "description": desc,
        "url": canonical,
    }

    html = f"""<!doctype html>
<html lang="en">
<head>
{head_block(title, desc, canonical, json_ld=json_ld)}
</head>
<body class="bg-slate-950 text-slate-100">
{nav_html()}
  <header class="border-b border-slate-800 bg-slate-950/90">
    <div class="mx-auto max-w-6xl px-6 py-12">
      <a href="/models/" class="text-sm font-semibold text-cyan-300 hover:text-cyan-200">← Back to model catalog</a>
      <p class="mt-6 text-sm font-bold uppercase tracking-[0.3em] text-cyan-300">{escape(family['displayName'])}</p>
      <h1 class="mt-3 text-4xl font-black tracking-tight md:text-5xl">{escape(family['displayName'])} family</h1>
      <p class="mt-4 max-w-3xl text-lg text-slate-300">Factual catalog summary from the pinned public projection. Publisher status: {verified}.</p>
      {stale_banner}
      <p class="mt-4 text-slate-400">Capabilities: {escape(caps)}. Ollama families: {escape(', '.join(family.get('ollamaFamilies') or []))}.</p>
    </div>
  </header>
  <main class="mx-auto max-w-6xl px-6 py-12">
    <section>
      <h2 class="text-2xl font-bold">Models in this family</h2>
      <table class="mt-6 w-full text-left text-sm">
        <thead class="text-slate-400">
          <tr>
            <th class="pb-3">Model</th>
            <th class="pb-3">Params</th>
            <th class="pb-3">Quant</th>
            <th class="pb-3">Capabilities</th>
            <th class="pb-3">Availability</th>
          </tr>
        </thead>
        <tbody>{model_rows}
        </tbody>
      </table>
    </section>
  </main>
{footer_html()}
</body>
</html>
"""
    out_path.write_text(normalize_html(html), encoding="utf-8")
    return out_path


def write_model_page(model: dict, family: dict) -> Path:
    slug = model["canonicalSlug"]
    out_dir = ROOT / "models" / "model" / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.html"

    robots = "noindex, follow" if model.get("noindex") else "index, follow"
    stale = ""
    if model.get("sourceException"):
        ex = model["sourceException"]
        stale = (
            f'<div class="mt-4 rounded-xl border border-amber-500/40 bg-amber-950/40 px-4 py-3 text-amber-100">'
            f"<strong>{escape(ex.get('label', 'Source exception'))}</strong>. "
            f"{escape(ex.get('note', ''))}</div>"
        )

    variants = ""
    for v in model.get("deploymentVariants") or []:
        variants += f"<li class=\"text-slate-300\"><code class=\"text-cyan-200\">{escape(v['tag'])}</code> — {escape(v.get('mode', ''))}</li>"

    ctx = model.get("contextTokens")
    ctx_s = f"{ctx:,} tokens" if ctx else "not specified in catalog"
    title = f"{model['displayName']} — Catalog model | NoCloudGPT"
    desc = (
        f"Catalog facts for {model['displayName']}: {fmt_param(model.get('parameterSizeB'))} parameters, "
        f"capabilities {', '.join(model.get('capabilities') or [])}. Deployment guidance via NoCloudGPT / terminal.glass."
    )
    canonical = f"{SITE}/models/model/{slug}/"
    json_ld = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": model["displayName"],
        "applicationCategory": "AI model",
        "description": desc,
        "url": canonical,
    }

    html = f"""<!doctype html>
<html lang="en">
<head>
{head_block(title, desc, canonical, robots=robots, json_ld=json_ld if not model.get('noindex') else None)}
</head>
<body class="bg-slate-950 text-slate-100">
{nav_html()}
  <header class="border-b border-slate-800 bg-slate-950/90">
    <div class="mx-auto max-w-6xl px-6 py-12">
      <a href="/models/" class="text-sm font-semibold text-cyan-300 hover:text-cyan-200">← Model catalog</a>
      <a href="/models/{escape(family['slug'])}/" class="ml-4 text-sm text-slate-400 hover:text-white">{escape(family['displayName'])} family</a>
      <p class="mt-6 text-sm font-bold uppercase tracking-[0.3em] text-cyan-300">Canonical model</p>
      <h1 class="mt-3 text-4xl font-black tracking-tight md:text-5xl">{escape(model['displayName'])}</h1>
      <p class="mt-4 max-w-3xl text-lg text-slate-300">Ollama tag: <code class="text-cyan-200">{escape(model.get('ollamaTag', ''))}</code></p>
      {stale}
      <div class="mt-8 flex flex-wrap gap-3">
        {deployment_cta(model)}
      </div>
    </div>
  </header>
  <main class="mx-auto max-w-6xl px-6 py-12 space-y-10">
    <section class="grid gap-6 md:grid-cols-2">
      <div class="rounded-2xl border border-slate-800 bg-slate-900 p-6">
        <h2 class="text-lg font-bold">Technical facts</h2>
        <ul class="mt-4 space-y-2 text-slate-300 text-sm">
          <li>Parameter size: {escape(fmt_param(model.get('parameterSizeB')))}</li>
          <li>Quantization: {escape(model.get('quantization') or '—')}</li>
          <li>Context: {escape(ctx_s)}</li>
          <li>Capabilities: {escape(', '.join(model.get('capabilities') or []))}</li>
          <li>Availability: {escape(model.get('availability', ''))}</li>
        </ul>
      </div>
      <div class="rounded-2xl border border-slate-800 bg-slate-900 p-6">
        <h2 class="text-lg font-bold">Deployment variants</h2>
        <ul class="mt-4 space-y-2 text-sm list-disc pl-5">{variants or '<li class="text-slate-400">No variants listed</li>'}</ul>
        <p class="mt-4 text-xs text-slate-500">Variant tags are not separate SEO pages.</p>
      </div>
    </section>
  </main>
{footer_html()}
</body>
</html>
"""
    out_path.write_text(normalize_html(html), encoding="utf-8")
    return out_path


CLOUD_CATALOG = ROOT / "models" / "data" / "terminal-glass-cloud-models.json"


def cloud_catalog_section_html() -> str:
    if not CLOUD_CATALOG.is_file():
        return ""
    entries = load_json(CLOUD_CATALOG)
    active = [
        e for e in entries
        if e.get("status") == "active" and not e.get("aliasOf")
    ]
    active.sort(key=lambda e: (e.get("priority", 999), e.get("slug", "")))
    cards = []
    for entry in active:
        slug = entry["slug"]
        name = escape(entry.get("displayName", slug))
        category = escape(entry.get("category", "").replace("-", " "))
        folder = entry.get("folder", f"/models/{slug}/")
        cards.append(
            f'<a href="{escape(folder)}" class="rounded-xl border border-slate-800 bg-slate-950 p-4 hover:border-cyan-500/50 block">'
            f'<div class="text-xs uppercase tracking-wider text-cyan-300">Terminal Glass Cloud</div>'
            f'<div class="mt-1 font-bold text-white">{name}</div>'
            f'<div class="mt-2 text-xs text-slate-400">{category}</div></a>'
        )
    grid = "\n        ".join(cards)
    return f"""
    <section class="mt-10 rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <div class="flex flex-col gap-2 md:flex-row md:items-end md:justify-between">
        <div>
          <p class="text-sm font-semibold uppercase tracking-[0.3em] text-cyan-300">Cloud deployment lane</p>
          <h2 class="mt-2 text-2xl font-bold text-white">Terminal Glass cloud model families</h2>
          <p class="mt-2 max-w-3xl text-sm text-slate-400">Ollama Cloud-backed inference with a small local Linux host. Licensing and packages: <a href="https://terminal.glass/pricing/" class="text-cyan-300 hover:text-cyan-200" target="_blank" rel="noopener">terminal.glass pricing</a>.</p>
        </div>
        <a href="/models/deploy/" class="text-sm font-semibold text-cyan-300 hover:text-cyan-200">Deployment options →</a>
      </div>
      <div class="mt-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {grid}
      </div>
    </section>"""


def write_catalog_landing(manifest: dict) -> Path:
    browse_path = CATALOG / "index" / "browse.json"
    browse_json = json.dumps(load_json(browse_path))
    out_path = ROOT / "models" / "index.html"
    title = "Private AI Model Catalog — Search &amp; deploy with NoCloudGPT"
    desc = (
        f"Search {manifest['counts']['siteFamilies']} model families and "
        f"{manifest['counts']['models']} catalog models. Filter by capability, availability, and deployment lane."
    )
    canonical = f"{SITE}/models/"

    html = f"""<!doctype html>
<html lang="en">
<head>
{head_block("Private AI Model Catalog — Deploy with NoCloudGPT", desc.replace("&amp;", "&"), canonical)}
</head>
<body class="bg-slate-950 text-slate-100">
{nav_html()}
  <header class="border-b border-slate-800 bg-slate-950/90">
    <div class="mx-auto max-w-7xl px-6 py-10">
      <p class="text-sm font-semibold uppercase tracking-[0.3em] text-cyan-300">Catalog · pinned projection</p>
      <h1 class="mt-3 text-4xl font-bold tracking-tight md:text-5xl">Find a model, plan a deployment.</h1>
      <p class="mt-5 max-w-3xl text-lg text-slate-300">Search families and canonical models from the pinned Phase 4A public catalog. No live Ollama requests at page load.</p>
      <p class="mt-2 text-sm text-slate-500">Manifest: {escape(manifest.get('projectionVersion', ''))}</p>
    </div>
  </header>
  <main class="mx-auto max-w-7xl px-6 py-10">
    <section class="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <div class="flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
        <div class="flex-1">
          <label for="catalog-search" class="text-sm font-semibold text-slate-400">Search</label>
          <input id="catalog-search" type="search" placeholder="Family, model, alias, capability…"
            class="mt-2 w-full rounded-xl border border-slate-700 bg-slate-950 px-4 py-3 text-white placeholder:text-slate-500 focus:border-cyan-400 focus:outline-none" autocomplete="off">
        </div>
        <button type="button" id="clear-filters" class="rounded-xl border border-slate-700 px-4 py-3 text-sm font-semibold text-slate-200 hover:bg-slate-800">Show all</button>
      </div>
      <div class="mt-6 flex flex-wrap gap-3">
        <label class="text-sm text-slate-400">Availability
          <select id="filter-availability" class="ml-2 rounded-lg border border-slate-700 bg-slate-950 px-3 py-1.5 text-sm">
            <option value="">Any</option>
            <option value="available">Available</option>
            <option value="stale_source">Stale source</option>
          </select>
        </label>
        <label class="text-sm text-slate-400">Local / private
          <select id="filter-local" class="ml-2 rounded-lg border border-slate-700 bg-slate-950 px-3 py-1.5 text-sm">
            <option value="">Any</option>
            <option value="yes">Suitable</option>
          </select>
        </label>
        <label class="text-sm text-slate-400">Cloud / Jet
          <select id="filter-cloud" class="ml-2 rounded-lg border border-slate-700 bg-slate-950 px-3 py-1.5 text-sm">
            <option value="">Any</option>
            <option value="yes">Supported</option>
          </select>
        </label>
        <label class="text-sm text-slate-400">Capability
          <select id="filter-capability" class="ml-2 rounded-lg border border-slate-700 bg-slate-950 px-3 py-1.5 text-sm">
            <option value="">Any</option>
            <option value="text">text</option>
            <option value="vision">vision</option>
            <option value="tools">tools</option>
            <option value="thinking">thinking</option>
            <option value="embedding">embedding</option>
            <option value="cloud">cloud</option>
          </select>
        </label>
        <label class="text-sm text-slate-400">Min params (B)
          <input id="filter-params" type="number" min="0" step="0.5" placeholder="e.g. 7"
            class="ml-2 w-20 rounded-lg border border-slate-700 bg-slate-950 px-3 py-1.5 text-sm">
        </label>
      </div>
      <p id="result-count" class="mt-4 text-sm text-slate-400"></p>
      <div id="empty-state" class="mt-8 hidden rounded-xl border border-dashed border-slate-700 p-8 text-center text-slate-400">
        <p>No matches. <button type="button" class="text-cyan-300 underline" id="empty-reset">Reset filters</button> to browse all catalog entries.</p>
      </div>
      <div id="results" class="mt-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-3"></div>
    </section>
{cloud_catalog_section_html()}
    <section class="mt-10 text-sm text-slate-500">
      <p>Families: {manifest['counts']['seoEligibleFamilies']} SEO-eligible · Models: {manifest['counts']['seoEligibleModels']} SEO-eligible · Source exceptions (noindex): {manifest['counts']['noindexSourceExceptions']}</p>
    </section>
  </main>
{footer_html()}
  <script id="catalog-browse-data" type="application/json">{browse_json}</script>
  <script>
    const BROWSE = JSON.parse(document.getElementById('catalog-browse-data').textContent);
    const resultsEl = document.getElementById('results');
    const emptyEl = document.getElementById('empty-state');
    const countEl = document.getElementById('result-count');

    function card(item) {{
      const type = item.type === 'family' ? 'Family' : 'Model';
      const badge = item.cloudJetSuitable ? '<span class="text-cyan-300">cloud</span>' : '';
      const local = item.localPrivateSuitable ? '<span class="text-emerald-400">local</span>' : '';
      return `<a href="${{item.path}}" class="rounded-xl border border-slate-800 bg-slate-950 p-4 hover:border-cyan-500/50 block">
        <div class="text-xs uppercase tracking-wider text-slate-500">${{type}}</div>
        <div class="mt-1 font-bold text-white">${{item.name}}</div>
        <div class="mt-2 text-xs text-slate-400">${{(item.capabilities || []).join(', ')}}</div>
        <div class="mt-2 text-xs gap-2 flex">${{badge}} ${{local}}</div>
      </a>`;
    }}

    function applyFilters() {{
      const q = document.getElementById('catalog-search').value.trim().toLowerCase();
      const avail = document.getElementById('filter-availability').value;
      const local = document.getElementById('filter-local').value;
      const cloud = document.getElementById('filter-cloud').value;
      const cap = document.getElementById('filter-capability').value;
      const minP = parseFloat(document.getElementById('filter-params').value) || 0;

      let items = BROWSE.filter(item => {{
        if (avail && item.availability !== avail) return false;
        if (local === 'yes' && !item.localPrivateSuitable) return false;
        if (cloud === 'yes' && !item.cloudJetSuitable) return false;
        if (cap && !(item.capabilities || []).includes(cap)) return false;
        if (minP && item.parameterSizeB != null && item.parameterSizeB < minP) return false;
        if (q) {{
          const hay = [item.name, item.slug, item.familySlug, (item.capabilities || []).join(' ')].join(' ').toLowerCase();
          if (!hay.includes(q)) return false;
        }}
        return true;
      }});

      // Prefer families first, cap visible cards
      items.sort((a,b) => (a.type === 'family' ? 0 : 1) - (b.type === 'family' ? 0 : 1) || a.name.localeCompare(b.name));
      const display = items.slice(0, 60);

      countEl.textContent = `${{items.length}} match(es) — showing ${{display.length}} (use search to narrow further)`;
      resultsEl.innerHTML = display.map(card).join('');
      emptyEl.classList.toggle('hidden', items.length > 0);
    }}

    ['catalog-search','filter-availability','filter-local','filter-cloud','filter-capability','filter-params'].forEach(id => {{
      document.getElementById(id).addEventListener('input', applyFilters);
      document.getElementById(id).addEventListener('change', applyFilters);
    }});
    document.getElementById('clear-filters').onclick = () => {{
      document.getElementById('catalog-search').value = '';
      document.getElementById('filter-availability').value = '';
      document.getElementById('filter-local').value = '';
      document.getElementById('filter-cloud').value = '';
      document.getElementById('filter-capability').value = '';
      document.getElementById('filter-params').value = '';
      applyFilters();
    }};
    document.getElementById('empty-reset').onclick = () => document.getElementById('clear-filters').click();
    applyFilters();
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
) -> Path:
    today = date.today().isoformat()
    urls: list[str] = []

    for p in STATIC_SITEMAP_PATHS:
        if p.endswith(".html"):
            urls.append(f"{SITE}{p if p.startswith('/') else '/' + p}")
        else:
            urls.append(f"{SITE}{p}")

    for f in families:
        if f.get("seoEligible"):
            urls.append(f"{SITE}/models/{f['slug']}/")

    # Preserve Terminal Glass cloud marketing lanes in sitemap (not overwritten by catalog build).
    models_dir = ROOT / "models"
    for child in sorted(models_dir.iterdir()):
        if child.is_dir() and child.name.endswith("-cloud") and (child / "index.html").is_file():
            urls.append(f"{SITE}/models/{child.name}/")

    for m in models:
        if m.get("seoEligible") and not m.get("noindex"):
            urls.append(f"{SITE}/models/model/{m['canonicalSlug']}/")

    # chatgpt-alternatives subpages — preserve from existing sitemap pattern
    alt_dir = ROOT / "models" / "chatgpt-alternatives"
    if alt_dir.is_dir():
        for child in sorted(alt_dir.iterdir()):
            if child.is_dir() and (child / "index.html").is_file():
                urls.append(f"{SITE}/models/chatgpt-alternatives/{child.name}/")

    urls = sorted(set(urls))

    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for loc in urls:
        url_el = ET.SubElement(urlset, "url")
        ET.SubElement(url_el, "loc").text = loc
        ET.SubElement(url_el, "lastmod").text = today

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    out = ROOT / "sitemap.xml"
    tree.write(out, encoding="utf-8", xml_declaration=True)
    return out


def main() -> int:
    if not CATALOG.is_dir():
        print(f"Missing pinned catalog: {CATALOG}", file=sys.stderr)
        return 1

    manifest = load_json(CATALOG / "manifest.json")
    families = load_json(CATALOG / "index" / "families.json")
    models = load_json(CATALOG / "index" / "models.json")
    family_by_slug = {f["slug"]: f for f in families}

    family_paths = []
    model_paths = []
    for f in families:
        if f.get("seoEligible"):
            p = write_family_page(f, models)
            if p:
                family_paths.append(p)
    for m in models:
        fam = family_by_slug.get(m["familySlug"])
        if fam:
            model_paths.append(write_model_page(m, fam))

    # Remove stale generated model pages from prior builds.
    model_root = ROOT / "models" / "model"
    keep = {m["canonicalSlug"] for m in models}
    if model_root.is_dir():
        for child in model_root.iterdir():
            if child.is_dir() and child.name not in keep:
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

    landing = write_catalog_landing(manifest)
    sitemap = write_sitemap(manifest, families, models)

    summary = {
        "familyPages": len(family_paths),
        "modelPages": len(model_paths),
        "landing": str(landing.relative_to(ROOT)),
        "sitemap": str(sitemap.relative_to(ROOT)),
        "manifest": manifest.get("projectionVersion"),
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
