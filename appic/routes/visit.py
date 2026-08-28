"""Page unit: visit.py → Visit. Named steps, plans, calendar, dialog."""
from __future__ import annotations

from appic.rooms import room
from appic.ux import Component


class Visit(Component):
    id = "visit"

    def render(self):
        return room(
            "Visit",
            "Finish is a Cap.",
            "Named steps. One plan. A day on the calendar. Keep it swipes down; Delete spends a Cap.",
            "stepper",
            "plans",
            "calendar",
            "dialog",
            rid=self.id,
        )
