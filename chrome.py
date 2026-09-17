"""GET chrome — outside Component.render(). Morph payloads stay fragments.

Uses GET_CHROME_ATTR so doctor scan_render_chrome stays quiet.
Isolation: no ux_channel.
"""
from __future__ import annotations

from typing import Any

from ux_compose import a, div, footer, header, main, nav, p, span, svg, path, circle
from ux_compose.chrome import GET_CHROME_ATTR, DEFAULT_BRAND

from store import HOST

ROOMS = (
    ("/", "Table"),
    ("/brief", "Brief"),
    ("/wheel", "Wheel"),
    ("/glaze", "Glaze"),
    ("/commission", "Make"),
    ("/kiln", "Kiln"),
    ("/watch", "Watch"),
    ("/vitrine", "Vitrine"),
    ("/hands", "Hands"),
    ("/docs", "Law"),
)

LOOP = (
    ("/brief", "Brief"),
    ("/wheel", "Wheel"),
    ("/glaze", "Glaze"),
    ("/commission", "Make"),
    ("/kiln", "Kiln"),
    ("/watch", "Watch"),
    ("/vitrine", "Vitrine"),
)

DOCK = (
    ("/", "Table"),
    ("/wheel", "Wheel"),
    ("/watch", "Watch"),
    ("/vitrine", "Shelf"),
    ("/command", "Cmd"),
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
        a(label, href=href, className="room-link")
        for href, label in ROOMS
    ]
    return header(
        a(mark(), span("APPIC", className="brand"), href="/", className="wordmark", aria_label="APPIC table"),
        nav(*links, className="rooms", aria_label="Rooms"),
        a(
            span("Command"),
            span("⌘K", className="kbd"),
            href="/command",
            className="cmd-chip",
            aria_label="Open command",
        ),
        className="top",
        **{GET_CHROME_ATTR: True},
    )


def loop_rail():
    steps = []
    for i, (href, label) in enumerate(LOOP):
        if i:
            steps.append(span("→", className="loop-arrow", aria_hidden="true"))
        steps.append(a(label, href=href, className="loop-step"))
    heat = f"{HOST.heat_remain}h" if HOST.firing else "hearth dark"
    return nav(
        span("loop", className="loop-kicker"),
        *steps,
        span(heat, className="loop-heat"),
        className="loop-rail",
        aria_label="Foundry loop",
    )


def dock():
    links = [a(label, href=href) for href, label in DOCK]
    return nav(*links, className="dock", aria_label="Mobile rooms")


def foot():
    return footer(
        p("APPIC · ux-compose 0.1.0 · 80563ab · kit-81 · Cut C · Channel.boot · extract_by_id"),
        p("GET is Clock A. Action is Clock B. Empty Content-Type is bad_request. The watch keeps the heat."),
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
        sky = str(HOST.sky_band or "night")
        if sky not in ("night", "dusk", "dawn"):
            sky = "night"
        return document(
            div(
                top_nav(),
                loop_rail(),
                main(node, id="stage", className="stage"),
                foot(),
                dock(),
                className="shell",
                data_brand=label,
                data_band=sky,
                data_firing="1" if HOST.firing else "0",
                **{GET_CHROME_ATTR: True},
            )
        )

    wrap.brand = label  # type: ignore[attr-defined]
    return wrap
