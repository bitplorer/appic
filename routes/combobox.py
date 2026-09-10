"""Page unit — combobox.py → Combobox. Owned kit, shell=False."""
from __future__ import annotations

from components.combobox import Combobox as ComboboxCard


class Combobox(ComboboxCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
