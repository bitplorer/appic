"""Page unit — datepicker.py → DatePicker. Owned kit, shell=False."""
from __future__ import annotations

from components.datepicker import DatePicker as DatePickerCard


class DatePicker(DatePickerCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
