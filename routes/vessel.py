"""Page unit — vessel.py → GET /vessel.

The piece as a room. Named stage. Host stock. Presence-continuous with the
cradle (same #cradle-vessel identity via scene.share). Not a Pulse room.
"""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    a,
    act,
    action,
    button,
    control,
    div,
    dl,
    dt,
    dd,
    h1,
    h2,
    mark_dirty,
    notify,
    p,
    section,
    span,
    update_with,
    scene,
    rise,
)
from chrome import vessel_mark
from store import HOST, STAGES


class Vessel(Component):
    id = "vessel"
    stage = MorphState("drawn")
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("vessel")
        piece = HOST.vessel
        if not piece:
            return section(
                span("Vessel", className="eyebrow"),
                h1("Nothing sits on the cloth.", className="display"),
                p(
                    "The vessel is an inhabitant, not a byproduct. "
                    "File a brief, throw a body, or draw from the kiln. "
                    "When it sits, the cradle in chrome keeps it — objects that stay do not remount.",
                    className="lede",
                ),
                div(
                    a("File a brief", href="/brief", className="btn-primary"),
                    a("Throw a body", href="/wheel", className="btn-ghost"),
                    a("Walk the vitrine", href="/vitrine", className="btn-ghost"),
                    className="hero-actions",
                ),
                id=self.id,
                className="room emptystate vessel-room",
            )
        stage = str(piece.get("stage") or "drawn")
        clay = str(piece.get("clay") or "clay")
        glaze = str(piece.get("glaze") or "glaze")
        note = str(piece.get("note") or "Seated on the cloth.")
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if stage == key else "seg",
                **control("vessel.name", stage=key),
            )
            for key in STAGES
            if key != "gifted"
        ]
        return section(
            span("Vessel", className="eyebrow"),
            h1("The piece is the house.", className="display"),
            p(
                "Named stage on MorphState. The body is Host stock. "
                "The cradle in GET chrome shares this presence — walk the loop and it does not remount. "
                "Brass is the join. Gift is how it leaves.",
                className="lede",
            ),
            div(
                div(
                    span("on the cloth", className="eyebrow"),
                    vessel_mark(piece, size=180, ident="vessel-body"),
                    p(f"{clay} · {glaze}", className="hearth-piece"),
                    p(note, className="muted"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Named stage"),
                    div(
                        act("vessel.hold", "Hold the cloth", kind="primary", target="#vessel"),
                        a("Mend a break", href="/kintsugi", className="btn-ghost"),
                        a("Send it", href="/gift", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className=f"hearth vessel-chamber stage-{stage}",
                    id="vessel-chamber",
                ),
                div(
                    span("stock", className="eyebrow"),
                    h2(str(piece.get("id") or "—"), className="sight-title"),
                    dl(
                        dt("Stage"),
                        dd(stage),
                        dt("Clay"),
                        dd(clay),
                        dt("Glaze"),
                        dd(glaze),
                        dt("Join"),
                        dd(str(piece.get("join") or "whole")),
                        dt("Joins spent"),
                        dd(str(HOST.join_n)),
                        className="kpi",
                    ),
                    p(
                        "Presence identity is the piece id. Morph the chamber, then play. "
                        "XOR: the plan carries no html=.",
                        className="sight-law",
                    ),
                    className="paper",
                    id="vessel-card",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room vessel-room",
            data_stage=stage,
        )

    @action(caps=())
    def name(self, stage: str = "drawn"):
        if stage not in STAGES or stage == "gifted":
            stage = "drawn"
        self.stage = stage
        if HOST.vessel:
            HOST.seat(stage=stage)
        mark_dirty(self)
        HOST.log("vessel.stage", stage)
        HOST.notice = f"The vessel is named {stage}."
        plan = (
            scene("vessel-name")
            .share("vessel", leave="#vessel-body", arrive="#cradle-vessel", recipe=rise.enter(ms=140))
            .enter("#vessel-chamber", rise.enter(ms=160))
        )
        return update_with(self, plan, extra_ops=[notify(stage)])

    @action(caps=())
    def hold(self):
        HOST.occupy("vessel")
        mark_dirty(self)
        HOST.notice = "The cloth is held."
        HOST.log("vessel.hold")
        return update_with(self, extra_ops=[notify("held")])
