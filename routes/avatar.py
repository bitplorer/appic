"""Page unit — avatar.py → Avatar. Owned kit, shell=False."""
from __future__ import annotations

from components.avatar import Avatar as AvatarCard


class Avatar(AvatarCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
