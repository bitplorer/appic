"""Page unit — slider.py → Slider. Owned kit, shell=False."""
from __future__ import annotations

from components.slider import Slider as SliderCard


class Slider(SliderCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
