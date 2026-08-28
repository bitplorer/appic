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
            "Typeahead filters on input delay:. Longpress a mark. Swipe the sheet closed. The carousel pip translates.",
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
