"""Page unit — tide.py → GET /tide.

Lunar climate. Named phase. Water is a path. TIDE-1.
Phase is MorphState. Count is Host stock. Clock tick names auto tide.
New burns hotter. Full cools the hearth. Not a Pulse room.
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
from store import HOST, TIDES, clock_label, tide_d

PHASE_COPY = {
    "new": "The water is still. The hearth burns faster. Name a phase to hold it.",
    "wax": "The water is arriving. Specular from the top still holds.",
    "full": "The water is named. Heat wanes slower. Grain thickens on the body.",
    "wane": "The brass is returning. A tick of the clock will name the next tide.",
}

MOON_CX = {"new": 28, "wax": 44, "full": 60, "wane": 76}


class Tide(Component):
    id = "tide"
    phase = MorphState("new")
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("tide")
        phase = str(HOST.tide_phase or self.phase or "new")
        if phase not in TIDES:
            phase = "new"
        segs = [
            button(
                key,
                type="button",
                className="seg is-on" if phase == key else "seg",
                **bind(self.name, phase=key),
            )
            for key in TIDES
        ]
        cx = MOON_CX.get(phase, 28)
        return section(
            span("Tide", className="eyebrow"),
            h1("Name the water.", className="display"),
            p(
                "Phase is MorphState. The tide is Host climate — the same water the "
                "instrument reads. Naming a phase turns auto off. New burns hotter. "
                "Full cools the hearth. GET chrome carries data-tide.",
                className="lede",
            ),
            div(
                div(
                    span("lumen", className="eyebrow"),
                    svg(
                        circle(cx="60", cy="60", r="34", fill="none", stroke="currentColor", stroke_width="1.4", className="eclipse-sun"),
                        circle(cx=str(cx), cy="60", r="28", fill="currentColor", className="tide-moon"),
                        path(
                            d=tide_d(phase),
                            fill="none",
                            stroke="currentColor",
                            stroke_width="1.4",
                            stroke_linecap="round",
                            className="wave-path",
                            transform="translate(0 70)",
                        ),
                        viewBox="0 0 120 120",
                        className="eclipse-svg tide-svg",
                        id="tide-disk",
                        role="img",
                        aria_label=f"{phase} tide",
                    ),
                    p(clock_label(HOST.clock_h), className="stat"),
                    p(f"auto {'on' if HOST.auto_tide else 'held'}.", className="muted"),
                    className=f"paper eclipse-chamber phase-{phase}",
                    id="tide-card",
                ),
                div(
                    span("phase", className="eyebrow"),
                    h2(phase, className="sight-title"),
                    p(PHASE_COPY[phase], className="sight-law"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Tide phase"),
                    div(
                        button("Name a full tide", type="button", className="btn-primary", **bind(self.name, phase="full")),
                        button("Release auto", type="button", className="btn-ghost", **bind(self.release)),
                        a("Hop the fugue", href="/fugue", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room tide-room",
            data_tide=phase,
        )

    @action(caps=())
    def name(self, phase: str = "full"):
        named = HOST.name_tide(phase)
        self.phase = named
        mark_dirty(self)
        return update_with(self, optional_fade("tide", "#tide-card"), extra_ops=[notify(named)])

    @action(caps=())
    def release(self):
        HOST.auto_tide = True
        named = HOST.sync_tide()
        self.phase = named
        mark_dirty(self)
        HOST.notice = "The tide follows the clock."
        return update_with(self, optional_fade("tide-auto", "#tide-card"), extra_ops=[notify(named)])
