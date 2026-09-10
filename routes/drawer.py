"""Page unit — drawer.py → Drawer. Sheet alias, same Host, right edge."""
from __future__ import annotations

from components.sheet import Sheet


class Drawer(Sheet):
    id = "drawer"

    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
