"""Page unit — duet.py → GET /duet.

Two vessels. Two cradles. scene.share XOR. DUET-1.
The companion is Host stock. Pass moves presence from #vessel-a to #cradle-duet.
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
    mark_dirty,
    notify,
    p,
    section,
    span,
    update_with,
    rise,
    scene,
)
from chrome import vessel_mark
from store import HOST, STAGES


class Duet(Component):
    id = "duet"
    stage = MorphState("thrown")
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("duet")
        left = HOST.vessel
        right = HOST.duet
        stage = str(self.stage or (right or {}).get("stage") or "thrown")
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if stage == key else "seg",
                **control("duet.name", stage=key),
            )
            for key in STAGES
            if key != "gifted"
        ]
        left_body = (
            div(
                vessel_mark(left, size=88, ident="vessel-a"),
                span(str((left or {}).get("clay") or "empty"), className="eyebrow"),
                p(str((left or {}).get("glaze") or "the cloth is bare"), className="muted"),
                className="duet-hand",
                id="duet-left",
            )
            if left
            else div(
                span("cloth empty", className="eyebrow"),
                p("Seat a vessel first.", className="muted"),
                a("Walk the vessel", href="/vessel", className="btn-ghost"),
                className="duet-hand is-empty",
                id="duet-left",
            )
        )
        right_body = (
            div(
                vessel_mark(right, size=88, ident="vessel-b"),
                span(str((right or {}).get("clay") or "empty"), className="eyebrow"),
                p(str((right or {}).get("note") or "the other hand"), className="muted"),
                className="duet-hand",
                id="duet-right",
            )
            if right
            else div(
                span("companion empty", className="eyebrow"),
                p("Pass the cloth, or seat a companion.", className="muted"),
                className="duet-hand is-empty",
                id="duet-right",
            )
        )
        return section(
            span("Duet", className="eyebrow"),
            h1("Two hands. One presence.", className="display"),
            p(
                "The companion vessel is Host stock. Named stage is MorphState. "
                "Pass is scene.share from #vessel-a to #cradle-duet. XOR: the Plan "
                "carries no html=. Objects that stay do not remount.",
                className="lede",
            ),
            div(left_body, right_body, className="duet-pair", id="duet-pair"),
            div(
                span("companion stage", className="eyebrow"),
                h2(stage, className="sight-title"),
                p("Name the companion, then pass the cloth. The second cradle in chrome keeps it.", className="sight-law"),
                div(*segs, className="segs", role="radiogroup", aria_label="Companion stage"),
                div(
                    button("Pass to the companion", type="button", className="btn-primary", **control("duet.cross")),
                    button("Seat a companion", type="button", className="btn-ghost", **control("duet.seat")),
                    a("Walk the chorus", href="/chorus", className="btn-ghost"),
                    className="hero-actions",
                ),
                className="paper",
                id="duet-card",
            ),
            id=self.id,
            className="room duet-room",
            data_stage=stage,
        )

    @action(caps=())
    def name(self, stage: str = "thrown"):
        self.stage = stage if stage in STAGES else "thrown"
        if HOST.duet:
            HOST.duet["stage"] = str(self.stage)
        mark_dirty(self)
        HOST.log("duet.stage", str(self.stage))
        return update_with(self, extra_ops=[notify(str(self.stage))])

    @action(caps=())
    def seat(self):
        HOST.seat_duet(stage=str(self.stage or "thrown"))
        HOST.notice = "A companion sat down."
        HOST.log("duet.seat", str((HOST.duet or {}).get("id")))
        HOST.score_write("duet.seat", "duet", "F")
        mark_dirty(self)
        return update_with(self, extra_ops=[notify("seated")])

    @action(caps=())
    def cross(self):
        row = HOST.pass_duet()
        if not row:
            return update_with(self, extra_ops=[notify("empty cloth")])
        mark_dirty(self)
        plan = (
            scene("duet-pass")
            .share("vessel", leave="#vessel-a", arrive="#cradle-duet", recipe=rise.enter(ms=140))
            .enter("#duet-right", rise.enter(ms=160))
        )
        return update_with(self, plan, extra_ops=[notify("passed")])
