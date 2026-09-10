"""Page unit — calendar.py → Calendar. Owned kit, shell=False."""
from __future__ import annotations

from components.calendar import Calendar as CalendarCard


class Calendar(CalendarCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
