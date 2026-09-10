"""Page unit — stats.py → Stats. Owned kit, shell=False."""
from __future__ import annotations

from components.stats import Stats as StatsCard


class Stats(StatsCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
