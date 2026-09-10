"""Market hall — Hero, pricing, marks, quotes, newsletter as a storefront."""
from __future__ import annotations

from foundry import kit_tree
from ux_compose import Component, a, div, h1, p, section, span


class Atelier(Component):
    id = "atelier"

    def render(self):
        return section(
            span("market hall", className="kicker"),
            h1("Atelier"),
            p(
                "Marketing stems are a real storefront for the foundry, not a widget zoo. "
                "Choose a pricing tier on the button, never the row.",
                className="lede",
            ),
            div(
                kit_tree("hero"),
                kit_tree("featuregrid"),
                kit_tree("pricingsection"),
                kit_tree("logocloud"),
                kit_tree("testimonials"),
                kit_tree("newsletter"),
                kit_tree("cta"),
                className="stack-paper",
            ),
            a("Commission a piece", href="/commission", className="btn-primary"),
            id=self.id,
            className="page",
        )
