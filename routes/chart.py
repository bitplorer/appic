"""Page unit — chart.py → Chart. Owned kit, shell=False."""
from __future__ import annotations

from components.chart import Chart as ChartCard


class Chart(ChartCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
