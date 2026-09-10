"""APG chrome gallery — Caps stay off chrome."""
from __future__ import annotations

from foundry import kit_tree
from ux_compose import Component, div, h1, p, section, span


class Chrome(Component):
    id = "chrome"

    def render(self):
        return section(
            span("caps off chrome", className="kicker"),
            h1("Chrome"),
            p(
                "Menubar submenu ids stay in the tree when closed. "
                "Toolbar last command is aria-current, not pressed. "
                "Spin magnitude is RefState. Theme is a named radiogroup, not a boolean.",
                className="lede",
            ),
            div(
                kit_tree("navbar"),
                kit_tree("menubar"),
                kit_tree("toolbar"),
                kit_tree("togglegroup"),
                kit_tree("spinbutton"),
                kit_tree("themeswitch"),
                kit_tree("filterbar"),
                kit_tree("bottomnav"),
                kit_tree("separator"),
                className="stack-paper",
            ),
            id=self.id,
            className="page",
        )
