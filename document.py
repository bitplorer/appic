"""Document SSoT — one HTML shell for every GET.

Isolation: this module never imports ux_channel.
Channel is the ux_dom.runtime alias — never ux_channel.Channel.
HTMX stays off. Component.render() stays a fragment.
"""
from __future__ import annotations

from ux_dom import Document
from ux_dom.runtime import XElement, Csp, Channel
from ux_dom.dom import link, meta, title, script

from settings import OUTPUT_CSS

_plugins = (
    XElement(),
    Csp.auto(
        style_hosts=("https://fonts.googleapis.com",),
        font_src=("'self'", "data:", "https://fonts.gstatic.com"),
        script_hosts=(
            "https://unpkg.com",
            "https://cdn.jsdelivr.net",
            "https://grok.com",
        ),
    ),
    Channel.optional(),
)
document = Document(
    head=[
        meta(charset="utf-8"),
        meta(name="viewport", content="width=device-width, initial-scale=1"),
        meta(name="theme-color", content="#07080A"),
        meta(name="description", content="APPIC — a house of making. Wedge kneads. Raku quenches. Ember is the last coal. Authored in ux-compose."),
        title("APPIC · a house of making"),
        link(rel="icon", type="image/svg+xml", href="/media/favicon.svg"),
        link(rel="apple-touch-icon", href="/__grok/icon-180.png"),
        link(rel="preconnect", href="https://fonts.googleapis.com"),
        link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True),
        link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,480;9..144,560;9..144,600&family=IBM+Plex+Mono:wght@400;500&family=Source+Sans+3:wght@400;500;600&display=swap",
        ),
        link(href=f"/css/{OUTPUT_CSS}", rel="stylesheet"),
        script(src="https://grok.com/grok-app-builder/extensions.js", defer=True),
        script(src="/media/preview-host-bridge.js", defer=True),
    ],
    body=[],
    ensure_csrf_token=False,
).use(*[p for p in _plugins if p is not None])
