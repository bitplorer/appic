"""Page unit — colorpicker.py → ColorPicker. Owned kit, shell=False."""
from __future__ import annotations

from components.colorpicker import ColorPicker as ColorPickerCard


class ColorPicker(ColorPickerCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
