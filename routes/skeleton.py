"""Page unit — skeleton.py → Skeleton. Owned kit, shell=False."""
from __future__ import annotations

from components.skeleton import Skeleton as SkeletonCard


class Skeleton(SkeletonCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
