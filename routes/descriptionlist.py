"""Page unit — descriptionlist.py → DescriptionList. Owned kit, shell=False."""
from __future__ import annotations

from components.descriptionlist import DescriptionList as DescriptionListCard


class DescriptionList(DescriptionListCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
