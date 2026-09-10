"""Page unit — badge.py → Badge. Owned kit, shell=False."""
from __future__ import annotations

from components.badge import Badge as BadgeCard


class Badge(BadgeCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
