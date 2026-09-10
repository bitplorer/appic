"""Product constitution. FastAPI Swagger stays off. This page owns GET /docs."""
from __future__ import annotations

from ux_compose import Component, a, article, div, h1, h2, li, p, section, span, ul


class Docs(Component):
    id = "docs"

    def render(self):
        laws = [
            "Product lifecycle CLI is uxcompose only.",
            "Page units have no HTTP verbs. Clock A wraps render().",
            "Quantity is RefState. Named things are MorphState.",
            "Isolation: product modules never import ux_channel.",
            "GET chrome lives on wrap=, never inside render().",
            "Plans carry no html=. Morph first, then transition.play.",
            "Kit cards are rooms you own after uxcompose add.",
            "AlertDialog is interrupting. Escape does not dismiss it.",
            "Menubar / FAB closed menus keep their ids, hidden.",
            "Typeahead morphs the hits slot, never the field being typed.",
            "cek=require is the product Cap Host.",
            "Levels are additive. L1 stays correct at L3. Zero rewrite.",
        ]
        return section(
            span("constitution", className="kicker"),
            h1("Law"),
            p(
                "This is GET /docs — a written constitution, not Swagger. "
                "build(openapi=False) is the default so this room can exist.",
                className="lede",
            ),
            article(
                h2("Hard invariants"),
                ul(*[li(law) for law in laws], className="law-list"),
                className="paper",
            ),
            div(
                a("Trace doctor residuals", href="/trace", className="btn-ghost"),
                a("Notes", href="/notes", className="btn-ghost"),
                a("Ship", href="/ship", className="btn-ghost"),
                a("Skin", href="/skin", className="btn-ghost"),
                className="row",
            ),
            id=self.id,
            className="page",
        )
