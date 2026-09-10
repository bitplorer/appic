"""Page unit — footer.py → Footer. Owned kit, shell=False."""
from __future__ import annotations

from components.footer import Footer as FooterCard


class Footer(FooterCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
