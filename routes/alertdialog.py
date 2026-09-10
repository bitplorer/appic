"""Page unit — alertdialog.py → AlertDialog. Owned kit, shell=False."""
from __future__ import annotations

from components.alertdialog import AlertDialog as AlertDialogCard

from store import HOST

class AlertDialog(AlertDialogCard):
    def on_confirm(self) -> str:
        HOST.log("alertdialog.confirm", "wipe", "cap")
        return "The kiln is cold."

    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)

