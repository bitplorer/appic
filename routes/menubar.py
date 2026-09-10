"""Page unit — menubar.py → Menubar. Owned kit, shell=False."""
from __future__ import annotations

from components.menubar import Menubar as MenubarCard


class Menubar(MenubarCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
