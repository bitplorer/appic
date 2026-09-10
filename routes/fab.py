"""Page unit — fab.py → Fab. Owned kit, shell=False."""
from __future__ import annotations

from components.fab import Fab as FabCard

from store import HOST

class Fab(FabCard):
    def on_run(self, key: str) -> str:
        HOST.log("fab.run", key, "morph")
        return f"Forge {key}"

    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)

