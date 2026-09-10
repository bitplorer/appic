"""Page unit — newsletter.py → Newsletter. Owned kit, shell=False."""
from __future__ import annotations

from components.newsletter import Newsletter as NewsletterCard

from store import HOST

class Newsletter(NewsletterCard):
    def on_join(self, email: str) -> str:
        HOST.log("list.subscribe", email, "cap")
        return f"The letter will find {email}"

    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)

