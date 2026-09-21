"""Page unit — wedge.py → GET /wedge.

The clay before the wheel. Named grain. Folds are RefState.
bind() kneads. Each fold is mark_dirty. stagger_in on #fold-*.
WEDGE-1. Not a Pulse room.
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
from store import GRAINS, HOST

GRAIN_COPY = {
    "fine": "Porcelain grain. The folds vanish. The lip will be thin.",
    "medium": "Stoneware grain. The fold holds. The body will stand.",
    "coarse": "Grog in the body. Heat will not crack the foot.",
}


class Wedge(Component):
    id = "wedge"
    grain = MorphState("medium")
    folds = RefState(0)
    dirty = MorphState("idle")

    def _plan(self):
        return scene("wedge-fold").stagger_in('[id^="fold-"]', rise.enter(ms=80), gap_ms=28)

    def render(self):
        HOST.occupy("wedge")
        grain = str(HOST.grain or self.grain or "medium")
        if grain not in GRAINS:
            grain = "medium"
        self.grain = grain
        n = int(HOST.fold_n or self.folds or 0)
        self.folds = n
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if grain == key else "seg",
                **bind(self.name, grain=key),
            )
            for key in GRAINS
        ]
        folds = [
            li(
                span(f"{i + 1:02d}", className="warp-idx"),
                span("fold", className="warp-name"),
                id=f"fold-{i + 1}",
                className="warp-thread is-on" if i == n - 1 else "warp-thread",
            )
            for i in range(max(n, 1))
        ]
        return section(
            span("Wedge", className="eyebrow"),
            h1("Knead the clay.", className="display"),
            p(
                "Grain is MorphState. Folds are RefState — Channel refuses quantity "
                "on the session plane. bind() kneads. Each fold is mark_dirty. "
                "stagger_in on #fold-*. The clay before the wheel. Not Pulse.",
                className="lede",
            ),
            div(
                div(
                    span("grain", className="eyebrow"),
                    h2(grain, className="sight-title"),
                    p(GRAIN_COPY[grain], className="sight-law"),
                    p(f"{n} folds on the cloth.", className="stat"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Grain"),
                    div(
                        button("Knead", type="button", className="btn-primary", **bind(self.knead)),
                        button("Name fine grain", type="button", className="btn-ghost", **bind(self.name, grain="fine")),
                        a("Walk the wheel", href="/wheel", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper",
                    id="wedge-card",
                ),
                div(
                    span("folds", className="eyebrow"),
                    ul(*folds, className="warp-list", id="wedge-folds"),
                    p("Presence-continuous folds. Surviving ids do not remount.", className="muted"),
                    className="paper",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room wedge-room",
            data_grain=grain,
        )

    @action(caps=())
    def name(self, grain: str = "medium"):
        named = HOST.name_grain(grain)
        self.grain = named
        mark_dirty(self)
        return update_with(self, self._plan(), extra_ops=[notify(named)])

    @action(caps=())
    def knead(self):
        n = HOST.knead()
        self.folds = n
        mark_dirty(self)
        return update_with(self, self._plan(), extra_ops=[notify(f"fold {n}")])
