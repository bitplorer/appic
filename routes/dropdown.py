"""Page unit — dropdown.py → Dropdown. Owned kit, shell=False."""
from __future__ import annotations

from components.dropdown import Dropdown as DropdownCard


class Dropdown(DropdownCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
