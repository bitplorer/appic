"""Page unit — otp.py → Otp. Owned kit, shell=False."""
from __future__ import annotations

from components.otp import Otp as OtpCard

from store import HOST

class Otp(OtpCard):
    def on_verify(self, code: str) -> str | None:
        digits = "".join(c for c in (code or "") if c.isdigit())
        if digits == "000000":
            HOST.log("otp.verify", "refused", "cap")
            return None
        HOST.log("otp.verify", digits, "cap")
        return "The seal is warm."

    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)

