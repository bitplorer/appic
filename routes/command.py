"""Page unit — command.py → Command. Owned kit, shell=False."""
from __future__ import annotations

from components.command import Command as CommandCard

from store import HOST

class Command(CommandCard):
    def on_run(self, key: str) -> str:
        HOST.log("command.run", key, "morph")
        return f"Ran {key}"

    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)

