"""Page unit — dialog.py → Dialog. Owned kit, shell=False."""
from __future__ import annotations

from components.dialog import Dialog as DialogCard

from store import HOST

class Dialog(DialogCard):
    TITLE = "Break the piece?"
    BODY = "Confirm spends items.delete. Escape and scrim dismiss. Swipe lives on Keep."

    def on_confirm(self, target: str) -> str:
        HOST.log("dialog.confirm", target or "piece", "cap")
        return "The piece is gone."

    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)

