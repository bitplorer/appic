"""Page unit — mockup.py → Mockup. Owned kit, shell=False."""
from __future__ import annotations

from components.mockup import Mockup as MockupCard


class Mockup(MockupCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
