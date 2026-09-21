"""Page unit — well.py → GET /well.

Water as a verb. Tide is climate; the well is the draw.
Owned PullRefresh, shell=False. WELL-1. Not Pulse. Not /pullrefresh.
"""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    a,
    action,
    bind,
    button,
    div,
    h1,
    h2,
    mark_dirty,
    notify,
    optional_slide,
    p,
    path,
    section,
    span,
    svg,
    update_with,
)
from components.pullrefresh import PullRefresh
from store import DRAWS, HOST, well_d

DRAW_COPY = {
    "sip": "A finger of water. The hearth cools one hour.",
    "scoop": "A bowl. Occupancy remembers the well.",
    "flood": "The cloth drinks. Tide names itself full.",
}


class WellDraw(PullRefresh):
    """Owned copy. shell=False. SEED is the well log."""

    id = "welldraw"
    SEED = (
        "A sip from the night well.",
        "The cloth drank.",
        "Ash cooled in the bowl.",
    )
    MORE = (
        "Grog settled.",
        "The chop was rinsed.",
        "A filament brightened.",
        "The cradle took water.",
    )

    def on_refresh(self):
        HOST.draw_well("sip")
        have = list(self.items or self.SEED)
        line = HOST.well_log[0] if HOST.well_log else "A draw crossed the cloth."
        return tuple([line] + [x for x in have if x != line])[:8]


class Well(Component):
    id = "well"
    draw = MorphState("sip")
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("well")
        draw = str(self.draw or "sip")
        if draw not in DRAWS:
            draw = "sip"
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if draw == key else "seg",
                **bind(self.name, draw=key),
            )
            for key in DRAWS
        ]
        feed = WellDraw()
        feed.items = tuple(HOST.well_log[:8]) if HOST.well_log else None
        return section(
            span("Well", className="eyebrow"),
            h1("Draw the water.", className="display"),
            p(
                "Tide is lunar climate. The well is the verb. Named draw on MorphState. "
                "PullRefresh is an owned copy, shell=False, restyled onto APPIC tokens. "
                "Swipe down or tap. A flood names a full tide. Not /pullrefresh. Not Pulse.",
                className="lede",
            ),
            div(
                div(
                    span("mouth", className="eyebrow"),
                    svg(
                        path(
                            d="M20 18 C20 18 60 8 100 18 C100 58 80 92 60 102 C40 92 20 58 20 18 Z",
                            fill="none",
                            stroke="currentColor",
                            stroke_width="1.5",
                            className="well-rim",
                        ),
                        path(
                            d=well_d(draw),
                            fill="none",
                            stroke="currentColor",
                            stroke_width="1.4",
                            stroke_linecap="round",
                            className="wave-path",
                        ),
                        viewBox="0 0 120 120",
                        className="eclipse-svg well-svg",
                        id="well-disk",
                        role="img",
                        aria_label=f"{draw} well",
                    ),
                    p(f"{len(HOST.well_log)} draws.", className="stat"),
                    p(f"tide {HOST.tide_phase}", className="muted"),
                    className=f"paper eclipse-chamber draw-{draw}",
                    id="well-card",
                ),
                div(
                    span("draw", className="eyebrow"),
                    h2(draw, className="sight-title"),
                    p(DRAW_COPY[draw], className="sight-law"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Well draw"),
                    div(
                        button("Draw from the well", type="button", className="btn-primary", **bind(self.take)),
                        a("Name the tide", href="/tide", className="btn-ghost"),
                        a("Rake the ash", href="/ash", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper",
                    id="well-panel",
                ),
                className="kiln-split",
            ),
            feed.render(shell=False),
            id=self.id,
            className="room well-room",
            data_draw=draw,
        )

    @action(caps=())
    def name(self, draw: str = "sip"):
        if draw not in DRAWS:
            draw = "sip"
        self.draw = draw
        mark_dirty(self)
        HOST.log("well.draw", draw)
        return update_with(self, extra_ops=[notify(draw)])

    @action(caps=())
    def take(self):
        draw = str(self.draw or "sip")
        HOST.draw_well(draw)
        mark_dirty(self)
        return update_with(
            self,
            optional_slide("well", "#well-card", direction="next"),
            extra_ops=[notify(draw)],
        )
