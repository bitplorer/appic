"""Atelier — Kit Cut 1 slots live in the house."""
from __future__ import annotations
from ux_compose import Component, a, div, h1, p, section, span

class Atelier(Component):
    id = "atelier"
    def render(self):
        return section(
            span("Atelier", className="eyebrow"),
            h1("shell=False is the unit. The kicker is optional.", className="display"),
            p("apply_slots writes documented seams. Unknown slots fail closed. Kits stay Component subclasses.", className="lede"),
            div(
                a("Login unit", href="/login", className="map-card"),
                a("Hero unit", href="/hero", className="map-card"),
                a("Card unit", href="/card", className="map-card"),
                a("Empty state", href="/emptystate", className="map-card"),
                a("Skeleton", href="/skeleton", className="map-card"),
                a("Alert", href="/alert", className="map-card"),
                a("Banner", href="/banner", className="map-card"),
                a("Badge", href="/badge", className="map-card"),
                a("Avatar", href="/avatar", className="map-card"),
                a("Stats", href="/stats", className="map-card"),
                a("Switch", href="/switch", className="map-card"),
                a("Slider", href="/slider", className="map-card"),
                className="map-grid",
            ),
            id=self.id, className="room",
        )
