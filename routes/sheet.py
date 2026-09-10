"""Page unit — sheet.py → Sheet. Owned kit, shell=False."""
from __future__ import annotations

from components.sheet import Sheet as SheetCard


class Sheet(SheetCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
