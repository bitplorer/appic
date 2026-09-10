"""Studio — chat log, feed, files. Presence, not a SPA socket toy."""
from __future__ import annotations

from foundry import kit_tree
from ux_compose import Component, div, h1, p, section, span


class Studio(Component):
    id = "studio"

    def render(self):
        return section(
            span("role=log", className="kicker"),
            h1("Studio"),
            p(
                "The thread is a log. Composer label matches id. Send is public. "
                "Feed articles are RefState. Files are names on RefState.",
                className="lede",
            ),
            div(
                kit_tree("chat"),
                kit_tree("feed"),
                kit_tree("fileupload"),
                kit_tree("attachment"),
                kit_tree("scrollarea"),
                className="stack-paper",
            ),
            id=self.id,
            className="page",
        )
