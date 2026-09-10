"""Door — Login + OTP. Secrets stay on RefState. Submit is a Cap."""
from __future__ import annotations

from foundry import kit_tree
from ux_compose import Component, a, div, h1, p, section, span


class Enter(Component):
    id = "enter"

    def render(self):
        return section(
            span("the door", className="kicker"),
            h1("Enter"),
            p(
                "Mode tabs are MorphState. Email, password, and OTP digits live on RefState. "
                "Submit spends auth.login. Reveal is public. Try any valid email and eight letters, "
                "or @blocked.test to feel a refused Cap.",
                className="lede",
            ),
            div(kit_tree("login"), kit_tree("otp"), className="stack-paper"),
            a("Back to the table", href="/", className="btn-ghost"),
            id=self.id,
            className="page",
        )
