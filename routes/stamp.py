"""Page unit — stamp.py → GET /stamp.

Maker's mark. field() is the inscription. status() is the reading.
Press spends stamp.press. Not /author. STAMP-1. Not Pulse.
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
    circle,
    div,
    field,
    h1,
    h2,
    li,
    mark_dirty,
    notify,
    optional_fade,
    p,
    path,
    section,
    span,
    status,
    svg,
    ul,
    update_with,
)
from chrome import vessel_mark
from store import CHOPS, HOST

FACES = ("lip", "foot", "belly")

FACE_COPY = {
    "lip": "A mark at the rim. The first thing a hand meets.",
    "foot": "A mark under the foot. Provenance that sits on the shelf.",
    "belly": "A mark in the well. The piece looking inward.",
}


class Stamp(Component):
    id = "stamp"
    face = MorphState("foot")
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("stamp")
        face = str(self.face or "foot")
        if face not in FACES:
            face = "foot"
        piece = HOST.vessel
        mark = str(HOST.stamp_mark or "APPIC")
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if face == key else "seg",
                **bind(self.name, face=key),
            )
            for key in FACES
        ]
        chops = [
            button(
                key,
                type="button",
                className="seg is-on" if mark == key else "seg",
                **bind(self.inscribe, mark=key),
            )
            for key in CHOPS
        ]
        pressed = [
            li(
                span(str(row.get("at") or ""), className="tiny mono"),
                span(f"{row.get('mark')} · {row.get('face')}", className="hand-line-verb"),
                span(str(row.get("id") or ""), className="muted"),
                className="hand-line",
            )
            for row in reversed(HOST.stamps[-6:])
        ] or [li("No chop has been pressed.", className="hand-line")]
        kids = [
            circle(cx="50", cy="50", r="44", fill="none", stroke="currentColor", stroke_width="1.6"),
            circle(cx="50", cy="50", r="36", fill="none", stroke="currentColor", stroke_width="0.8"),
            path(
                d="M32 50 L50 28 L68 50 L50 72 Z",
                fill="none",
                stroke="currentColor",
                stroke_width="1.4",
                className="stamp-diamond",
            ),
        ]
        reading = HOST.stamp_mark or "unmarked"
        chamber = [
            span("chop", className="eyebrow"),
            svg(
                *kids,
                viewBox="0 0 100 100",
                className="stamp-svg",
                id="stamp-disk",
                role="img",
                aria_label=f"chop {reading}",
            ),
            p(reading, className="stat stamp-reading"),
            status(HOST.notice or "The wax is quiet.", kind="note"),
        ]
        if piece:
            chamber.insert(1, vessel_mark(piece, size=88, ident="stamp-vessel"))
        return section(
            span("Stamp", className="eyebrow"),
            h1("Press the maker's mark.", className="display"),
            p(
                "field() is the inscription. status() is the reading. Face is MorphState. "
                "The press spends stamp.press. The chop is Host stock, never MorphState(list). "
                "Not /author. Not Pulse.",
                className="lede",
            ),
            div(
                div(
                    *chamber,
                    className="paper eclipse-chamber stamp-chamber",
                    id="stamp-card",
                ),
                div(
                    span("inscription", className="eyebrow"),
                    h2(face, className="sight-title"),
                    p(FACE_COPY[face], className="sight-law"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Stamp face"),
                    span("chop", className="eyebrow"),
                    div(*chops, className="segs", role="radiogroup", aria_label="Chop"),
                    field("mark", value=mark, placeholder="A chop — four letters", kind="text"),
                    div(
                        button(
                            "Press the chop",
                            type="button",
                            className="btn-primary",
                            **bind(self.press, mark=mark, face=face),
                        ),
                        act("stamp.press", "Press via /act", kind="ghost", target="#stamp", mark=mark, face=face),
                        a("Rake the ash", href="/ash", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    ul(*pressed, className="hands-log", role="log", aria_label="Chops"),
                    className="paper",
                    id="stamp-panel",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room stamp-room",
            data_face=face,
        )

    @action(caps=())
    def name(self, face: str = "foot"):
        if face not in FACES:
            face = "foot"
        self.face = face
        mark_dirty(self)
        HOST.log("stamp.face", face)
        return update_with(self, extra_ops=[notify(face)])

    @action(caps=())
    def inscribe(self, mark: str = "APPIC"):
        letters = "".join(ch for ch in str(mark or "APPIC").upper() if ch.isalnum())[:12] or "APPIC"
        HOST.stamp_mark = letters
        mark_dirty(self)
        HOST.log("stamp.inscribe", letters)
        return update_with(self, extra_ops=[notify(letters)])

    @action(caps=("stamp.press",))
    def press(self, mark: str = "APPIC", face: str = "foot"):
        row = HOST.press_stamp(mark, face=face)
        self.face = str(row.get("face") or face)
        mark_dirty(self)
        return update_with(self, optional_fade("stamp", "#stamp-card"), extra_ops=[notify(str(row.get("mark") or mark))])
