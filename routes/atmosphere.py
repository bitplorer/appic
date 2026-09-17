"""Page unit — atmosphere.py → GET /atmosphere.

The kiln's air is a named chemistry. Heat (cone) is RefState.
Morph-then-Play: the chamber morphs, then rise/fade/slide.
"""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    button,
    circle,
    control,
    div,
    h1,
    h2,
    mark_dirty,
    morph_play,
    notify,
    optional_fade,
    optional_plan,
    optional_slide,
    p,
    path,
    progress,
    section,
    span,
    svg,
    update_with,
    a,
    fade,
    rise,
    scene,
    slide,
)
from store import HOST

AIRS = (
    ("oxidation", "Oxidation", "Clear flame. Iron stays honest. The glaze is quiet."),
    ("reduction", "Reduction", "The flame eats oxygen. Copper goes red. Iron goes celadon."),
    ("salt", "Salt", "Sodium in the air. Orange-peel skin. The chamber is weather."),
    ("wood", "Wood", "Ash falls. Flame licks. Every shelf is a different sky."),
)
CONES = ((6, "Cone 6"), (8, "Cone 8"), (10, "Cone 10"), (12, "Cone 12"))


class Atmosphere(Component):
    id = "atmosphere"
    air = MorphState("oxidation")
    cone = RefState(10)
    dirty = MorphState("idle")
    held = MorphState(False)

    def _cone(self) -> int:
        try:
            return max(6, min(12, int(self.cone or 10)))
        except (TypeError, ValueError):
            return 10

    def _row(self):
        key = str(self.air or "oxidation")
        for row in AIRS:
            if row[0] == key:
                return row
        return AIRS[0]

    def render(self):
        key, title, law = self._row()
        n = self._cone()
        pct = int(((n - 6) / 6) * 100)
        chips = [
            button(
                label,
                type="button",
                className="choice is-on" if self.air == k else "choice",
                **control("atmosphere.shift", air=k),
            )
            for k, label, _law in AIRS
        ]
        cones = [
            button(
                label,
                type="button",
                className="choice is-on" if n == val else "choice",
                **control("atmosphere.heat", cone=str(val)),
            )
            for val, label in CONES
        ]
        return section(
            span("Atmosphere", className="eyebrow"),
            h1("Name the air the fire breathes.", className="display"),
            p(
                "The atmosphere is MorphState. Cone is RefState. "
                "Holding the air is public; walking the piece to vitrine is Clock A. "
                "Motion is morph, then play — never html= on a plan.",
                className="lede",
            ),
            div(
                div(
                    span("chamber", className="eyebrow"),
                    svg(
                        circle(cx="80", cy="80", r="62", fill="none", stroke="currentColor", stroke_width="0.6", className="air-ring air-ring-3"),
                        circle(cx="80", cy="80", r="44", fill="none", stroke="currentColor", stroke_width="0.8", className="air-ring air-ring-2"),
                        circle(cx="80", cy="80", r="26", fill="none", stroke="currentColor", stroke_width="1.2", className="air-ring air-ring-1"),
                        circle(cx="80", cy="80", r="8", fill="currentColor", className="air-core"),
                        path(
                            d="M80 18 C92 40 96 56 80 80 C64 56 68 40 80 18",
                            fill="currentColor",
                            className="air-flame",
                        ),
                        viewBox="0 0 160 160",
                        className="air-svg",
                        aria_hidden="true",
                    ),
                    p(title, className="hearth-piece"),
                    p(f"Cone {n}", className="stat"),
                    p(law, className="muted"),
                    className=f"hearth air-chamber air-{key}",
                    data_air=key,
                    data_cone=str(n),
                    id="chamber",
                ),
                div(
                    span("named air", className="eyebrow"),
                    h2(title, className="sight-title"),
                    p(law, className="sight-law"),
                    div(*chips, className="choices", role="radiogroup", aria_label="Atmosphere"),
                    span("cone", className="eyebrow"),
                    div(*cones, className="choices", role="radiogroup", aria_label="Cone"),
                    progress(
                        value=str(pct),
                        max="100",
                        className="fire-bar",
                        role="progressbar",
                        aria_valuemin="0",
                        aria_valuemax="100",
                        aria_valuenow=str(pct),
                        aria_label="Cone heat",
                    ),
                    div(
                        button(
                            "Air is held" if self.held else "Hold this air",
                            type="button",
                            className="btn-primary",
                            **control("atmosphere.hold"),
                        ),
                        a("Draw to the vitrine", href="/vitrine", className="btn-ghost"),
                        a("Keep the fire", href="/kiln", className="btn-ghost"),
                        className="hero-actions",
                    ),
                    className="paper",
                    id="air-card",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room",
            data_air=key,
        )

    @action(caps=())
    def shift(self, air: str = "oxidation"):
        keys = {row[0] for row in AIRS}
        self.air = air if air in keys else "oxidation"
        mark_dirty(self)
        HOST.atmosphere = str(self.air)
        HOST.log("atmosphere.shift", str(self.air))
        # morph-then-play: fade the chamber after the fragment lands
        _ = morph_play, scene, fade, rise, slide
        return update_with(
            self,
            optional_fade("air", "#chamber"),
            extra_ops=[notify(str(self.air))],
        )

    @action(caps=())
    def heat(self, cone: str = "10"):
        try:
            n = int(cone)
        except (TypeError, ValueError):
            n = 10
        self.cone = max(6, min(12, n))
        mark_dirty(self)
        HOST.cone = int(self.cone)
        HOST.log("atmosphere.heat", str(self.cone))
        return update_with(
            self,
            optional_plan("cone", "#chamber"),
            extra_ops=[notify(f"cone {self.cone}")],
        )

    @action(caps=())
    def hold(self):
        self.held = True
        HOST.atmosphere = str(self.air)
        HOST.cone = self._cone()
        HOST.notice = f"{self.air} · cone {self._cone()} is held."
        HOST.log("atmosphere.hold", str(self.air))
        mark_dirty(self)
        return update_with(
            self,
            optional_slide("hold", "#air-card"),
            extra_ops=[notify("held")],
        )
