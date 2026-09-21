"""Page unit — bisque.py → GET /bisque.

First fire. Named biscuit. Remaining is RefState.
optional_plan on #bisque-kiln. Shared hearth, cooler than glaze fire.
BISQUE-1. Not a Pulse room. Not /kiln.
"""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    a,
    action,
    bind,
    button,
    div,
    h1,
    h2,
    mark_dirty,
    notify,
    optional_plan,
    p,
    section,
    span,
    update_with,
)
from store import BISCUITS, HOST

BISCUIT_COPY = {
    "bone": "The body is still pale. Water has left. The glaze will drink.",
    "cream": "The biscuit is named. Heat is quieter than a glaze fire.",
    "toast": "The foot is set. Walk the glaze while the body is thirsty.",
}


class Bisque(Component):
    id = "bisque"
    biscuit = MorphState("bone")
    remain = RefState(0)
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("bisque")
        biscuit = str(HOST.biscuit or self.biscuit or "bone")
        if biscuit not in BISCUITS:
            biscuit = "bone"
        self.biscuit = biscuit
        remain = int(HOST.bisque_remain or self.remain or 0)
        self.remain = remain
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if biscuit == key else "seg",
                **bind(self.name, biscuit=key),
            )
            for key in BISCUITS
        ]
        band = "warm" if remain > 4 else ("peak" if remain > 0 else "idle")
        return section(
            span("Bisque", className="eyebrow"),
            h1("First fire.", className="display"),
            p(
                "Biscuit is MorphState. Remaining hours are RefState. "
                "This is not the glaze kiln. Heat is the shared hearth, cooler. "
                "optional_plan on #bisque-kiln. XOR: the Plan carries no html=.",
                className="lede",
            ),
            div(
                div(
                    span("hearth", className="eyebrow"),
                    div(
                        span("", className="heat-ring r1"),
                        span("", className="heat-ring r2"),
                        span("", className="heat-ring r3"),
                        span(f"{remain}h", className="ember"),
                        className=f"watch-hearth hearth band-{band}",
                        id="bisque-kiln",
                    ),
                    p(f"{remain} hours on the biscuit.", className="stat"),
                    className=f"paper hearth-card band-{band}",
                ),
                div(
                    span("biscuit", className="eyebrow"),
                    h2(biscuit, className="sight-title"),
                    p(BISCUIT_COPY[biscuit], className="sight-law"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Biscuit"),
                    div(
                        button("Light the biscuit", type="button", className="btn-primary", **bind(self.light)),
                        button("Advance heat", type="button", className="btn-ghost", **bind(self.tick)),
                        a("Walk the glaze", href="/glaze", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper",
                    id="bisque-card",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room bisque-room",
            data_biscuit=biscuit,
        )

    @action(caps=())
    def name(self, biscuit: str = "cream"):
        named = HOST.name_biscuit(biscuit)
        self.biscuit = named
        mark_dirty(self)
        return update_with(self, optional_plan("biscuit", "#bisque-card"), extra_ops=[notify(named)])

    @action(caps=())
    def light(self):
        remain = HOST.light_bisque()
        self.remain = remain
        mark_dirty(self)
        return update_with(self, optional_plan("bisque-light", "#bisque-kiln"), extra_ops=[notify("bisque lit")])

    @action(caps=())
    def tick(self):
        remain = HOST.tick_bisque()
        self.remain = remain
        mark_dirty(self)
        return update_with(self, optional_plan("bisque-tick", "#bisque-kiln"), extra_ops=[notify(f"{remain}h")])
