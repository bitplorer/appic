"""Page unit — navbar.py → Navbar. Owned kit, shell=False."""
from __future__ import annotations

from components.navbar import Navbar as NavbarCard


class Navbar(NavbarCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
