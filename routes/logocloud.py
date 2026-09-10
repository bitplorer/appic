"""Page unit — logocloud.py → LogoCloud. Owned kit, shell=False."""
from __future__ import annotations

from components.logocloud import LogoCloud as LogoCloudCard


class LogoCloud(LogoCloudCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
