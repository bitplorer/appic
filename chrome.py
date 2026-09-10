"""GET chrome — brand nav lives here, never inside Component.render().

Clock A wraps render() with build(wrap=). Morph payloads stay fragments.
"""
from __future__ import annotations

from typing import Any

from ux_compose import a, div, footer, header, main, nav, span
from ux_compose.chrome import GET_CHROME_ATTR

NAV = (
    ("/", "Table"),
    ("/enter", "Door"),
    ("/house", "House"),
    ("/atelier", "Atelier"),
    ("/commission", "Commission"),
    ("/forge", "Forge"),
    ("/studio", "Studio"),
    ("/lab", "Lab"),
    ("/docs", "Law"),
)


def foundry_wrap(document: Any, *, brand: str = "APPIC"):
    if document is None or not callable(document):
        raise TypeError(
            "foundry_wrap requires a callable Document. "
            "Product path is build(document=, wrap=foundry_wrap(document, brand=...))."
        )
    label = str(brand)

    def wrap(child: Any = None):
        links = [
            a(name, href=href, className="mark") for href, name in NAV
        ]
        chrome = header(
            a(
                span(label, className="brand-word"),
                span("foundry", className="brand-kicker"),
                href="/",
                className="brand-lockup",
            ),
            nav(*links, className="site-nav", aria_label="Foundry"),
            className="site-chrome",
            **{GET_CHROME_ATTR: True},
        )
        inner = main(child, id="main", className="site-main") if child is not None else main(id="main", className="site-main")
        foot = footer(
            span("Intent. Presence. Caps. Kit. Signal."),
            span("Server-authored · no React · L1 stays legal at L3"),
            className="site-foot",
        )
        return document(
            div(
                chrome,
                inner,
                foot,
                className="foundry-shell",
            )
        )

    wrap.brand = label  # type: ignore[attr-defined]
    return wrap
