"""Page unit — toast.py → Toast. Owned kit, shell=False."""
from __future__ import annotations

from components.toast import Toast as ToastCard


class Toast(ToastCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
