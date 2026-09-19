"""Page unit — score.py → GET /score.

The house as a staff. Every named verb is a Host note. Morph-then-Play
stagger_in on surviving #note-* nodes. SCORE-1. Not a Pulse room.
"""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    a,
    action,
    button,
    circle,
    control,
    div,
    h1,
    h2,
    li,
    mark_dirty,
    notify,
    p,
    path,
    section,
    span,
    svg,
    ul,
    update_with,
    rise,
    scene,
)
from chrome import staff_mark
from store import HOST, PITCHES, STAFF_LINES, note_cy, staff_line_d


class Score(Component):
    id = "score"
    pitch = MorphState("G")
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("score")
        pitch = str(self.pitch or "G")
        if pitch not in PITCHES:
            pitch = "G"
        notes = list(HOST.score[-16:])
        kids = [
            path(
                d=staff_line_d(y, 640),
                fill="none",
                stroke="currentColor",
                stroke_width="1.1",
                className="staff-line",
            )
            for y in STAFF_LINES
        ]
        for i, row in enumerate(notes):
            x = 28 + i * 38
            cy = note_cy(str(row.get("pitch") or "G"))
            nid = str(row.get("id") or f"n{i}")
            kids.append(
                circle(
                    cx=str(x),
                    cy=str(cy),
                    r="6",
                    fill="currentColor",
                    className="staff-note is-on" if str(row.get("pitch")) == pitch else "staff-note",
                    id=f"note-{nid}",
                )
            )
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if pitch == key else "seg",
                **control("score.name", pitch=key),
            )
            for key in PITCHES
        ]
        lines = [
            li(
                span(str(row.get("at") or ""), className="hand-line-verb"),
                span(str(row.get("pitch") or "G"), className="chip"),
                span(str(row.get("verb") or ""), className="hand-line"),
                id=f"score-row-{row.get('id')}",
                className="hand-line",
            )
            for row in reversed(notes)
        ] or [li("The staff is empty. Write a note.", className="hand-line", id="score-empty")]
        return section(
            span("Score", className="eyebrow"),
            h1("The house writes itself.", className="display"),
            p(
                "Named pitch is MorphState. The staff is Host stock — never MorphState(list). "
                "Write is public. Walking a room already leaves a note. Morph-then-Play "
                "staggers surviving #note-* ids. XOR: the Plan carries no html=.",
                className="lede",
            ),
            div(
                div(
                    span("staff", className="eyebrow"),
                    svg(
                        *kids,
                        viewBox="0 0 640 80",
                        className="score-staff",
                        id="score-staff",
                        role="img",
                        aria_label=f"Score of {len(HOST.score)} notes",
                    ),
                    staff_mark(notes, ident="score-echo"),
                    p(f"{len(HOST.score)} notes on the cloth.", className="muted"),
                    className="paper score-paper",
                    id="score-card",
                ),
                div(
                    span("pitch", className="eyebrow"),
                    h2(pitch, className="sight-title"),
                    p("Name a pitch, then write. The instrument in chrome keeps the last ten.", className="sight-law"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Named pitch"),
                    div(
                        button("Write the note", type="button", className="btn-primary", **control("score.write")),
                        button("Rest", type="button", className="btn-ghost", **control("score.rest")),
                        a("Walk the chorus", href="/chorus", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    ul(*lines, className="hands-log", role="log", aria_label="Score ledger"),
                    className="paper",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room score-room",
            data_pitch=pitch,
        )

    def _plan(self):
        ids = [f"#note-{row.get('id')}" for row in HOST.score[-16:] if row.get("id")]
        return scene("score-write").stagger_in(ids or '[id^="note-"]', rise.enter(ms=90), gap_ms=36)

    @action(caps=())
    def name(self, pitch: str = "G"):
        self.pitch = pitch if pitch in PITCHES else "G"
        mark_dirty(self)
        HOST.log("score.pitch", str(self.pitch))
        return update_with(self, extra_ops=[notify(str(self.pitch))])

    @action(caps=())
    def write(self):
        pitch = str(self.pitch or "G")
        HOST.score_write("score.write", "score", pitch)
        HOST.notice = f"A {pitch} crossed the staff."
        mark_dirty(self)
        return update_with(self, self._plan(), extra_ops=[notify(pitch)])

    @action(caps=())
    def rest(self):
        HOST.score_write("score.rest", "score", str(self.pitch or "G"))
        HOST.notice = "A rest on the staff."
        mark_dirty(self)
        return update_with(self, self._plan(), extra_ops=[notify("rest")])
