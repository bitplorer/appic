"""Page unit — chorus.py → GET /chorus.

Concurrent hands. Named order. Presence cookbook stagger_in. CHORUS-1.
Voices are Host stock (named keys). Order is MorphState.
"""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    a,
    action,
    button,
    control,
    div,
    h1,
    h2,
    li,
    mark_dirty,
    notify,
    p,
    section,
    span,
    ul,
    update_with,
    rise,
    scene,
)
from store import CHORUS_ORDERS, HOST, VOICES


def _ordered(voices: list[str], order: str) -> list[str]:
    rows = list(voices or VOICES)
    if order == "fall":
        return list(reversed(rows))
    if order == "pulse":
        if len(rows) > 1:
            return rows[1:] + rows[:1]
        return rows
    return rows


class Chorus(Component):
    id = "chorus"
    order = MorphState("rise")
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("chorus")
        order = str(self.order or "rise")
        if order not in CHORUS_ORDERS:
            order = "rise"
        voices = _ordered(list(HOST.voices or VOICES), order)
        cards = [
            li(
                span(name, className="voice-name"),
                span(f"{i + 1:02d}", className="voice-idx"),
                p(
                    {
                        "wheel": "The left hand. RPM is a private magnitude.",
                        "glaze": "Oxide named. Load is silent.",
                        "kiln": "Shared hearth. Heat is Host stock.",
                        "watch": "The night sits with the fire.",
                    }.get(name, "A named hand."),
                    className="muted",
                ),
                id=f"voice-{name}",
                className=f"voice-card voice-{name}",
            )
            for i, name in enumerate(voices)
        ]
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if order == key else "seg",
                **control("chorus.sort", order=key),
            )
            for key in CHORUS_ORDERS
        ]
        return section(
            span("Chorus", className="eyebrow"),
            h1("More than one hand on the wheel.", className="display"),
            p(
                "Order is MorphState (rise | fall | pulse). Voices are Host stock. "
                "Stable ids #voice-{name} are presence. Morph-then-Play staggers "
                "the surviving nodes. Objects that stay do not remount.",
                className="lede",
            ),
            div(
                span("order", className="eyebrow"),
                h2(order, className="sight-title"),
                p("Rise is the foundry loop. Fall reverses it. Pulse rotates the first voice to the end.", className="sight-law"),
                div(*segs, className="segs", role="radiogroup", aria_label="Chorus order"),
                div(
                    button("Lift the chorus", type="button", className="btn-primary", **control("chorus.lift")),
                    a("Walk the score", href="/score", className="btn-ghost"),
                    a("Walk the duet", href="/duet", className="btn-ghost"),
                    className="hero-actions",
                ),
                className="paper",
                id="chorus-card",
            ),
            ul(*cards, className="chorus-row", id="chorus-list", aria_label="Concurrent voices"),
            id=self.id,
            className="room chorus-room",
            data_order=order,
        )

    def _plan(self):
        voices = _ordered(list(HOST.voices or VOICES), str(self.order or "rise"))
        return scene("chorus-reorder").stagger_in(
            [f"#voice-{name}" for name in voices],
            rise.enter(ms=110),
            gap_ms=48,
        )

    @action(caps=())
    def sort(self, order: str = "rise"):
        self.order = order if order in CHORUS_ORDERS else "rise"
        HOST.chorus_order = str(self.order)
        HOST.log("chorus.order", str(self.order))
        HOST.score_write("chorus.sort", "chorus", "D")
        mark_dirty(self)
        return update_with(self, self._plan(), extra_ops=[notify(str(self.order))])

    @action(caps=())
    def lift(self):
        order = str(self.order or "rise")
        HOST.voices = _ordered(list(HOST.voices or VOICES), "pulse" if order != "pulse" else order)
        HOST.chorus_order = order
        HOST.notice = "The chorus lifted."
        HOST.log("chorus.lift", order)
        HOST.score_write("chorus.lift", "chorus", "A")
        mark_dirty(self)
        return update_with(self, self._plan(), extra_ops=[notify("lift")])
