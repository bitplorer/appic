"""Page unit — bottomnav.py → BottomNav. Owned kit, shell=False."""
from __future__ import annotations

from components.bottomnav import BottomNav as BottomNavCard


class BottomNav(BottomNavCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
