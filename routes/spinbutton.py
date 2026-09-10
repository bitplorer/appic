"""Page unit — spinbutton.py → SpinButton. Owned kit, shell=False."""
from __future__ import annotations

from components.spinbutton import SpinButton as SpinButtonCard


class SpinButton(SpinButtonCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
