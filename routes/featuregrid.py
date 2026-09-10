"""Page unit — featuregrid.py → FeatureGrid. Owned kit, shell=False."""
from __future__ import annotations

from components.featuregrid import FeatureGrid as FeatureGridCard


class FeatureGrid(FeatureGridCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
