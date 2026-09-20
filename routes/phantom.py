"""Page unit — phantom.py → GET /phantom.

Ghost occupancy. Unsighted warp fades. Named filter.
HOST.phantom is domain stock. Not a Pulse room.
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
    li,
    mark_dirty,
    notify,
    p,
    section,
    span,
    ul,
    update_with,
    scene,
    rise,
)
from store import HOST, PHANTOM_FILTERS, WARP_HREF

FILTER_COPY = {
    "all": "Warp and memory together. Present rooms hold; the rest are ghosts.",
    "ghost": "Only the unsighted. optional_fade on surviving #ghost-*.",
    "present": "Only occupancy. The weft as it is.",
}


class Phantom(Component):
    id = "phantom"
    which = MorphState("all")
    dirty = MorphState("idle")

    def _plan(self):
        return (
            scene("phantom")
            .stagger_in('[id^="ghost-"]', rise.enter(ms=80), gap_ms=32)
        )

    def render(self):
        HOST.occupy("phantom")
        which = str(self.which or "all")
        if which not in PHANTOM_FILTERS:
            which = "all"
        present = list(HOST.occupied or ["table"])
        ghosts = HOST.ghosts()
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if which == key else "seg",
                **bind(self.filter, which=key),
            )
            for key in PHANTOM_FILTERS
        ]
        shown = []
        if which in ("all", "present"):
            for name in present:
                shown.append(
                    li(
                        span("present", className="warp-idx"),
                        span(name, className="warp-name"),
                        a("walk", href=WARP_HREF.get(name, f"/{name}" if name != "table" else "/"), className="warp-walk"),
                        id=f"ghost-{name}",
                        className="warp-thread is-on",
                        data_station=name,
                    )
                )
        if which in ("all", "ghost"):
            for name in ghosts:
                shown.append(
                    li(
                        span("ghost", className="warp-idx"),
                        span(name, className="warp-name"),
                        a("walk", href=WARP_HREF.get(name, f"/{name}"), className="warp-walk"),
                        id=f"ghost-{name}",
                        className="warp-thread is-ghost",
                        data_station=name,
                    )
                )
        if not shown:
            shown = [
                li(
                    span("void", className="warp-idx"),
                    span("the house is empty", className="warp-name"),
                    id="ghost-void",
                    className="warp-thread",
                )
            ]
        return section(
            span("Phantom", className="eyebrow"),
            h1("Rooms you are not in.", className="display"),
            p(
                "Occupancy is weft. Phantom is the warp that occupancy left behind. "
                "Filter is MorphState. The list is Host stock. Morph, then fade the "
                "surviving ghosts. XOR: the Plan carries no html=. Not Pulse.",
                className="lede",
            ),
            div(
                div(
                    span("memory", className="eyebrow"),
                    ul(*shown, className="warp", id="phantom-list", role="list"),
                    className="paper cloth-warp",
                ),
                div(
                    span("filter", className="eyebrow"),
                    h2(which, className="sight-title"),
                    p(FILTER_COPY[which], className="sight-law"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Phantom filter"),
                    p(f"{len(ghosts)} ghosts. {len(present)} present.", className="muted"),
                    div(
                        a("Hold the cloth", href="/cloth", className="btn-primary"),
                        a("Hop the fugue", href="/fugue", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper",
                    id="phantom-card",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room phantom-room",
            data_filter=which,
        )

    @action(caps=())
    def filter(self, which: str = "all"):
        keys = set(PHANTOM_FILTERS)
        self.which = which if which in keys else "all"
        mark_dirty(self)
        HOST.log("phantom.filter", str(self.which))
        HOST.notice = f"The phantom is named {self.which}."
        return update_with(
            self,
            self._plan(),
            extra_ops=[notify(str(self.which))],
        )
