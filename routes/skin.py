"""Skin — WebAssets + ThemeSwitch. CSS is a frozen sheet after uxcompose build."""
from __future__ import annotations

from foundry import kit_tree
from settings import OUTPUT_CSS, webassets
from ux_compose import Component, div, h1, p, section, span


class Skin(Component):
    id = "skin"

    def render(self):
        href = "/css/" + OUTPUT_CSS
        css_dir = getattr(getattr(webassets, "static", None), "css", None)
        return section(
            span("webassets", className="kicker"),
            h1("Skin"),
            p(
                f"Document links {href}. Theme is a named radiogroup (light / dark / system), "
                "not a boolean switch. Companion CSS per kit card is forbidden.",
                className="lede",
            ),
            p(f"compiler dir · {css_dir}", className="mono"),
            div(kit_tree("themeswitch"), className="stack-paper"),
            id=self.id,
            className="page",
        )
