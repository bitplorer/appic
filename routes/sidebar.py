"""Page unit — sidebar.py → Sidebar. Owned kit, shell=False."""
from __future__ import annotations

from components.sidebar import Sidebar as SidebarCard


class Sidebar(SidebarCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
