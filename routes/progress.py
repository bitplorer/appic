"""Page unit — progress.py → Progress. Owned kit, shell=False."""
from __future__ import annotations

from components.progress import Progress as ProgressCard


class Progress(ProgressCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
