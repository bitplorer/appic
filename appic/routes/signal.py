"""Page unit: signal.py → Signal. Wave 1 grammar made visible."""
from __future__ import annotations

from appic.rooms import hero
from appic.ux import Component, article, div, h2, li, p, span, ul


GRAMMAR = (
    ("swipe.vertical", "PullRefresh list. Axis-lock. The Refresh control also accepts click swipe.down."),
    ("swipe.horizontal", "Carousel stage. Prev/Next overlay 44px chevrons. One translating pip."),
    ("click swipe.down", "ActionSheet handle. Dialog Keep it. Never the root — a root swipe swallows row clicks."),
    ("click swipe.right", "Sheet Close / Done. No root swipe.horizontal."),
    ("longpress", "ContextMenu. Floating panel, menuitem rows, not a native list."),
    ("input delay:", "Typeahead. The field is the control. Query attaches, then morphs."),
    ("data-channel-id", "Root stamp on carousel, action sheet, context menu. Slot is #id and [data-channel-id] together."),
    ("data-channel-on", "The synthesizer attribute. Kit already stamps it. Product never invents a second one."),
)


class Signal(Component):
    id = "signal"

    def render(self):
        chips = [
            article(
                h2(name, className="mono"),
                p(body, className="lede"),
                className="signal-chip",
                id=f"signal-{name.split('.')[0]}-{i}",
            )
            for i, (name, body) in enumerate(GRAMMAR)
        ]
        return div(
            hero(
                "Signal",
                "A grammar you can feel.",
                "Swipe lives on the handle. Longpress opens a floating menu. Delayed input is still one Intent.",
            ),
            ul(
                *[li(span(n, className="chip"), className="signal-legend") for n, _ in GRAMMAR],
                className="chip-row",
            ),
            div(*chips, className="kit-grid"),
            id=self.id,
            className="room",
        )
