"""Page unit — timeline.py → Timeline. Owned kit, shell=False."""
from __future__ import annotations

from components.timeline import Timeline as TimelineCard


class Timeline(TimelineCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
