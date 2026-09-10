"""Page unit — questionnaire.py → Questionnaire. Owned kit, shell=False."""
from __future__ import annotations

from components.questionnaire import Questionnaire as QuestionnaireCard


class Questionnaire(QuestionnaireCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
