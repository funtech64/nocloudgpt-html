#!/usr/bin/env python3
"""Apply Spectrum Mark chrome and COLORS.chat artwork to catalog HTML pages."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from chrome import HEAD_LINKS, site_chrome, site_footer

ROOT = Path(__file__).resolve().parents[2]
MODELS = ROOT / "models"

HEAD_MARK = "/brand/chrome.css"
CHROME_MARK = 'data-spectrum-chrome="1"'
ART_MARK = 'data-spectrum-artwork="1"'
FOOT_MARK = 'data-spectrum-footer="1"'

# First-in-body nav bars that only brand as NoCloudGPT text.
OLD_TOP_CHROME = re.compile(
    r"""
    (?:
      <div\s+class="bg-slate-900/90[^"]*">[\s\S]*?</div>\s*
    )?
    (?:
      <div\s+class="border-b border-slate-800 bg-slate-950/95">[\s\S]*?</div>\s*
    )?
    (?:
      <header\s+class="border-b border-slate-800[^"]*">\s*
        <div[^>]*>\s*
          (?:<nav[\s\S]*?</nav>|
             <a\s+href="/"[\s\S]*?</a>\s*<nav[\s\S]*?</nav>)
        \s*</div>\s*
      </header>\s*
    )
    """,
    re.IGNORECASE | re.VERBOSE,
)

OLD_FOOTER = re.compile(
    r"""<footer\b[^>]*>[\s\S]*?</footer>\s*(?=</body>)""",
    re.IGNORECASE,
)

SPECTRUM_CHROME_BLOCK = re.compile(
    r"""<div\s+class="ecosystem-bar"[^>]*data-spectrum-chrome="1"[\s\S]*?</aside>\s*""",
    re.IGNORECASE,
)
SPECTRUM_FOOTER_BLOCK = re.compile(
    r"""<footer\s+class="site-footer"[^>]*data-spectrum-footer="1"[\s\S]*?</footer>\s*""",
    re.IGNORECASE,
)

# Inner editorial/cloud nav bars left after Spectrum chrome is prepended.
LEFTOVER_NAV_HEADER = re.compile(
    r'(?:<!--[\s\S]{0,240}?NAVIGATION[\s\S]{0,120}?-->\s*)?'
    r'<header\s+class="border-b border-slate-800[^"]*">\s*'
    r'<div[^>]*>\s*'
    r'(?:<nav[\s\S]*?</nav>|<a[\s\S]*?</a>\s*<nav[\s\S]*?</nav>)'
    r'\s*</div>\s*</header>\s*',
    re.IGNORECASE,
)

ACTIVE_BY_PREFIX = (
    ("models/deploy/", "deploy"),
    ("models/pricing.html", "licensing"),
    ("models/quote.html", "models"),
    ("models/", "models"),
)


def active_for(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    for prefix, name in ACTIVE_BY_PREFIX:
        if rel.startswith(prefix) or rel == prefix.rstrip("/"):
            return name
    return "models"


def ensure_head_links(html: str) -> str:
    if HEAD_MARK in html:
        return html
    if re.search(r"</head>", html, re.I):
        return re.sub(r"</head>", HEAD_LINKS + "\n</head>", html, count=1, flags=re.I)
    return html


def strip_old_top_chrome(html: str) -> str:
    def repl_body(match: re.Match[str]) -> str:
        start = match.group(0)
        rest = html[match.end() :]
        old = OLD_TOP_CHROME.match(rest)
        if not old:
            return start
        return start

    # Operate on the body contents only.
    m = re.search(r"(<body\b[^>]*>)([\s\S]*)$", html, re.I)
    if not m:
        return html
    prefix, body = m.group(1), m.group(2)
    body = SPECTRUM_CHROME_BLOCK.sub("", body, count=1)
    body = OLD_TOP_CHROME.sub("", body, count=1)
    return html[: m.start()] + prefix + body


def replace_site_footer(html: str) -> str:
    if FOOT_MARK in html:
        return SPECTRUM_FOOTER_BLOCK.sub(site_footer() + "\n", html, count=1)
    if OLD_FOOTER.search(html):
        return OLD_FOOTER.sub(site_footer() + "\n", html, count=1)
    return re.sub(r"</body>", site_footer() + "\n</body>", html, count=1, flags=re.I)


def insert_chrome(html: str, active: str) -> str:
    chrome = site_chrome(active)
    m = re.search(r"(<body\b[^>]*>)", html, re.I)
    if not m:
        return html
    return html[: m.end()] + chrome + html[m.end() :]


def strip_leftover_inner_nav(html: str) -> str:
    return LEFTOVER_NAV_HEADER.sub("", html, count=4)


def apply_file(path: Path) -> bool:
    before = path.read_text(encoding="utf-8")
    html = before
    html = ensure_head_links(html)
    html = strip_old_top_chrome(html)
    html = insert_chrome(html, active_for(path))
    html = strip_leftover_inner_nav(html)
    html = replace_site_footer(html)
    if html == before:
        return False
    path.write_text(html, encoding="utf-8")
    return True


def main() -> int:
    pages = sorted(p for p in MODELS.rglob("*.html") if "data/P4-Public-Catalog" not in p.as_posix())
    changed = 0
    for path in pages:
        if apply_file(path):
            changed += 1
    print(f"updated {changed} of {len(pages)} catalog HTML pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
