"""Clock A GET vs Clock B action. Payload type picks media type."""
from __future__ import annotations

from ux_compose import Component, a, div, h1, h2, p, section, span


class Clocks(Component):
    id = "clocks"

    def render(self):
        return section(
            span("two clocks, one sky", className="kicker"),
            h1("Clocks"),
            div(
                div(
                    h2("Clock A"),
                    p("GET wraps render(). HTML is daylight. A dict is a pulse. A generator is a stream of light."),
                    a("JSON pulse", href="/pulse.json", className="btn-ghost"),
                    a("Stream", href="/stream", className="btn-ghost"),
                    className="paper",
                ),
                div(
                    h2("Clock B"),
                    p("Action is Intent → Cap → Result. Live client posts /ux-channel/action. Author door posts /act/{action}."),
                    a("Open the lab", href="/lab", className="btn-ghost"),
                    className="paper",
                ),
                className="kit-grid",
            ),
            id=self.id,
            className="page",
        )
