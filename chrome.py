"""GET chrome — outside Component.render(). Morph payloads stay fragments.

Uses GET_CHROME_ATTR so doctor scan_render_chrome stays quiet.
Isolation: no ux_channel.
"""
from __future__ import annotations

from typing import Any

from ux_compose import a, div, footer, header, main, nav, p, span, svg, path, circle
from ux_compose.chrome import GET_CHROME_ATTR, DEFAULT_BRAND

ROOMS = (
    ("/", "Table"),
    ("/enter", "Door"),
    ("/house", "House"),
    ("/commission", "Make"),
    ("/market", "Hall"),
    ("/forge", "Forge"),
    ("/rail", "Rail"),
    ("/studio", "Studio"),
    ("/overlay", "Edge"),
    ("/cut", "Cut"),
    ("/boot", "Boot"),
    ("/trace", "Trace"),
    ("/docs", "Law"),
    ("/deploy", "Ship"),
)


def mark():
    return svg(
        circle(cx="12", cy="12", r="9", fill="none", stroke="currentColor", stroke_width="1.4"),
        circle(cx="12", cy="12", r="2.2", fill="currentColor"),
        path(d="M12 3v3.2M12 17.8V21M3 12h3.2M17.8 12H21", fill="none", stroke="currentColor", stroke_width="1.2"),
        viewBox="0 0 24 24",
        width="22",
        height="22",
        aria_hidden="true",
        className="mark",
    )


def top_nav():
    links = [
        a(
            label,
            href=href,
            className="room-link",
        )
        for href, label in ROOMS
    ]
    return header(
        a(mark(), span("APPIC", className="brand"), href="/", className="wordmark", aria_label="APPIC table"),
        nav(*links, className="rooms", aria_label="Rooms"),
        a("Command", href="/command", className="ghost"),
        className="top",
        **{GET_CHROME_ATTR: True},
    )


def foot():
    return footer(
        p("APPIC · ux-compose 0.1.0 · kit-81 · Cut C · Channel.boot · shell=False"),
        p("GET is Clock A. Action is Clock B. Empty Content-Type is bad_request."),
        className="foot",
        role="contentinfo",
    )


def foundry_wrap(document: Any, *, brand: str = "APPIC"):
    """Document wrap. Brand lives here, never inside render()."""
    if document is None or not callable(document):
        raise TypeError(
            "foundry_wrap requires a callable Document. "
            "Product path is build(document=, wrap=foundry_wrap(document))."
        )
    label = str(brand or DEFAULT_BRAND)

    def wrap(child: Any = None):
        node = child
        return document(
            div(
                top_nav(),
                main(node, id="stage", className="stage"),
                foot(),
                className="shell",
                data_brand=label,
                **{GET_CHROME_ATTR: True},
            )
        )

    wrap.brand = label  # type: ignore[attr-defined]
    return wrap
