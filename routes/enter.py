"""Page unit — Door room. Login and OTP live as kit rooms; this is the hinge."""
from __future__ import annotations

from ux_compose import Component, a, div, h1, p, section, span

from store import HOST


class Enter(Component):
    id = "enter"

    def render(self):
        who = HOST.authed or "a guest"
        return section(
            span("Door", className="eyebrow"),
            h1("Come in.", className="display"),
            p(
                f"The house currently knows {who}. Sign-in is a card. "
                "The six digits spend auth.otp. Secrets never sit on MorphState.",
                className="lede",
            ),
            div(
                a("Sign in", href="/login", className="btn-primary"),
                a("Hold the seal", href="/otp", className="btn-ghost"),
                a("User menu", href="/usermenu", className="btn-ghost"),
                className="hero-actions",
            ),
            id=self.id,
            className="room",
        )
