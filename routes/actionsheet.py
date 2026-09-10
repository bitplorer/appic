"""Page unit — actionsheet.py → ActionSheet. Owned kit, shell=False."""
from __future__ import annotations

from components.actionsheet import ActionSheet as ActionSheetCard


class ActionSheet(ActionSheetCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
