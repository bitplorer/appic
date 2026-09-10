"""Page unit — Visit. Commission path cards."""
from __future__ import annotations

from ux_compose import Component, a, div, h1, p, section, span


class Visit(Component):
    id = "visit"

    def render(self):
        return section(
            span("Visit", className="eyebrow"),
            h1("Stay for a firing.", className="display"),
            p("Named steps. Finish spends stepper.finish. Confirm is a Cap.", className="lede"),
            div(
                a("Stepper", href="/stepper", className="map-card"),
                a("Plans", href="/plans", className="map-card"),
                a("Calendar", href="/calendar", className="map-card"),
                a("Date picker", href="/datepicker", className="map-card"),
                a("Dialog", href="/dialog", className="map-card"),
                a("Questionnaire", href="/questionnaire", className="map-card"),
                className="map-grid",
            ),
            id=self.id,
            className="room",
        )
