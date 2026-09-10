"""Page unit — navmenu.py → NavMenu. Owned kit, shell=False."""
from __future__ import annotations

from components.navmenu import NavMenu as NavMenuCard


class NavMenu(NavMenuCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
