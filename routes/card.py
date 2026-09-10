"""Page unit — card.py → Card. Owned kit, shell=False."""
from __future__ import annotations

from components.card import Card as CardCard


class Card(CardCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
