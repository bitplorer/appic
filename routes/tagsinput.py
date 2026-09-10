"""Page unit — tagsinput.py → TagsInput. Owned kit, shell=False."""
from __future__ import annotations

from components.tagsinput import TagsInput as TagsInputCard


class TagsInput(TagsInputCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
