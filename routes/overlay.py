"""Page unit — OverlayChrome edge family vs anchored family."""
from __future__ import annotations

from ux_compose import Component, a, article, div, h1, h2, p, section, span


class Overlay(Component):
    id = "overlay"

    def render(self):
        return section(
            span("Edge", className="eyebrow"),
            h1("The edge is a different family.", className="display"),
            p(
                "OverlayChrome owns scrim / panel / dismiss ids, dismiss_on() += Escape, "
                "and open_plan() selectors-only. Root swipe.* is a defect.",
                className="lede",
            ),
            div(
                article(
                    h2("Edge family"),
                    p("Dialog · Sheet · Drawer · ActionSheet · AlertDialog · Command."),
                    a("Dialog", href="/dialog", className="btn-ghost"),
                    a("Sheet", href="/sheet", className="btn-ghost"),
                    a("Drawer", href="/drawer", className="btn-ghost"),
                    a("Action sheet", href="/actionsheet", className="btn-ghost"),
                    a("Alert dialog", href="/alertdialog", className="btn-ghost"),
                    a("Command", href="/command", className="btn-ghost"),
                    className="paper stack",
                ),
                article(
                    h2("Anchored family"),
                    p("Do not reuse OverlayChrome ids. Escape dismisses. Not interrupting."),
                    a("Dropdown", href="/dropdown", className="btn-ghost"),
                    a("Popover", href="/popover", className="btn-ghost"),
                    a("Tooltip", href="/tooltip", className="btn-ghost"),
                    a("Hover card", href="/hovercard", className="btn-ghost"),
                    className="paper stack",
                ),
                className="split",
            ),
            p(
                "AlertDialog is interrupting — Escape and scrim do not dismiss. "
                "Command takes OverlayChrome ids. kind=drawer is Sheet-right.",
                className="muted",
            ),
            id=self.id,
            className="room",
        )
