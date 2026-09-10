"""Page unit — togglegroup.py → ToggleGroup. Owned kit, shell=False."""
from __future__ import annotations

from components.togglegroup import ToggleGroup as ToggleGroupCard


class ToggleGroup(ToggleGroupCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
