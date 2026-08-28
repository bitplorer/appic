"""Page unit: desk.py → Desk. Owned kit living room."""
from __future__ import annotations

from appic.rooms import room
from appic.ux import Component


class Desk(Component):
    id = "desk"

    def render(self):
        return room(
            "Desk",
            "The house keeps a quiet list.",
            "Rail, crumbs, tabs, pull-to-refresh, accordion, command, toast — owned copies, restyled by living here.",
            "sidebar",
            "breadcrumb",
            "tabs",
            "pullrefresh",
            "accordion",
            "command",
            "toast",
            rid=self.id,
        )
