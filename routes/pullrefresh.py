"""Page unit — pullrefresh.py → PullRefresh. Owned kit, shell=False."""
from __future__ import annotations

from components.pullrefresh import PullRefresh as PullRefreshCard


class PullRefresh(PullRefreshCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
