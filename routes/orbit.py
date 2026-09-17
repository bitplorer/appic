"""Page unit — orbit.py → GET /orbit.

Firing as time. Named window is MorphState. Remaining hours are RefState.
Calendar + countdown + timeline as one inhabited room — not three kit demos.
"""
from __future__ import annotations

import math

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    button,
    circle,
    control,
    div,
    h1,
    h2,
    li,
    mark_dirty,
    notify,
    optional_plan,
    p,
    section,
    span,
    svg,
    ul,
    update_with,
    a,
)
from store import HOST

WINDOWS = (
    ("today", "Today", "The shelf is this afternoon."),
    ("next", "Next fire", "A window two nights out."),
    ("soak", "Soak", "The glaze is still. Hold."),
    ("drawn", "Drawn", "The orbit closed. Walk the vitrine."),
)
DAYS = (
    ("mon", "Mon"),
    ("tue", "Tue"),
    ("wed", "Wed"),
    ("thu", "Thu"),
    ("fri", "Fri"),
    ("sat", "Sat"),
    ("sun", "Sun"),
)


class Orbit(Component):
    id = "orbit"
    window = MorphState("today")
    day = MorphState("thu")
    remain = RefState(14)
    dirty = MorphState("idle")

    def _n(self) -> int:
        try:
            return max(0, min(72, int(self.remain or 0)))
        except (TypeError, ValueError):
            return 0

    def _row(self):
        key = str(self.window or "today")
        for row in WINDOWS:
            if row[0] == key:
                return row
        return WINDOWS[0]

    def render(self):
        key, title, law = self._row()
        n = self._n()
        day = str(self.day or "thu")
        stock = (HOST.thrown[-6:] + HOST.vitrine[-6:])[-8:]
        dots = []
        for i, piece in enumerate(stock or [{"id": "empty", "clay": "empty shelf"}]):
            ang = (i / max(1, len(stock) or 1)) * 6.2832
            cx = 80 + int(52 * math.cos(ang - 1.57))
            cy = 80 + int(52 * math.sin(ang - 1.57))
            dots.append(
                circle(
                    cx=str(cx),
                    cy=str(cy),
                    r="4.5",
                    fill="currentColor",
                    className="orbit-dot",
                )
            )
        chips = [
            button(
                label,
                type="button",
                className="choice is-on" if self.window == k else "choice",
                **control("orbit.aim", window=k),
            )
            for k, label, _law in WINDOWS
        ]
        days = [
            button(
                label,
                type="button",
                className="seg is-on" if day == k else "seg",
                **control("orbit.sit", day=k),
            )
            for k, label in DAYS
        ]
        hours = [
            button(
                lab,
                type="button",
                className="choice is-on" if n == val else "choice",
                **control("orbit.wait", hours=str(val)),
            )
            for val, lab in ((4, "4h"), (14, "14h"), (28, "28h"), (48, "48h"))
        ]
        trail = [
            li(
                span(row.get("at", ""), className="mono"),
                span(row.get("verb", ""), className="card-title"),
                span(row.get("detail", ""), className="muted"),
                className="hand-line",
            )
            for row in list(reversed(HOST.ledger[-8:]))
        ] or [li(span("The orbit is quiet.", className="muted"), className="hand-line")]
        return section(
            span("Orbit", className="eyebrow"),
            h1("A firing is a window, not a clock face.", className="display"),
            p(
                "The window and the weekday are named MorphState. "
                "Remaining hours are RefState. Pieces live on the Host, never the client plane.",
                className="lede",
            ),
            div(
                div(
                    span("sky", className="eyebrow"),
                    svg(
                        circle(cx="80", cy="80", r="52", fill="none", stroke="currentColor", stroke_width="0.7", className="orbit-ring"),
                        circle(cx="80", cy="80", r="6", fill="currentColor", className="air-core"),
                        *dots,
                        viewBox="0 0 160 160",
                        className="air-svg",
                        aria_hidden="true",
                    ),
                    p(title, className="hearth-piece"),
                    p(f"{n}h", className="stat", role="timer", aria_live="polite"),
                    p(f"{day} · {len(stock)} on the ring", className="muted"),
                    className=f"hearth orbit-chamber win-{key}",
                    data_window=key,
                    id="orbit-sky",
                ),
                div(
                    span("window", className="eyebrow"),
                    h2(title, className="sight-title"),
                    p(law, className="sight-law"),
                    div(*chips, className="choices", role="radiogroup", aria_label="Firing window"),
                    span("weekday", className="eyebrow"),
                    div(*days, className="segs", role="radiogroup", aria_label="Weekday"),
                    span("remaining", className="eyebrow"),
                    div(*hours, className="choices", role="radiogroup", aria_label="Hours remaining"),
                    div(
                        a("Walk the kiln", href="/kiln", className="btn-primary"),
                        a("File a brief", href="/brief", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper",
                    id="orbit-card",
                ),
                className="kiln-split",
            ),
            div(
                span("trail", className="eyebrow"),
                ul(*trail, className="hands-log", role="list"),
                className="paper",
            ),
            id=self.id,
            className="room",
        )

    @action(caps=())
    def aim(self, window: str = "today"):
        keys = {row[0] for row in WINDOWS}
        self.window = window if window in keys else "today"
        HOST.window = str(self.window)
        HOST.log("orbit.aim", str(self.window))
        mark_dirty(self)
        return update_with(
            self,
            optional_plan("window", "#orbit-sky"),
            extra_ops=[notify(str(self.window))],
        )

    @action(caps=())
    def sit(self, day: str = "thu"):
        keys = {k for k, _ in DAYS}
        self.day = day if day in keys else "thu"
        HOST.day = str(self.day)
        HOST.log("orbit.sit", str(self.day))
        mark_dirty(self)
        return update_with(self, extra_ops=[notify(str(self.day))])

    @action(caps=())
    def wait(self, hours: str = "14"):
        try:
            n = int(hours)
        except (TypeError, ValueError):
            n = 14
        self.remain = max(0, min(72, n))
        HOST.remain_h = int(self.remain)
        HOST.log("orbit.wait", str(self.remain))
        mark_dirty(self)
        return update_with(self, extra_ops=[notify(f"{self.remain}h")])
