"""Page unit — carousel.py → Carousel. Owned kit, shell=False."""
from __future__ import annotations

from components.carousel import Carousel as CarouselCard


class Carousel(CarouselCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
