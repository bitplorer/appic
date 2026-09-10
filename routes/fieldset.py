"""Page unit — fieldset.py → Fieldset. Owned kit, shell=False."""
from __future__ import annotations

from components.fieldset import Fieldset as FieldsetCard


class Fieldset(FieldsetCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
