"""Page unit — searchbar.py → SearchBar. Owned kit, shell=False."""
from __future__ import annotations

from components.searchbar import SearchBar as SearchBarCard


class SearchBar(SearchBarCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
