"""Page unit — scrollarea.py → ScrollArea. Owned kit, shell=False."""
from __future__ import annotations

from components.scrollarea import ScrollArea as ScrollAreaCard


class ScrollArea(ScrollAreaCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
