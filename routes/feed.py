"""Page unit — feed.py → Feed. Owned kit, shell=False."""
from __future__ import annotations

from components.feed import Feed as FeedCard


class Feed(FeedCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
