"""Page unit — gift.py → GET /gift.

The vessel leaves the house. Named destination. Send spends gift.send.
Presence ends — the cradle empties. Not a Pulse room.
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
    li,
    mark_dirty,
    notify,
    p,
    section,
    span,
    ul,
    update_with,
)
from chrome import vessel_mark
from store import HOST, DESTINATIONS


class Gift(Component):
    id = "gift"
    dest = MorphState("send")
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("gift")
        piece = HOST.vessel
        dest = str(self.dest or "send")
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if dest == key else "seg",
                **control("gift.name", dest=key),
            )
            for key in DESTINATIONS
        ]
        sent = [
            li(
                span(str(row.get("at", "")), className="tiny mono"),
                span(f"{row.get('clay', '')} · {row.get('dest', '')}", className="hand-line-verb"),
                span(str(row.get("id", "")), className="muted"),
                className="hand-line",
            )
            for row in reversed(HOST.gifts[-6:])
        ] or [li("Nothing has left the house.", className="hand-line")]
        if not piece:
            return section(
                span("Gift", className="eyebrow"),
                h1("The cloth is empty.", className="display"),
                p(
                    "A gift needs a vessel. Seat one, mend it if it broke, then name a destination. "
                    "Keep stays. Send leaves. Archive is memory.",
                    className="lede",
                ),
                div(
                    a("Seat a vessel", href="/vessel", className="btn-primary"),
                    a("Read lineage", href="/lineage", className="btn-ghost"),
                    className="hero-actions",
                ),
                ul(*sent, className="hands-log", role="log", aria_label="Gifts"),
                id=self.id,
                className="room emptystate gift-room",
            )
        return section(
            span("Gift", className="eyebrow"),
            h1("Let it leave the cloth.", className="display"),
            p(
                "Named destination on MorphState. The send is a Cap (gift.send). "
                "After it leaves, the cradle empties. Presence ends. Lineage remembers.",
                className="lede",
            ),
            div(
                div(
                    span("ready", className="eyebrow"),
                    vessel_mark(piece, size=160, ident="gift-body"),
                    p(
                        f"{piece.get('clay')} · {piece.get('glaze')} · {piece.get('stage')}",
                        className="hearth-piece",
                    ),
                    div(*segs, className="segs", role="radiogroup", aria_label="Destination"),
                    div(
                        button(
                            "Keep on the shelf" if dest == "keep" else (
                                "Lay it in memory" if dest == "archive" else "Send the vessel"
                            ),
                            type="button",
                            className="btn-primary",
                            **control("gift.send"),
                        ),
                        a("Mend first", href="/kintsugi", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="hearth gift-chamber",
                    id="gift-chamber",
                ),
                div(
                    span("left the house", className="eyebrow"),
                    h2(f"{len(HOST.gifts)} sent", className="sight-title"),
                    ul(*sent, className="hands-log", role="log", aria_label="Gifts"),
                    className="paper",
                    id="gift-card",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room gift-room",
        )

    @action(caps=())
    def name(self, dest: str = "send"):
        if dest not in DESTINATIONS:
            dest = "send"
        self.dest = dest
        mark_dirty(self)
        HOST.log("gift.dest", dest)
        return update_with(self, extra_ops=[notify(dest)])

    @action(caps=("gift.send",))
    def send(self):
        dest = str(self.dest or "send")
        HOST.gift(dest)
        mark_dirty(self)
        return update_with(self, extra_ops=[notify(dest)])
