"""Page unit — toolbar.py → Toolbar. Owned kit, shell=False."""
from __future__ import annotations

from components.toolbar import Toolbar as ToolbarCard


class Toolbar(ToolbarCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
