"""Page unit — kintsugi.py → GET /kintsugi.

Mend a drawn vessel. Named break. Brass is the join. Repair spends repair.join.
Presence-continuous with the cradle. Not a Pulse room. Not the kit tree demo.
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
    scene,
    rise,
)
from chrome import vessel_mark
from store import HOST, BREAKS


class Kintsugi(Component):
    id = "kintsugi"
    where = MorphState("belly")
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("kintsugi")
        piece = HOST.vessel
        if not piece:
            return section(
                span("Kintsugi", className="eyebrow"),
                h1("Nothing to mend.", className="display"),
                p(
                    "A join needs a vessel. Draw from the kiln, then name the break. "
                    "Brass is the only accent — it is also the repair.",
                    className="lede",
                ),
                div(
                    a("Seat a vessel", href="/vessel", className="btn-primary"),
                    a("Walk the kiln", href="/kiln", className="btn-ghost"),
                    className="hero-actions",
                ),
                id=self.id,
                className="room emptystate kintsugi-room",
            )
        where = str(self.where or piece.get("break") or "belly")
        join = str(piece.get("join") or "")
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if where == key else "seg",
                **control("kintsugi.name", where=key),
            )
            for key in BREAKS
        ]
        repairs = [
            div(
                span(str(row.get("at", "")), className="tiny mono"),
                span(str(row.get("join", "")), className="card-title"),
                span(str(row.get("clay", "")), className="muted"),
                className="cap-row",
            )
            for row in reversed(HOST.repairs[-5:])
        ] or [p("No joins yet.", className="muted")]
        return section(
            span("Kintsugi", className="eyebrow"),
            h1("Brass holds what fire kept.", className="display"),
            p(
                "A named break (lip, belly, foot). The join is Host stock. "
                "Mend spends repair.join. The crack becomes the only accent. "
                "Peak is denser gold, not louder motion.",
                className="lede",
            ),
            div(
                div(
                    span("the break", className="eyebrow"),
                    vessel_mark(piece, size=200, ident="kintsugi-body"),
                    p(
                        f"{piece.get('clay')} · {piece.get('glaze')}",
                        className="hearth-piece",
                    ),
                    p(
                        f"Brass holds the {join}." if join else f"A named break at the {where}.",
                        className="muted",
                    ),
                    div(*segs, className="segs", role="radiogroup", aria_label="Named break"),
                    div(
                        button(
                            "Already joined" if join else "Join with brass",
                            type="button",
                            className="btn-primary",
                            **control("kintsugi.join"),
                        ),
                        button(
                            "Name a break",
                            type="button",
                            className="btn-ghost",
                            **control("kintsugi.crack"),
                        ),
                        a("Send it", href="/gift", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className=f"hearth kintsugi-chamber {'is-joined' if join else 'is-open'}",
                    id="kintsugi-chamber",
                ),
                div(
                    span("joins", className="eyebrow"),
                    h2(f"{HOST.join_n} spent", className="sight-title"),
                    p("Each join is a Cap. The vessel stays. Presence does not remount.", className="sight-law"),
                    *repairs,
                    className="paper",
                    id="kintsugi-card",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room kintsugi-room",
        )

    @action(caps=())
    def name(self, where: str = "belly"):
        if where not in BREAKS:
            where = "belly"
        self.where = where
        mark_dirty(self)
        HOST.log("kintsugi.where", where)
        return update_with(self, extra_ops=[notify(where)])

    @action(caps=())
    def crack(self):
        where = str(self.where or "belly")
        HOST.crack(where)
        mark_dirty(self)
        return update_with(self, extra_ops=[notify(where)])

    @action(caps=("repair.join",))
    def join(self):
        where = str(self.where or "belly")
        HOST.mend(where)
        mark_dirty(self)
        plan = (
            scene("kintsugi-join")
            .share("vessel", leave="#kintsugi-body", arrive="#cradle-vessel", recipe=rise.enter(ms=180))
            .enter("#kintsugi-chamber", rise.enter(ms=200))
        )
        return update_with(self, plan, extra_ops=[notify("joined")])
