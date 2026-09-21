"""Page unit — coda.py → GET /coda.

The loop closes. Named close. morph_play toward the table.
stagger_in on #coda-*. CODA-1. Not a Pulse room.
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
    morph_play,
    notify,
    optional_slide,
    p,
    section,
    span,
    ul,
    update_with,
    scene,
    rise,
)
from store import CODAS, HOST

CLOSE_COPY = {
    "rest": "A rest on the staff. The house is still listening.",
    "return": "The loop names the table. Walking is Clock A.",
    "silence": "The last note is held. Occupancy thins. Phantom remains.",
}


class Coda(Component):
    id = "coda"
    close = MorphState("rest")
    dirty = MorphState("idle")

    def _plan(self):
        return scene("coda-close").stagger_in('[id^="coda-"]', rise.enter(ms=88), gap_ms=32)

    def render(self):
        HOST.occupy("coda")
        close = str(HOST.coda_close or self.close or "rest")
        if close not in CODAS:
            close = "rest"
        self.close = close
        keys = HOST.warp_keys()
        items = []
        for i, key in enumerate(keys):
            items.append(
                li(
                    span(f"{i + 1:02d}", className="warp-idx"),
                    span(key, className="warp-name"),
                    id=f"coda-{key}",
                    className="warp-thread is-on" if key == keys[-1] else "warp-thread",
                )
            )
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if close == key else "seg",
                **bind(self.name, close=key),
            )
            for key in CODAS
        ]
        return section(
            span("Coda", className="eyebrow"),
            h1("Close the loop.", className="display"),
            p(
                "Close is MorphState. The warp is Host stock. morph_play returns "
                "toward the table. stagger_in on #coda-*. XOR: no html= on the plan. "
                "The fugue hopped. The coda names rest.",
                className="lede",
            ),
            div(
                div(
                    span("warp", className="eyebrow"),
                    ul(*items, className="warp-list", id="coda-warp"),
                    className="paper",
                    id="coda-card",
                ),
                div(
                    span("close", className="eyebrow"),
                    h2(close, className="sight-title"),
                    p(CLOSE_COPY[close], className="sight-law"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Coda close"),
                    div(
                        button("Name return", type="button", className="btn-primary", **bind(self.name, close="return")),
                        button("Hold silence", type="button", className="btn-ghost", **bind(self.name, close="silence")),
                        a("Walk the table", href="/", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room coda-room",
            data_coda=close,
        )

    @action(caps=())
    def name(self, close: str = "rest"):
        named = HOST.name_coda(close)
        self.close = named
        mark_dirty(self)
        land = morph_play("#coda-card", optional_slide("coda", "#coda-card", direction="prev"))
        return update_with(self, self._plan(), extra_ops=list(land) + [notify(named)])
