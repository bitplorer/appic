"""Page unit — ash.py → GET /ash.

Memory of fire. Named grade. Host stock of last firings.
optional_fade as cooling. Not a Pulse room. ASH-1.
"""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    a,
    action,
    bind,
    button,
    circle,
    div,
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
    svg,
    ul,
    update_with,
)
from store import ASH_GRADES, HOST, ash_d

GRADE_COPY = {
    "fine": "Cool dust. The hearth is a whisper. optional_fade on #ash-disk.",
    "flake": "Leaf of fire. Specular still arrives from the top.",
    "slag": "The densest remainder. Grain thickens. Heat has left a body.",
}

CX = {"fine": 36, "flake": 60, "slag": 84}


class Ash(Component):
    id = "ash"
    grade = MorphState("fine")
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("ash")
        grade = str(self.grade or HOST.ash_grade or "fine")
        if grade not in ASH_GRADES:
            grade = "fine"
        HOST.ash_grade = grade
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if grade == key else "seg",
                **bind(self.name, grade=key),
            )
            for key in ASH_GRADES
        ]
        last = HOST.ash[-6:]
        rows = [
            li(
                span(str(row.get("at") or ""), className="tiny mono"),
                span(f"{row.get('grade')} · {row.get('clay') or 'clay'}", className="hand-line-verb"),
                span(str(row.get("heat") or "0"), className="muted"),
                className="hand-line",
                id=f"ash-row-{row.get('id') or i}",
            )
            for i, row in enumerate(reversed(last))
        ] or [li("The hearth has not yet left a body.", className="hand-line", id="ash-row-void")]
        cx = CX.get(grade, 36)
        return section(
            span("Ash", className="eyebrow"),
            h1("Name the remainder.", className="display"),
            p(
                "Fire leaves a body. Grade is MorphState. The list is Host stock. "
                "Raking is public. A draw from the kiln writes a row. "
                "Cooling is optional_fade. XOR: the Plan carries no html=. Not Pulse.",
                className="lede",
            ),
            div(
                div(
                    span("remainder", className="eyebrow"),
                    svg(
                        circle(
                            cx="60",
                            cy="60",
                            r="34",
                            fill="none",
                            stroke="currentColor",
                            stroke_width="1.2",
                            className="ash-ring",
                        ),
                        circle(
                            cx="60",
                            cy="60",
                            r="22",
                            fill="none",
                            stroke="currentColor",
                            stroke_width="1",
                            className="ash-ring ash-ring-in",
                        ),
                        circle(
                            cx=str(cx),
                            cy="60",
                            r="7",
                            fill="currentColor",
                            className="ash-ember",
                        ),
                        path(
                            d=ash_d(grade),
                            fill="none",
                            stroke="currentColor",
                            stroke_width="1.3",
                            stroke_linecap="round",
                            className="wave-path",
                            transform="translate(0 72)",
                        ),
                        viewBox="0 0 120 120",
                        className="eclipse-svg ash-svg",
                        id="ash-disk",
                        role="img",
                        aria_label=f"{grade} ash",
                    ),
                    p(f"{len(HOST.ash)} bodies.", className="stat"),
                    p(
                        "hearth dark" if not HOST.firing else f"{HOST.heat_remain}h remaining",
                        className="muted",
                    ),
                    className=f"paper eclipse-chamber grade-{grade}",
                    id="ash-card",
                ),
                div(
                    span("grade", className="eyebrow"),
                    h2(grade, className="sight-title"),
                    p(GRADE_COPY[grade], className="sight-law"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Ash grade"),
                    ul(*rows, className="hands-log", role="log", aria_label="Ash bodies"),
                    div(
                        button("Rake the hearth", type="button", className="btn-primary", **bind(self.rake)),
                        a("Name the grain", href="/grain", className="btn-ghost"),
                        a("Draw the well", href="/well", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper",
                    id="ash-panel",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room ash-room",
            data_ash=grade,
        )

    @action(caps=())
    def name(self, grade: str = "fine"):
        named = HOST.name_ash(grade)
        self.grade = named
        mark_dirty(self)
        return update_with(self, optional_fade("ash", "#ash-card"), extra_ops=[notify(named)])

    @action(caps=())
    def rake(self):
        row = HOST.rake_ash()
        self.grade = str(row.get("grade") or self.grade)
        mark_dirty(self)
        return update_with(self, optional_fade("ash-rake", "#ash-card"), extra_ops=[notify("raked")])
