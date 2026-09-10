"""Page unit — resizable.py → Resizable. Owned kit, shell=False."""
from __future__ import annotations

from components.resizable import Resizable as ResizableCard


class Resizable(ResizableCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
