"""Page unit — rating.py → Rating. Owned kit, shell=False."""
from __future__ import annotations

from components.rating import Rating as RatingCard


class Rating(RatingCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
