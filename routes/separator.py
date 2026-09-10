"""Page unit — separator.py → Separator. Owned kit, shell=False."""
from __future__ import annotations

from components.separator import Separator as SeparatorCard


class Separator(SeparatorCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
