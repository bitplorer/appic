"""Page unit — fileupload.py → FileUpload. Owned kit, shell=False."""
from __future__ import annotations

from components.fileupload import FileUpload as FileUploadCard


class FileUpload(FileUploadCard):
    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)
