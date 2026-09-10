"""Page unit — contextmenu.py → ContextMenu. Owned kit, shell=False."""
from __future__ import annotations

from components.contextmenu import ContextMenu as ContextMenuCard

from store import HOST

class ContextMenu(ContextMenuCard):
    def on_run(self, key: str) -> str:
        HOST.log("contextmenu.run", key, "morph")
        return f"Kept {key}"

    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)

