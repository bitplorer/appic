"""Forge — glaze chemistry, kiln time, chart, tree, diff, mockup."""
from __future__ import annotations

from foundry import kit_tree
from ux_compose import Component, div, h1, p, section, span


class Forge(Component):
    id = "forge"

    def render(self):
        return section(
            span("workbench", className="kicker"),
            h1("Forge"),
            p(
                "Color is a named swatch, never a hue quantity. "
                "Kiln remaining is RefState on a role=timer. "
                "Bar heights are RefState. Tree expanded ids are names.",
                className="lede",
            ),
            div(
                kit_tree("colorpicker"),
                kit_tree("countdown"),
                kit_tree("progress"),
                kit_tree("chart"),
                kit_tree("tree"),
                kit_tree("diff"),
                kit_tree("mockup"),
                kit_tree("attachment"),
                kit_tree("resizable"),
                className="kit-grid",
            ),
            id=self.id,
            className="page",
        )
