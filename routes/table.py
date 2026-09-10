"""Page unit — table.py → Table. Owned kit, shell=False."""
from __future__ import annotations

from components.table import Table as TableCard


class Table(TableCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
