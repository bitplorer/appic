"""Page unit — typeahead.py → Typeahead. Owned kit, shell=False."""
from __future__ import annotations

from components.typeahead import Typeahead as TypeaheadCard


class Typeahead(TypeaheadCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
