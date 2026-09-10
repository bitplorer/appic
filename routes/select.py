"""Page unit — select.py → Select. Owned kit, shell=False."""
from __future__ import annotations

from components.select import Select as SelectCard


class Select(SelectCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
