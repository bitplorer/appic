"""Page unit — diff.py → Diff. Owned kit, shell=False."""
from __future__ import annotations

from components.diff import Diff as DiffCard


class Diff(DiffCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
