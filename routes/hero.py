"""Page unit — hero.py → Hero. Owned kit, shell=False."""
from __future__ import annotations

from components.hero import Hero as HeroCard


class Hero(HeroCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
