"""Edge vs anchored — OverlayChrome family is not a popover family."""
from __future__ import annotations

from foundry import kit_tree
from ux_compose import Component, div, h1, p, section, span


class Overlay(Component):
    id = "overlay"

    def render(self):
        return section(
            span("two families", className="kicker"),
            h1("Edge"),
            p(
                "Dialog, Sheet, Drawer, ActionSheet, AlertDialog, and Command take OverlayChrome. "
                "AlertDialog is interrupting — Escape and scrim do not dismiss. "
                "Popover, Tooltip, HoverCard, Dropdown, Select stay anchored. "
                "Swipe lives on the handle, never the root.",
                className="lede",
            ),
            div(
                span("Edge", className="kicker"),
                kit_tree("dialog"),
                kit_tree("sheet"),
                kit_tree("drawer"),
                kit_tree("actionsheet"),
                kit_tree("alertdialog"),
                kit_tree("command"),
                span("Anchored", className="kicker"),
                kit_tree("popover"),
                kit_tree("tooltip"),
                kit_tree("hovercard"),
                kit_tree("dropdown"),
                kit_tree("select"),
                className="stack-paper",
            ),
            id=self.id,
            className="page",
        )
