"""Page unit — accordion.py → Accordion. Owned kit, shell=False."""
from __future__ import annotations

from components.accordion import Accordion as AccordionCard


class Accordion(AccordionCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
