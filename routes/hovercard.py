"""Page unit — hovercard.py → HoverCard. Owned kit, shell=False."""
from __future__ import annotations

from components.hovercard import HoverCard as HoverCardCard


class HoverCard(HoverCardCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
