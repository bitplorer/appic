"""Page unit — cta.py → Cta. Owned kit, shell=False."""
from __future__ import annotations

from components.cta import Cta as CtaCard


class Cta(CtaCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
