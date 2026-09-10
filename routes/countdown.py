"""Page unit — countdown.py → Countdown. Owned kit, shell=False."""
from __future__ import annotations

from components.countdown import Countdown as CountdownCard


class Countdown(CountdownCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
