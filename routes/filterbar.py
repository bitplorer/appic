"""Page unit — filterbar.py → FilterBar. Owned kit, shell=False."""
from __future__ import annotations

from components.filterbar import FilterBar as FilterBarCard


class FilterBar(FilterBarCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
