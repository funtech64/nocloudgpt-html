#!/usr/bin/env python3
"""Synchronize only marked public header/footer blocks; leave editorial bytes intact."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

from apply_spectrum_chrome import active_for
from chrome import site_chrome, site_footer

ROOT = Path(__file__).resolve().parents[2]
HEADER = re.compile(
    r'<div class="ecosystem-bar" data-spectrum-chrome="1">[\s\S]*?</header>'
)
FOOTER = re.compile(
    r'<footer class="site-footer" data-spectrum-footer="1">[\s\S]*?</footer>'
)


def public_pages() -> list[Path]:
    return sorted(p for p in (ROOT / "models").rglob("*.html")
                  if "data" not in p.relative_to(ROOT / "models").parts)


def blocks(html: str) -> tuple[re.Match[str], re.Match[str] | None]:
    headers, footers = list(HEADER.finditer(html)), list(FOOTER.finditer(html))
    if len(headers) != 1 or len(footers) > 1:
        raise ValueError("Expected exactly one marked header and at most one marked footer")
    if html.count('data-spectrum-chrome="1"') != 1:
        raise ValueError("Incomplete or duplicate marked ecosystem bar")
    if html.count('data-spectrum-header="1"') != 1:
        raise ValueError("Expected exactly one marked navigation header")
    if html.count('data-spectrum-footer="1"') != len(footers):
        raise ValueError("Incomplete marked footer")
    if footers and footers[0].start() < headers[0].end():
        raise ValueError("Shared footer must follow the shared header")
    return headers[0], footers[0] if footers else None


def editorial_bytes(html: str) -> str:
    """Keep everything outside the two approved regions, including artwork and SEO."""
    header, footer = blocks(html)
    if footer:
        html = html[:footer.start()] + "[SHARED FOOTER]" + html[footer.end():]
    return html[:header.start()] + "[SHARED HEADER]" + html[header.end():]


def synchronize(html: str, active: str) -> str:
    header, footer = blocks(html)
    # Six existing truncated editorial pages have no marked footer. Do not repair
    # their document structure or invent missing content in this chrome-only pass.
    if footer:
        html = html[:footer.start()] + site_footer().strip() + html[footer.end():]
    navigation = site_chrome(active).split('<aside class="catalog-artwork-rail"', 1)[0].strip()
    return html[:header.start()] + navigation + html[header.end():]


def verify_editorial(ref: str, pages: list[Path]) -> None:
    for path in pages:
        rel = path.relative_to(ROOT).as_posix()
        original = subprocess.run(
            ["git", "show", f"{ref}:{rel}"], cwd=ROOT,
            capture_output=True, check=True,
        ).stdout.decode("utf-8")
        current = path.read_bytes().decode("utf-8")
        if editorial_bytes(original) != editorial_bytes(current):
            raise ValueError(f"Content outside shared chrome changed: {rel}")
    print(f"Editorial bytes unchanged against {ref} on {len(pages)} pages")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report drift without writing")
    parser.add_argument("--verify-editorial-against", metavar="REF")
    args = parser.parse_args()
    pages = public_pages()
    # Validate the whole batch before writing any page.
    updates = []
    for path in pages:
        before = path.read_bytes().decode("utf-8")
        after = synchronize(before, active_for(path))
        if editorial_bytes(before) != editorial_bytes(after):
            raise ValueError(f"Synchronization changed editorial content: {path}")
        if before != after:
            updates.append((path, after))
    if args.verify_editorial_against:
        verify_editorial(args.verify_editorial_against, pages)
    if args.check:
        for path, _ in updates:
            print(f"Stale public chrome: {path.relative_to(ROOT)}")
    else:
        for path, after in updates:
            path.write_bytes(after.encode("utf-8"))
    print(f"{'Stale' if args.check else 'Updated'}: {len(updates)} of {len(pages)} pages")
    return int(args.check and bool(updates))


if __name__ == "__main__":
    raise SystemExit(main())
