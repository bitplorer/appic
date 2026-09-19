"""Page unit — cloth.py → GET /cloth.

The loop is warp. Occupancy is weft. Reorder is presence-continuous.
Not a Pulse room.
"""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    a,
    act,
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
    svg,
    path,
    ul,
    update_with,
    scene,
    rise,
)
from chrome import vessel_mark
from store import HOST, WARP_HREF


ORDERS = (("loop", "Loop"), ("alpha", "Alpha"), ("heat", "Heat"))


class Cloth(Component):
    id = "cloth"
    order = MorphState("loop")
    dirty = MorphState("idle")

    def _plan(self):
        return (
            scene("cloth-reorder")
            .stagger_in('[id^="warp-"]', rise.enter(ms=90), gap_ms=36)
        )

    def render(self):
        HOST.occupy("cloth")
        order = str(self.order or HOST.cloth_order or "loop")
        if order not in {k for k, _ in ORDERS}:
            order = "loop"
        HOST.cloth_order = order
        keys = HOST.warp_keys()
        present = set(HOST.occupied or [])
        piece = HOST.vessel
        segs = [
            button(
                label,
                type="button",
                className="seg is-on" if order == key else "seg",
                **bind(self.weave, order=key),
            )
            for key, label in ORDERS
        ]
        threads = []
        for i, key in enumerate(keys):
            on = key in present
            href = WARP_HREF.get(key, f"/{key}")
            threads.append(
                li(
                    span(f"{i + 1:02d}", className="warp-idx"),
                    span(key, className="warp-name"),
                    a("walk", href=href, className="warp-walk"),
                    id=f"warp-{key}",
                    className="warp-thread is-on" if on else "warp-thread",
                    data_station=key,
                )
            )
        weft = svg(
            path(
                d=HOST.weft_d(),
                fill="none",
                stroke="currentColor",
                stroke_width="1.4",
                stroke_linecap="round",
                className="wave-path",
            ),
            viewBox="0 0 240 36",
            preserveAspectRatio="none",
            className="wave weft",
            role="img",
            aria_label="Weft of occupancy across the warp",
        )
        seated = []
        if piece:
            seated = [
                div(
                    vessel_mark(piece, size=72, ident="cloth-vessel"),
                    span(
                        span(str(piece.get("clay") or "clay"), className="cradle-clay"),
                        span(str(piece.get("stage") or "drawn"), className="cradle-stage"),
                        className="cradle-copy",
                    ),
                    className="cloth-seat",
                    id="cloth-seat",
                )
            ]
        return section(
            span("Cloth", className="eyebrow"),
            h1("The loop is warp. Occupancy is weft.", className="display"),
            p(
                "Stations keep stable ids. Morph the cloth, then play a stagger "
                "on the surviving threads — objects that stay do not remount. "
                "XOR: the Plan carries no html=. bind() weaves. Caps stay off chrome.",
                className="lede",
            ),
            div(*segs, className="segs", role="radiogroup", aria_label="Warp order"),
            div(
                div(
                    span("warp", className="eyebrow"),
                    ul(*threads, className="warp", id="warp", role="list"),
                    className="paper cloth-warp",
                ),
                div(
                    span("weft", className="eyebrow"),
                    h2("A path, not a canvas.", className="sight-title"),
                    weft,
                    p(
                        "Sighted rooms cross the warp as weft. Heat-order lifts kiln and watch when the hearth is lit.",
                        className="sight-law",
                    ),
                    *seated,
                    div(
                        act("cloth.hold", "Hold the cloth", kind="primary", target="#cloth"),
                        a("Sit the chorus", href="/chorus", className="btn-ghost"),
                        a("Open the vessel", href="/vessel", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper cloth-weft",
                    id="cloth-weft",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room cloth-room",
            data_order=order,
        )

    @action(caps=())
    def weave(self, order: str = "loop"):
        keys = {k for k, _ in ORDERS}
        self.order = order if order in keys else "loop"
        HOST.cloth_order = str(self.order)
        mark_dirty(self)
        HOST.log("cloth.weave", str(self.order))
        HOST.notice = f"The warp is named {self.order}."
        return update_with(self, self._plan(), extra_ops=[notify(str(self.order))])

    @action(caps=())
    def hold(self):
        HOST.occupy("cloth")
        mark_dirty(self)
        HOST.notice = "The cloth is held."
        HOST.log("cloth.hold")
        plan = (
            scene("cloth-hold")
            .share("vessel", leave="#cloth-vessel", arrive="#cradle-vessel", recipe=rise.enter(ms=140))
            .enter("#cloth-weft", rise.enter(ms=160))
        )
        return update_with(self, plan, extra_ops=[notify("held")])
