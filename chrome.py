"""GET chrome — outside Component.render(). Morph payloads stay fragments.

Uses GET_CHROME_ATTR so doctor scan_render_chrome stays quiet.
Isolation: no ux_channel.
"""
from __future__ import annotations

from typing import Any

from ux_compose import a, div, footer, header, main, nav, p, span, svg, path, circle
from ux_compose.chrome import GET_CHROME_ATTR, DEFAULT_BRAND

from store import HOST, clock_label, waveform_d, VESSEL_BODY, VESSEL_WELL, crack_d

ROOMS = (
    ("/", "Table"),
    ("/now", "Now"),
    ("/vessel", "Vessel"),
    ("/watch", "Watch"),
    ("/vitrine", "Vitrine"),
    ("/kintsugi", "Mend"),
    ("/gift", "Gift"),
    ("/lineage", "Lineage"),
    ("/docs", "Law"),
)

LOOP = (
    ("/brief", "Brief"),
    ("/wheel", "Wheel"),
    ("/glaze", "Glaze"),
    ("/commission", "Make"),
    ("/kiln", "Kiln"),
    ("/watch", "Watch"),
    ("/atmosphere", "Air"),
    ("/vitrine", "Vitrine"),
    ("/kintsugi", "Mend"),
    ("/gift", "Gift"),
)

DOCK = (
    ("/", "Table"),
    ("/now", "Now"),
    ("/vessel", "Vessel"),
    ("/kintsugi", "Mend"),
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


def vessel_mark(piece: dict | None = None, *, size: int = 36, ident: str = "cradle-vessel"):
    """Presence-continuous vessel. Same id in chrome and rooms for scene.share."""
    row = piece or {}
    stage = str(row.get("stage") or "empty")
    join = str(row.get("join") or "")
    brk = str(row.get("break") or "")
    where = join or brk
    crack = crack_d(where)
    kids = [
        path(d=VESSEL_BODY, fill="none", stroke="currentColor", stroke_width="2.2", className="vessel-body"),
        path(d=VESSEL_WELL, fill="none", stroke="currentColor", stroke_width="1.2", className="vessel-well"),
    ]
    if crack:
        kids.append(
            path(
                d=crack,
                fill="none",
                stroke="currentColor",
                stroke_width="2.4" if join else "1.4",
                stroke_linecap="round",
                className="vessel-join" if join else "vessel-crack",
            )
        )
    return svg(
        *kids,
        viewBox="0 0 100 124",
        width=str(size),
        height=str(int(size * 1.24)),
        className="vessel-svg",
        id=ident,
        role="img",
        aria_label=f"Vessel {stage}",
        data_stage=stage,
        data_join=join or "none",
        data_break=brk or "none",
    )


def resonance(band: str = "idle"):
    """Hearth waveform. Peak is denser. Idle is still."""
    return svg(
        path(
            d=waveform_d(band),
            fill="none",
            stroke="currentColor",
            stroke_width="1.4",
            stroke_linecap="round",
            className="wave-path",
        ),
        viewBox="0 0 240 36",
        preserveAspectRatio="none",
        className="wave",
        role="img",
        aria_label=f"Hearth resonance {band}",
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


def instrument():
    HOST.sync_sky()
    sky = str(HOST.sky_band or "night")
    heat = f"{HOST.heat_remain}h" if HOST.firing else "hearth dark"
    notice = str(HOST.notice or "the house is listening")
    present = HOST.occupied[0] if HOST.occupied else "table"
    band = "peak" if HOST.firing and HOST.heat_remain <= 5 else (
        "warm" if HOST.firing else "idle"
    )
    return div(
        span(sky, className="inst-band"),
        span(clock_label(HOST.clock_h), className="inst-clock", aria_label="House clock"),
        span(heat, className="inst-heat"),
        span(present, className="inst-present"),
        resonance(band),
        span(notice, className="inst-notice"),
        className="instrument",
        aria_label="Living instrument",
        **{GET_CHROME_ATTR: True},
    )


def cradle():
    """GET chrome cradle. The vessel does not remount when you walk. CRADLE-1."""
    piece = HOST.vessel
    if not piece:
        return a(
            span("cradle empty", className="cradle-kicker"),
            href="/vessel",
            className="cradle is-empty",
            aria_label="Empty cradle. Seat a vessel.",
            **{GET_CHROME_ATTR: True},
        )
    stage = str(piece.get("stage") or "drawn")
    clay = str(piece.get("clay") or "clay")
    glaze = str(piece.get("glaze") or "glaze")
    return a(
        vessel_mark(piece, size=32, ident="cradle-vessel"),
        span(
            span(clay, className="cradle-clay"),
            span(f"{glaze} · {stage}", className="cradle-stage"),
            className="cradle-copy",
        ),
        href="/vessel",
        className=f"cradle is-seated stage-{stage}",
        aria_label=f"Vessel {clay} {stage}",
        data_stage=stage,
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
        p("APPIC · a house of making · ux-compose 0.1.0 · 80563ab · kit-81 · vessel · cradle · kintsugi · gift · lineage"),
        p("GET is Clock A. Action is Clock B. The vessel is presence-continuous. Brass is the join. Gift leaves the cloth."),
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
        sky = HOST.sync_sky()
        if sky not in ("night", "dusk", "dawn", "noon"):
            sky = "night"
        stage = str((HOST.vessel or {}).get("stage") or "empty")
        return document(
            div(
                top_nav(),
                instrument(),
                cradle(),
                loop_rail(),
                main(node, id="stage", className="stage"),
                foot(),
                dock(),
                className="shell",
                data_brand=label,
                data_band=sky,
                data_firing="1" if HOST.firing else "0",
                data_stage=stage,
                **{GET_CHROME_ATTR: True},
            )
        )

    wrap.brand = label  # type: ignore[attr-defined]
    return wrap
