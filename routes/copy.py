"""Copy press — the ownership ritual. Kit cards are rooms you own."""
from __future__ import annotations

from ux_compose import Component, a, h1, li, p, section, span, ul
from ux_compose.kit.catalog import CATALOG, list_components


class Copy(Component):
    id = "copy"

    def render(self):
        stems = sorted(CATALOG.keys())
        n = len(list_components())
        sample = [li(f"uxcompose add {s}") for s in stems[:12]]
        return section(
            span("ownership ritual", className="kicker"),
            h1("Press"),
            p(
                f"{n} catalog stems. catalog.py and copy.py are tooling, not cards. "
                "The library keeps the source of truth. The copy is yours to edit. "
                "drawer is the Sheet alias — still own it.",
                className="lede",
            ),
            ul(*sample, className="law-list paper"),
            p(f"{n - 12} more stems live in the house.", className="muted"),
            a("Walk the house", href="/house", className="btn-primary"),
            id=self.id,
            className="page",
        )
