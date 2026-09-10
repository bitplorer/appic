"""Page unit — popover.py → Popover. Owned kit, shell=False."""
from __future__ import annotations

from components.popover import Popover as PopoverCard


class Popover(PopoverCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
