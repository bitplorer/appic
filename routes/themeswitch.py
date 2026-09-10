"""Page unit — themeswitch.py → ThemeSwitch. Owned kit, shell=False."""
from __future__ import annotations

from components.themeswitch import ThemeSwitch as ThemeSwitchCard


class ThemeSwitch(ThemeSwitchCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
