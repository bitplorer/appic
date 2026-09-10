"""Page unit — pagination.py → Pagination. Owned kit, shell=False."""
from __future__ import annotations

from components.pagination import Pagination as PaginationCard


class Pagination(PaginationCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
