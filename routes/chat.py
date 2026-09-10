"""Page unit — chat.py → Chat. Owned kit, shell=False."""
from __future__ import annotations

from components.chat import Chat as ChatCard


class Chat(ChatCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
