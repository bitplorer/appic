"""Page unit — switch.py → Switch. Owned kit, shell=False."""
from __future__ import annotations

from components.switch import Switch as SwitchCard


class Switch(SwitchCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
