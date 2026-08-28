"""Page unit: pulse.py → Pulse. Stream payload door. No Document wrap."""
from __future__ import annotations

from appic.store import HOST
from appic.ux import Component


class Pulse(Component):
    id = "pulse"

    def render(self):
        n = int(HOST.pulse or 0)

        def beats():
            yield '<div id="pulse" class="room">'
            for i in range(1, 7):
                yield f'<div id="beat-{i}" class="beat">foundry heartbeat {n + i}</div>\n'
            yield "</div>"

        return beats()
