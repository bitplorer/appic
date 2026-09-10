"""Page unit — alert.py → Alert. Owned kit, shell=False."""
from __future__ import annotations

from components.alert import Alert as AlertCard


class Alert(AlertCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
