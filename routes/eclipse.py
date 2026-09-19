"""Page unit — eclipse.py → GET /eclipse.

Sky climate event. Named phase. Light is occluded. ECLIPSE-1.
Phase is MorphState. Count is Host stock. Clock tick wanes a full veil.
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
    mark_dirty,
    notify,
    optional_fade,
    p,
    path,
    section,
    span,
    svg,
    update_with,
)
from store import ECLIPSE_PHASES, HOST, clock_label

PHASE_COPY = {
    "clear": "The sky is named. Brass is visible. Walk as you were.",
    "wax": "The umbra is arriving. Specular from the top still holds.",
    "full": "Noon occluded. Grain thickens. The hearth is the only light.",
    "wane": "The brass is returning. A tick of the clock will lift the veil.",
}


class Eclipse(Component):
    id = "eclipse"
    phase = MorphState("clear")
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("eclipse")
        phase = str(HOST.eclipse_phase or self.phase or "clear")
        if phase not in ECLIPSE_PHASES:
            phase = "clear"
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if phase == key else "seg",
                **control("eclipse.veil", phase=key),
            )
            for key in ECLIPSE_PHASES
        ]
        cover = 8 if phase == "clear" else (42 if phase == "wax" else (92 if phase == "full" else 58))
        return section(
            span("Eclipse", className="eyebrow"),
            h1("Name the dark.", className="display"),
            p(
                "Phase is MorphState. The veil is Host climate — the same sky the "
                "instrument reads. Naming a phase turns auto off. A full veil wanes "
                "on the next clock tick, then lifts. GET chrome carries data-eclipse.",
                className="lede",
            ),
            div(
                div(
                    span("umbra", className="eyebrow"),
                    svg(
                        circle(cx="60", cy="60", r="34", fill="none", stroke="currentColor", stroke_width="1.4", className="eclipse-sun"),
                        circle(cx=str(60 + (cover - 50) * 0.4), cy="60", r="32", fill="currentColor", className="eclipse-moon"),
                        path(d="M20 60 A40 40 0 0 1 100 60", fill="none", stroke="currentColor", stroke_width="0.6", className="eclipse-arc"),
                        viewBox="0 0 120 120",
                        className="eclipse-svg",
                        id="eclipse-disk",
                        role="img",
                        aria_label=f"{phase} eclipse",
                    ),
                    p(clock_label(HOST.clock_h), className="stat"),
                    p(f"{HOST.eclipse_n} veils named.", className="muted"),
                    className=f"paper eclipse-chamber phase-{phase}",
                    id="eclipse-card",
                ),
                div(
                    span("phase", className="eyebrow"),
                    h2(phase, className="sight-title"),
                    p(PHASE_COPY[phase], className="sight-law"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Eclipse phase"),
                    div(
                        button("Veil the house", type="button", className="btn-primary", **control("eclipse.veil", phase="full")),
                        button("Lift the umbra", type="button", className="btn-ghost", **control("eclipse.unveil")),
                        a("Walk the table", href="/", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room eclipse-room",
            data_phase=phase,
        )

    @action(caps=())
    def veil(self, phase: str = "full"):
        named = HOST.veil(phase)
        self.phase = named
        mark_dirty(self)
        return update_with(self, optional_fade("eclipse", "#eclipse-card"), extra_ops=[notify(named)])

    @action(caps=())
    def unveil(self):
        named = HOST.unveil()
        self.phase = named
        mark_dirty(self)
        return update_with(self, optional_fade("unveil", "#eclipse-card"), extra_ops=[notify("clear")])
