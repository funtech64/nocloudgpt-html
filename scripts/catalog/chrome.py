"""Shared COLORS.chat Spectrum Mark chrome for catalog HTML."""

from __future__ import annotations

HEAD_LINKS = """  <link rel="apple-touch-icon" href="/brand/brand-mark.png">
  <meta property="og:image" content="https://nocloudgpt.com/brand/colors-chat-workspace.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://nocloudgpt.com/brand/colors-chat-workspace.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/brand/chrome.css">"""


def site_chrome(active: str = "models") -> str:
    def cur(name: str) -> str:
        return ' aria-current="page"' if active == name else ""

    return f"""
<div class="ecosystem-bar" data-spectrum-chrome="1">
  <div class="ecosystem-inner">
    <span class="ecosystem-label">COLORS.chat network</span>
    <div>
      <a href="https://colorschat.com" target="_blank" rel="noopener">colorschat.com · YouTube</a>
      <a href="https://colors.chat" target="_blank" rel="noopener">colors.chat · Order now</a>
      <a href="https://terminal.glass" target="_blank" rel="noopener">terminal.glass · Deploy</a>
    </div>
  </div>
</div>
<header class="site-header" data-spectrum-header="1">
  <div class="nav-wrap">
    <a href="/" class="lockup" aria-label="COLORS.chat via NoCloudGPT">
      <span class="spectrum-mark" aria-hidden="true"></span>
      <span class="lockup-text">
        <strong class="wordmark">COLORS.chat</strong>
        <span>Private deployment · NoCloudGPT</span>
      </span>
    </a>
    <nav class="site-nav" aria-label="Primary">
      <a href="/software.html"{cur("product")}>Product</a>
      <a href="/models/deploy/"{cur("deploy")}>Deploy</a>
      <a href="/models/"{cur("models")}>Models</a>
      <a href="/pricing.html"{cur("licensing")}>Licensing</a>
      <a href="/services.html"{cur("services")}>Services</a>
      <a href="/contact.html"{cur("contact")}>Contact</a>
      <a class="btn btn-primary" href="https://colors.chat" target="_blank" rel="noopener">Order now</a>
    </nav>
  </div>
</header>
<aside class="catalog-artwork-rail" data-spectrum-artwork="1">
  <figure>
    <img src="/brand/colors-chat-workspace.jpg" width="1400" height="933" alt="COLORS.chat workspace with Spectrum Mark and gradient wordmark">
  </figure>
  <div>
    <p class="eyebrow">COLORS.chat artwork</p>
    <p>These models run in the <strong>COLORS.chat</strong> workspace — on your Mac, your Linux server, or your cloud. COLORS.chat, powered by colorsXUI.</p>
  </div>
</aside>
"""


def site_footer() -> str:
    return """
<footer class="site-footer" data-spectrum-footer="1">
  <div class="footer-grid">
    <div>
      <a href="/" class="lockup" style="margin-bottom:0.8rem;">
        <span class="spectrum-mark" aria-hidden="true"></span>
        <span class="lockup-text">
          <strong class="wordmark">COLORS.chat</strong>
          <span>via NoCloudGPT</span>
        </span>
      </a>
      <p>Colorado, USA · Remote services available · In-person: Denver Metro Area only</p>
      <p>© 2026 NoCloudGPT · COLORS.chat, powered by colorsXUI</p>
    </div>
    <div>
      <h3>Network</h3>
      <a href="https://colorschat.com" target="_blank" rel="noopener">colorschat.com · YouTube</a>
      <a href="https://colors.chat" target="_blank" rel="noopener">colors.chat · Order now</a>
      <a href="https://terminal.glass" target="_blank" rel="noopener">terminal.glass · Deploy</a>
      <a href="https://terminal.glass/pricing/" target="_blank" rel="noopener">Glass License pricing</a>
    </div>
    <div>
      <h3>This site</h3>
      <a href="/software.html">Product</a>
      <a href="/models/">Model catalog</a>
      <a href="/models/deploy/">Deployment guides</a>
      <a href="/pricing.html">Licensing overview</a>
      <a href="/contact.html">Contact</a>
    </div>
  </div>
</footer>
"""
