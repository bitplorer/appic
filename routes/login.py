"""Page unit — login.py → Login. Owned kit, shell=False."""
from __future__ import annotations

from components.login import Login as LoginCard

from components.login import AuthDecision
from store import HOST

class Login(LoginCard):
    TITLE = "The door"
    BODY = "Secrets never sit on MorphState. Submit spends auth.login."

    def authenticate(self, *, email: str, password: str, name: str, signup: bool) -> AuthDecision:
        if (email or "").lower().endswith("@blocked.test"):
            HOST.log("login.authenticate", "blocked", "cap")
            return AuthDecision(ok=False, message="This account is not allowed at the door.", blocked=True)
        HOST.authed = email
        HOST.notice = email
        HOST.log("login.authenticate", email, "cap")
        return AuthDecision(ok=True, message="The door opened" if not signup else "The house wrote your name")

    def render(self, *, shell=None, **slots):
        return super().render(shell=False, **slots)

