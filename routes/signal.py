"""Signal — Wave 1 gesture grammar. Swipe lives on handles."""
from __future__ import annotations

from foundry import kit_tree
from ux_compose import Component, div, h1, p, section, span


class Signal(Component):
    id = "signal"

    def render(self):
        return section(
            span("grammar in the hand", className="kicker"),
            h1("Signal"),
            p(
                "ActionSheet handle: click swipe.down swipe.vertical threshold:48. "
                "PullRefresh accepts swipe.down. Sheet close accepts swipe.right. "
                "No root swipe on OverlayChrome.",
                className="lede",
            ),
            div(
                kit_tree("actionsheet"),
                kit_tree("pullrefresh"),
                kit_tree("sheet"),
                className="stack-paper",
            ),
            id=self.id,
            className="page",
        )
