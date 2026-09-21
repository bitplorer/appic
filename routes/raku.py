"""Page unit — raku.py → GET /raku.

Sudden quench. Named reduction. morph_play hop. Heat dumps to ash.
data-raku on GET chrome. XOR: no html= on the plan.
RAKU-1. Not a Pulse room. Not /kiln.
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
    morph_play,
    notify,
    optional_slide,
    p,
    path,
    section,
    span,
    svg,
    update_with,
    scene,
    rise,
)
from chrome import vessel_mark
from store import HOST, RAKU_ATMS

ATM_COPY = {
    "oxidation": "Air is named. The copper will stay green. Heat still holds.",
    "reduction": "The chamber is starved. Smoke is a path. The copper will blush.",
    "post": "The quench is done. Ash is Host stock. The vessel is drawn.",
}


class Raku(Component):
    id = "raku"
    atm = MorphState("oxidation")
    dirty = MorphState("idle")

    def _plan(self, land: str):
        return (
            scene("raku-quench")
            .stagger_in('[id^="raku-"]', rise.enter(ms=70), gap_ms=24)
            .enter(f"#raku-{land}", rise.enter(ms=130))
        )

    def render(self):
        HOST.occupy("raku")
        atm = str(HOST.raku_atm or self.atm or "oxidation")
        if atm not in RAKU_ATMS:
            atm = "oxidation"
        self.atm = atm
        piece = HOST.vessel
        ash = int(HOST.ash or 0)
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if atm == key else "seg",
                **bind(self.name, atm=key),
            )
            for key in RAKU_ATMS
        ]
        stations = []
        for key in RAKU_ATMS:
            stations.append(
                div(
                    span(key, className="warp-name"),
                    id=f"raku-{key}",
                    className="warp-thread is-on" if key == atm else "warp-thread",
                    data_atm=key,
                )
            )
        seated = []
        if piece:
            seated = [
                vessel_mark(piece, size=88, ident="raku-vessel"),
                span(f"{piece.get('clay')} · {atm}", className="muted"),
            ]
        return section(
            span("Raku", className="eyebrow"),
            h1("Name the quench.", className="display"),
            p(
                "Atmosphere is MorphState. Ash is Host stock. morph_play hops the "
                "named reduction. Heat dumps. GET chrome carries data-raku. "
                "XOR: the Plan carries no html=. Not Pulse. Not the glaze kiln.",
                className="lede",
            ),
            div(
                div(
                    span("chamber", className="eyebrow"),
                    *seated,
                    svg(
                        path(
                            d="M20 90 Q40 20 60 90 T100 90 T140 90",
                            fill="none",
                            stroke="currentColor",
                            stroke_width="1.6",
                            stroke_linecap="round",
                            className="wave-path",
                        ),
                        viewBox="0 0 160 110",
                        className="raku-svg",
                        id="raku-smoke",
                        role="img",
                        aria_label=f"{atm} raku",
                    ),
                    p(f"{ash} ash on the hearth.", className="stat"),
                    className=f"paper raku-chamber atm-{atm}",
                    id="raku-card",
                ),
                div(
                    span("atmosphere", className="eyebrow"),
                    h2(atm, className="sight-title"),
                    p(ATM_COPY[atm], className="sight-law"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Raku atmosphere"),
                    div(*stations, className="warp-list"),
                    div(
                        button("Quench", type="button", className="btn-primary", **bind(self.quench)),
                        button("Name reduction", type="button", className="btn-ghost", **bind(self.name, atm="reduction")),
                        a("Keep the watch", href="/watch", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room raku-room",
            data_raku=atm,
        )

    @action(caps=())
    def name(self, atm: str = "reduction"):
        named = HOST.name_raku(atm)
        self.atm = named
        mark_dirty(self)
        return update_with(self, self._plan(named), extra_ops=[notify(named)])

    @action(caps=())
    def quench(self):
        named = HOST.quench()
        self.atm = named
        mark_dirty(self)
        land = morph_play("#raku-post", optional_slide("quench", "#raku-post", direction="next"))
        plan = self._plan(named)
        return update_with(self, plan, extra_ops=list(land) + [notify("quenched")])
