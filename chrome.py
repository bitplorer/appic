"""GET chrome — outside Component.render(). Morph payloads stay fragments.

Uses GET_CHROME_ATTR so doctor scan_render_chrome stays quiet.
Isolation: no ux_channel.
"""
from __future__ import annotations

from typing import Any

from ux_compose import a, circle, div, footer, header, main, nav, p, path, span, svg
from ux_compose.chrome import DEFAULT_BRAND, GET_CHROME_ATTR

from store import (
    HOST,
    STAFF_LINES,
    VESSEL_BODY,
    VESSEL_WELL,
    ash_d,
    clock_label,
    crack_d,
    grain_d,
    note_cy,
    staff_line_d,
    tide_d,
    waveform_d,
)

ROOMS = (
    ("/", "Table"),
    ("/now", "Now"),
    ("/tide", "Tide"),
    ("/ash", "Ash"),
    ("/grain", "Grain"),
    ("/stamp", "Stamp"),
    ("/well", "Well"),
    ("/vessel", "Vessel"),
    ("/watch", "Watch"),
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
    ("/score", "Score"),
    ("/chorus", "Chorus"),
    ("/tide", "Tide"),
    ("/fugue", "Fugue"),
    ("/ash", "Ash"),
    ("/stamp", "Stamp"),
)

DOCK = (
    ("/", "Table"),
    ("/ash", "Ash"),
    ("/grain", "Grain"),
    ("/stamp", "Stamp"),
    ("/well", "Well"),
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


def tide_mark(phase: str = "new"):
    """Lunar climate fragment in GET chrome. TIDE-1."""
    return svg(
        path(
            d=tide_d(phase),
            fill="none",
            stroke="currentColor",
            stroke_width="1.4",
            stroke_linecap="round",
            className="wave-path",
        ),
        viewBox="0 0 240 36",
        preserveAspectRatio="none",
        className="wave tide-wave",
        role="img",
        aria_label=f"Tide {phase}",
    )


def grain_mark(body: str = "fine"):
    """Clay body fragment in GET chrome. GRAIN-1."""
    return svg(
        path(
            d=grain_d(body),
            fill="none",
            stroke="currentColor",
            stroke_width="1.4",
            stroke_linecap="round",
            className="wave-path",
        ),
        viewBox="0 0 120 120",
        className="wave grain-wave",
        role="img",
        aria_label=f"Grain {body}",
    )


def ash_mark(grade: str = "fine"):
    """Remainder fragment in GET chrome. ASH-1."""
    return svg(
        path(
            d=ash_d(grade),
            fill="none",
            stroke="currentColor",
            stroke_width="1.4",
            stroke_linecap="round",
            className="wave-path",
        ),
        viewBox="0 0 240 36",
        preserveAspectRatio="none",
        className="wave ash-wave",
        role="img",
        aria_label=f"Ash {grade}",
    )


def staff_mark(notes: list[dict] | None = None, *, ident: str = "chrome-staff"):
    """Living score fragment in GET chrome. SCORE-1."""
    rows = list(notes or HOST.score[-10:])
    kids = [
        path(
            d=staff_line_d(y, 220),
            fill="none",
            stroke="currentColor",
            stroke_width="0.7",
            className="staff-line",
        )
        for y in STAFF_LINES
    ]
    for i, row in enumerate(rows[-10:]):
        x = 14 + i * 20
        cy = note_cy(str(row.get("pitch") or "G"))
        nid = str(row.get("id") or f"cn{i}")
        kids.append(
            circle(
                cx=str(x),
                cy=str(cy),
                r="3.4",
                fill="currentColor",
                className="staff-note",
                id=f"chrome-{nid}",
            )
        )
    return svg(
        *kids,
        viewBox="0 0 220 80",
        className="staff",
        id=ident,
        role="img",
        aria_label=f"House score {len(HOST.score)} notes",
    )


def top_nav():
    links = [a(label, href=href, className="room-link") for href, label in ROOMS]
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
    if HOST.eclipse:
        sky = f"{HOST.eclipse_phase} eclipse"
    heat = f"{HOST.heat_remain}h" if HOST.firing else "hearth dark"
    notice = str(HOST.notice or "the house is listening")
    present = HOST.occupied[0] if HOST.occupied else "table"
    tide = str(HOST.tide_phase or "new")
    grain = HOST.sync_grain()
    ash = str(HOST.ash_grade or "fine")
    band = "peak" if HOST.firing and HOST.heat_remain <= 5 else (
        "warm" if HOST.firing else "idle"
    )
    return div(
        span(sky, className="inst-band"),
        span(clock_label(HOST.clock_h), className="inst-clock", aria_label="House clock"),
        span(f"tide {tide}", className="inst-tide"),
        span(f"grain {grain}", className="inst-grain"),
        span(f"ash {ash}", className="inst-ash"),
        span(heat, className="inst-heat"),
        span(present, className="inst-present"),
        resonance(band),
        tide_mark(tide),
        ash_mark(ash),
        staff_mark(),
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


def duet_cradle():
    """Companion cradle. Presence-continuous with /duet. DUET-1."""
    piece = HOST.duet
    if not piece:
        return a(
            span("duet empty", className="cradle-kicker"),
            href="/duet",
            className="cradle cradle-duet is-empty",
            aria_label="Empty companion cradle.",
            **{GET_CHROME_ATTR: True},
        )
    stage = str(piece.get("stage") or "drawn")
    clay = str(piece.get("clay") or "clay")
    return a(
        vessel_mark(piece, size=28, ident="cradle-duet"),
        span(
            span(clay, className="cradle-clay"),
            span(f"duet · {stage}", className="cradle-stage"),
            className="cradle-copy",
        ),
        href="/duet",
        className=f"cradle cradle-duet is-seated stage-{stage}",
        aria_label=f"Companion {clay} {stage}",
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
        p("APPIC · a house of making · ux-compose 0.1.0 · 80563ab · kit-81 · ash · grain · stamp · well"),
        p("GET is Clock A. Action is Clock B. Ash is remainder. Grain is clay. Caps are seals."),
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
        phase = str(HOST.eclipse_phase or "clear")
        tide = str(HOST.tide_phase or "new")
        grain = str(HOST.grain or "fine")
        ash = str(HOST.ash_grade or "fine")
        return document(
            div(
                top_nav(),
                instrument(),
                div(cradle(), duet_cradle(), className="cradles"),
                loop_rail(),
                main(node, id="stage", className="stage"),
                foot(),
                dock(),
                className="shell",
                data_brand=label,
                data_band=sky,
                data_firing="1" if HOST.firing else "0",
                data_stage=stage,
                data_eclipse="1" if HOST.eclipse else "0",
                data_phase=phase,
                data_tide=tide,
                data_grain=grain,
                data_ash=ash,
                **{GET_CHROME_ATTR: True},
            )
        )

    wrap.brand = label  # type: ignore[attr-defined]
    return wrap
