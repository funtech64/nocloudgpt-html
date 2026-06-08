#!/usr/bin/env python3
"""
NoCloudGPT Artwork Downloader
Downloads hero images for all model families and updates index.html files.
Run this from the root of the nocloudgpt-html repository.
"""

import os
import re
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Configuration
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(REPO_ROOT, "models")
ARTWORK_MANIFEST = os.path.join(MODELS_DIR, "artwork-sources.md")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; NoCloudGPT-ArtworkBot/1.0)"
}
DELAY_BETWEEN_REQUESTS = 1.5  # seconds - be polite

def parse_manifest():
    """Parse the artwork-sources.md file and return a list of families."""
    families = []
    with open(ARTWORK_MANIFEST, "r", encoding="utf-8") as f:
        content = f.read()

    # Simple regex to extract table rows
    pattern = r"\|\s*(\d+)\s*\|\s*([a-z0-9\-]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|"
    matches = re.findall(pattern, content)

    for match in matches:
        families.append({
            "number": match[0].strip(),
            "slug": match[1].strip(),
            "family_name": match[2].strip(),
            "official_link": match[3].strip(),
            "photo_reference": match[4].strip(),
            "brand_link": match[5].strip(),
            "ollama_link": match[6].strip(),
            "priority": match[7].strip() if len(match) > 7 else "Low"
        })
    return families


def download_image(url, save_path):
    """Download an image from a URL."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"    ✗ Failed to download {url}: {e}")
    return False


def update_html_file(family_slug, hero_path):
    """Update the index.html with local image path and source reference block."""
    html_path = os.path.join(MODELS_DIR, family_slug, "index.html")
    if not os.path.exists(html_path):
        print(f"    ⚠ No index.html found for {family_slug}")
        return False

    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace common placeholder patterns with local image
    content = re.sub(
        r'<!--\s*ARTWORK PLACEHOLDER.*?-->', 
        f'<img src="/models/{family_slug}/hero.jpg" alt="{family_slug} hero" class="w-full rounded-2xl">', 
        content, 
        flags=re.DOTALL
    )

    # Add Artwork and source references block if it doesn't exist
    if "Artwork and source references" not in content:
        reference_block = f"""
<section class="mt-10 rounded-3xl border border-slate-800 bg-slate-900 p-6">
  <h2 class="text-2xl font-black">Artwork and source references</h2>
  <p class="mt-3 text-slate-300">
    These links are provided for future model-family artwork, brand verification,
    and visual sourcing. Review license and brand rules before using any image in production.
  </p>
  <ul class="mt-4 space-y-2 text-slate-300">
    <li>
      <a class="text-cyan-300 hover:text-cyan-200" href="https://ollama.com/library/{family_slug}" target="_blank" rel="noopener">
        Official model or developer reference
      </a>
    </li>
    <li>
      <a class="text-cyan-300 hover:text-cyan-200" href="https://unsplash.com/s/photos/ai" target="_blank" rel="noopener">
        Suggested photo reference
      </a>
    </li>
  </ul>
</section>
"""
        # Insert before the final footer or closing tags
        if "</main>" in content:
            content = content.replace("</main>", reference_block + "\n</main>")
        else:
            content += "\n" + reference_block

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)

    return True


def main():
    print("Starting NoCloudGPT Artwork Download Script...\n")
    families = parse_manifest()
    print(f"Found {len(families)} families in manifest.\n")

    success_count = 0
    failed_count = 0

    for family in families:
        slug = family["slug"]
        ollama_link = family["ollama_link"]

        print(f"[{family['number']}] Processing: {family['family_name']} ({slug})")

        family_dir = os.path.join(MODELS_DIR, slug)
        os.makedirs(family_dir, exist_ok=True)

        hero_path = os.path.join(family_dir, "hero.jpg")

        # Try to get image from Ollama library page
        downloaded = False
        if "ollama.com/library" in ollama_link:
            try:
                time.sleep(DELAY_BETWEEN_REQUESTS)
                resp = requests.get(ollama_link, headers=HEADERS, timeout=10)
                if resp.status_code == 200:
                    soup = BeautifulSoup(resp.text, "html.parser")
                    # Look for og:image or first large image
                    og_image = soup.find("meta", property="og:image")
                    if og_image and og_image.get("content"):
                        img_url = og_image["content"]
                        if download_image(img_url, hero_path):
                            print(f"    ✓ Downloaded hero.jpg from Ollama")
                            downloaded = True
            except Exception as e:
                print(f"    ✗ Error scraping Ollama: {e}")

        if not downloaded:
            print(f"    ⚠ No suitable image found. Leaving placeholder.")
            # You can add fallback Unsplash download logic here if desired

        # Always update the HTML file
        if update_html_file(slug, hero_path):
            print(f"    ✓ Updated index.html")
            success_count += 1
        else:
            failed_count += 1

        print()

    print("=" * 50)
    print(f"Finished processing {len(families)} families.")
    print(f"Successful updates: {success_count}")
    print(f"Failed updates: {failed_count}")
    print("=" * 50)


if __name__ == "__main__":
    main()
