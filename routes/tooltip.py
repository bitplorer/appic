"""Page unit — tooltip.py → Tooltip. Owned kit, shell=False."""
from __future__ import annotations

from components.tooltip import Tooltip as TooltipCard


class Tooltip(TooltipCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
