"""Page unit — banner.py → Banner. Owned kit, shell=False."""
from __future__ import annotations

from components.banner import Banner as BannerCard


class Banner(BannerCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
