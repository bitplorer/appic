"""Page unit — tree.py → Tree. Owned kit, shell=False."""
from __future__ import annotations

from components.tree import Tree as TreeCard


class Tree(TreeCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
