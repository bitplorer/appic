"""Page unit: enter.py → Enter. Door: owned Login + Otp."""
from __future__ import annotations

from appic.rooms import room
from appic.ux import Component, MorphState, action, update_with


class Enter(Component):
    id = "enter"
    lit = MorphState("closed")

    def render(self):
        return room(
            "Door",
            "Caps keep the threshold.",
            "Sign in spends auth.login. Six digits spend auth.otp. @blocked.test is refused. 000000 is refused.",
            "login",
            "otp",
            rid=self.id,
        )

    @action(caps=())
    def knock(self):
        self.lit = "open" if self.lit != "open" else "closed"
        return update_with(self)
