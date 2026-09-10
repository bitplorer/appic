"""Page unit — emptystate.py → EmptyState. Owned kit, shell=False."""
from __future__ import annotations

from components.emptystate import EmptyState as EmptyStateCard


class EmptyState(EmptyStateCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
