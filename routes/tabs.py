"""Page unit — tabs.py → Tabs. Owned kit, shell=False."""
from __future__ import annotations

from components.tabs import Tabs as TabsCard


class Tabs(TabsCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
