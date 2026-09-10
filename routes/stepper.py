"""Page unit — stepper.py → Stepper. Owned kit, shell=False."""
from __future__ import annotations

from components.stepper import Stepper as StepperCard


class Stepper(StepperCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
