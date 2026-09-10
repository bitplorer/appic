"""Page unit — multiselect.py → MultiSelect. Owned kit, shell=False."""
from __future__ import annotations

from components.multiselect import MultiSelect as MultiSelectCard


class MultiSelect(MultiSelectCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
