"""Page unit — usermenu.py → UserMenu. Owned kit, shell=False."""
from __future__ import annotations

from components.usermenu import UserMenu as UserMenuCard


class UserMenu(UserMenuCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
