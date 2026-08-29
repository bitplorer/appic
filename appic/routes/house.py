"""Page unit: house.py → House. Search, stage, shelf, signal."""
from __future__ import annotations

from appic.rooms import room
from appic.ux import Component


class House(Component):
    id = "house"

    def render(self):
        return room(
            "House",
            "Linen, oak, wool, clay.",
            "Typeahead morphs the hits slot after a 300ms pause — the field is never rewritten. Longpress a mark. Swipe the sheet closed. The carousel pip translates.",
            "typeahead",
            "combobox",
            "select",
            "dropdown",
            "sheet",
            "carousel",
            "table",
            "pagination",
            "contextmenu",
            "actionsheet",
            rid=self.id,
        )
