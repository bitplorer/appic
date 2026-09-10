"""Page unit — attachment.py → Attachment. Owned kit, shell=False."""
from __future__ import annotations

from components.attachment import Attachment as AttachmentCard


class Attachment(AttachmentCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
