"""Page unit — plans.py → Plans. Owned kit, shell=False."""
from __future__ import annotations

from components.plans import Plans as PlansCard

from store import HOST

class Plans(PlansCard):
    def on_choose(self, key: str) -> str:
        HOST.log("plans.choose", key, "morph")
        return f"Chose {key}"

    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)

