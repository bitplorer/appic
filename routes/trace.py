"""Page unit — Doctor residuals. Hard vs teaching vs store-clone."""
from __future__ import annotations

from pathlib import Path

from ux_compose import Component, article, div, h1, h2, li, p, section, span, ul, doctor
from ux_compose.doctor import (
    scan_isolation,
    scan_kit_product_imports,
    scan_leftover_aliases,
    scan_render_chrome,
    scan_fastapi_docs_collision,
    scan_cek_host,
    scan_store_clone,
    scan_dual_document,
    scan_store_precedence,
)


class Trace(Component):
    id = "trace"

    def render(self):
        root = Path(__file__).resolve().parents[1]
        paths = [
            str(p)
            for p in root.rglob("*.py")
            if "site-packages" not in str(p) and "/.venv/" not in str(p)
        ]
        families = (
            ("isolation (hard)", scan_isolation(paths)),
            ("dual-Document (hard)", scan_dual_document(paths)),
            ("store-clone (hard)", scan_store_clone(paths)),
            ("store-precedence (hard)", scan_store_precedence()),
            ("kit imports (teaching)", scan_kit_product_imports(paths)),
            ("leftover aliases (teaching)", scan_leftover_aliases(paths)),
            ("render chrome (teaching)", scan_render_chrome(paths)),
            ("docs collision (teaching)", scan_fastapi_docs_collision(paths)),
            ("cek host (teaching)", scan_cek_host(None)),
        )
        report = doctor(paths, fail=False)
        cards = []
        for name, hits in families:
            shown = hits or ["clean"]
            items = [li(h) for h in shown[:8]]
            cards.append(article(h2(name), ul(*items, className="mono-list"), className="paper"))
        return section(
            span("Trace", className="eyebrow"),
            h1("Residuals expire by teaching.", className="display"),
            p(
                f"Doctor ok={getattr(report, 'ok', None)}. Isolation, dual-Document, store-clone, and store-precedence fail closed. "
                "Kit-import, leftover aliases, render-chrome, docs collision teach. Redis wins; do not export both store envs.",
                className="lede",
            ),
            div(*cards, className="map-grid"),
            id=self.id,
            className="room",
        )
