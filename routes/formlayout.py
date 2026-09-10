"""Page unit — formlayout.py → FormLayout. Owned kit, shell=False."""
from __future__ import annotations

from components.formlayout import FormLayout as FormLayoutCard


class FormLayout(FormLayoutCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
