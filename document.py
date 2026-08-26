"""Document SSoT — one HTML shell for every GET.

Isolation: this module never imports ux_channel.
HTMX stays off (use_htmx=False).
"""
from __future__ import annotations

try:
    from ux_dom import Document
    from ux_dom.runtime import XElement, Csp
    from ux_dom.dom import link, meta, title, script

    from settings import OUTPUT_CSS

    document = Document(
        head=[
            meta(charset="utf-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1"),
            title("APPIC · Intent · Presence · Caps"),
            link(href=f"/css/{OUTPUT_CSS}", rel="stylesheet"),
            script(src="https://grok.com/grok-app-builder/extensions.js", defer=True),
        ],
        body=[],
        ensure_csrf_token=False,
    ).use(XElement(), Csp.auto())

    def page(*body, page_title: str | None = None):
        extra_head = [title(page_title)] if page_title else []
        return document(*body, head=extra_head or None)

except Exception:
    document = None

    def page(*body, page_title: str | None = None):
        return body[0] if body else None
