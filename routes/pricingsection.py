"""Page unit — pricingsection.py → PricingSection. Owned kit, shell=False."""
from __future__ import annotations

from components.pricingsection import PricingSection as PricingSectionCard


class PricingSection(PricingSectionCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
