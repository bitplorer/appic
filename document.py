"""Document SSoT — one HTML shell for every GET.

Component.render() stays a fragment. Brand, fonts, CSP, Channel client,
and the Grok preview bridge live here / in wrap=. Isolation: never import
ux_channel. Channel is the ux_dom.runtime alias.
"""
from __future__ import annotations

from ux_dom import Document
from ux_dom.dom import link, meta, script, title
from ux_dom.runtime import Channel, Csp, XElement

from settings import BRAND, DEBUG, OUTPUT_CSS

_csp = None
if not DEBUG:
    _csp = Csp.prod(
        script_hosts=["'self'", "https://grok.com"],
        frame_ancestors="*",
        img_src=["'self'", "data:", "https:"],
        connect_src=["'self'", "ws:", "wss:", "https://grok.com"],
    )
else:
    # Nonce + 'unsafe-inline' is ignored; Grok's pill and Tailwind CDN
    # need inline style. Preview keeps CSP off; prod uses Csp.prod().
    _csp = None


document = Document(
    head=[
        meta(charset="utf-8"),
        meta(name="viewport", content="width=device-width, initial-scale=1"),
        meta(name="theme-color", content="#0c0d0b"),
        meta(
            name="description",
            content="APPIC — a nocturnal foundry OS authored in ux-compose. Intent. Presence. Caps.",
        ),
        title(f"{BRAND} · foundry"),
        link(rel="icon", type="image/svg+xml", href="/favicon.svg"),
        link(rel="apple-touch-icon", href="/__grok/icon-180.png"),
        link(rel="manifest", href="/__grok/manifest.webmanifest"),
        link(rel="preconnect", href="https://fonts.googleapis.com"),
        link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin="anonymous"),
        link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Source+Sans+3:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap",
        ),
        script(src="https://cdn.tailwindcss.com"),
        link(href=f"/css/{OUTPUT_CSS}", rel="stylesheet"),
        link(href="/static/css/kit.css", rel="stylesheet"),
        link(href="/static/css/appic.css", rel="stylesheet"),
        script(src="/static/js/preview-bridge.js", defer=True),
        script(src="https://grok.com/grok-app-builder/extensions.js"),
    ],
    body=[],
    ensure_csrf_token=False,
).use(*[p for p in (XElement(), _csp, Channel.optional()) if p is not None])
