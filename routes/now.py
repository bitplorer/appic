"""Page unit — now.py → GET /now. Living instrument of the house.

Clock, occupancy, heat trace, resonance. Not a Pulse room.
"""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    a,
    act,
    action,
    button,
    control,
    div,
    dl,
    dt,
    dd,
    h1,
    h2,
    li,
    mark_dirty,
    notify,
    optional_plan,
    p,
    progress,
    rect,
    section,
    span,
    svg,
    ul,
    update_with,
)
from chrome import resonance
from store import HOST, BANDS, clock_label, band_for_hour, band_for_hour


class Now(Component):
    id = "now"
    hour = MorphState("dawn")
    remain = RefState(0)
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("now")
        sky = HOST.sync_sky()
        kpi = HOST.kpi()
        n = int(HOST.heat_remain) if HOST.firing else 0
        pct = 0 if not HOST.firing else max(0, min(100, int(((12 - n) / 12) * 100)))
        band = "idle"
        if HOST.firing:
            if n <= 2:
                band = "cool"
            elif n <= 5:
                band = "peak"
            elif n <= 8:
                band = "soak"
            else:
                band = "warm"
        trace = list(HOST.heat_trace or [0])
        mx = max(trace) or 1
        bars = []
        width = max(4, int(220 / max(len(trace), 1)) - 2)
        for i, val in enumerate(trace[-16:]):
            h = max(2, int((int(val) / mx) * 48))
            bars.append(
                rect(
                    x=str(i * (width + 2)),
                    y=str(52 - h),
                    width=str(width),
                    height=str(h),
                    rx="2",
                    className="chart-bar is-on" if i == len(trace[-16:]) - 1 else "chart-bar",
                )
            )
        present = [li(name, className="chip") for name in (HOST.occupied or ["now"])]
        events = [
            li(
                span(row.get("at", ""), className="tiny mono"),
                span(str(row.get("verb", "")), className="hand-line-verb"),
                span(str(row.get("detail", "")), className="muted"),
                className="hand-line",
            )
            for row in reversed(HOST.ledger[-8:])
        ] or [li("The house has not spoken yet.", className="hand-line")]
        hours = [
            button(
                label,
                type="button",
                className="seg is-on" if sky == key else "seg",
                **control("now.shift", band=key),
            )
            for key, label in (("night", "Night"), ("dawn", "Dawn"), ("noon", "Noon"), ("dusk", "Dusk"))
        ]
        return section(
            span("Now", className="eyebrow"),
            h1("The house, as it is.", className="display"),
            p(
                "The clock is Host stock. Sky follows the hour unless you name a band. "
                "Occupancy is a short memory of sighted rooms. Resonance is the hearth "
                "made audible as a path. This is not a Pulse room.",
                className="lede",
            ),
            div(
                div(
                    span("instrument", className="eyebrow"),
                    p(clock_label(HOST.clock_h), className="stat", aria_label="House clock"),
                    p(f"{sky} · auto {'on' if HOST.auto_sky else 'off'}", className="hearth-piece"),
                    resonance(band),
                    p(
                        "The kiln is holding." if HOST.firing else "The hearth is dark.",
                        className="muted",
                    ),
                    progress(
                        value=str(pct),
                        max="100",
                        className="fire-bar",
                        role="progressbar",
                        aria_valuemin="0",
                        aria_valuemax="100",
                        aria_valuenow=str(pct),
                        aria_label="Firing progress",
                    ),
                    div(*hours, className="segs", role="radiogroup", aria_label="Sky band"),
                    div(
                        act("now.tick_clock", "Advance the hour", kind="primary", target="#now"),
                        act("now.follow", "Follow the sun", kind="ghost", target="#now"),
                        a("Sit the watch", href="/watch", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className=f"hearth band-{band} {'is-lit' if HOST.firing else 'is-dark'}",
                    id="now-bell",
                ),
                div(
                    span("stock", className="eyebrow"),
                    h2("What the house is holding", className="sight-title"),
                    dl(
                        dt("Pulse"),
                        dd(str(kpi["pulse"])),
                        dt("Heat"),
                        dd(str(kpi["heat"])),
                        dt("Thrown"),
                        dd(str(kpi["thrown"])),
                        dt("Drawn"),
                        dd(str(kpi["drawn"])),
                        dt("Joins"),
                        dd(str(kpi.get("joins", 0))),
                        dt("Gifts"),
                        dd(str(kpi.get("gifts", 0))),
                        className="kpi",
                    ),
                    span("heat trace", className="eyebrow"),
                    svg(
                        *bars,
                        viewBox="0 0 220 56",
                        className="trace-svg",
                        role="img",
                        aria_label="Heat remaining over ticks",
                    ),
                    span("present", className="eyebrow"),
                    ul(*present, className="chips", aria_label="Recent occupancy"),
                    span("ledger", className="eyebrow"),
                    ul(*events, className="hands-log", role="log", aria_label="House ledger"),
                    className="paper",
                    id="now-card",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room now-room",
            data_band=sky,
        )

    @action(caps=())
    def shift(self, band: str = "night"):
        if band not in BANDS:
            band = "night"
        HOST.auto_sky = False
        HOST.sky_band = band
        self.hour = band
        mark_dirty(self)
        HOST.log("now.band", band)
        HOST.notice = f"The house is named {band}."
        return update_with(self, optional_plan("now", "#now"), extra_ops=[notify(band)])

    @action(caps=())
    def tick_clock(self):
        HOST.auto_sky = True
        sky = HOST.tick_clock()
        self.hour = sky
        mark_dirty(self)
        HOST.log("now.clock", clock_label(HOST.clock_h))
        HOST.notice = f"{clock_label(HOST.clock_h)} · {sky}"
        return update_with(self, extra_ops=[notify(sky)])

    @action(caps=())
    def follow(self):
        HOST.auto_sky = True
        from store import ist_hour

        HOST.clock_h = ist_hour()
        sky = HOST.sync_sky()
        self.hour = sky
        mark_dirty(self)
        HOST.log("now.follow", sky)
        HOST.notice = f"Following the sun · {sky}"
        return update_with(self, extra_ops=[notify(sky)])
