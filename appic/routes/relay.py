"""Page unit: relay.py → Relay. Serve clocks made visible.

Soft morph is the happy path. Hard reload is the fallback.
restart-channel is an action, not a flag. Isolation: no ux_channel.
"""
from __future__ import annotations

from appic.rooms import hero
from appic.ux import (
    Component,
    MorphState,
    action,
    article,
    bind,
    button,
    div,
    h2,
    p,
    span,
    update_with,
)

try:
    from ux_compose.hmr import HMR_PATH
except Exception:  # pragma: no cover
    HMR_PATH = "/__uxcompose/hmr"

try:
    from ux_compose.assets import CSS_URL_PREFIX, OUTPUT_CSS_NAME
except Exception:  # pragma: no cover
    CSS_URL_PREFIX = "/css"
    OUTPUT_CSS_NAME = "output.css"

CLOCKS = (
    (
        "process",
        "Process",
        "uvicorn --reload on *.py. New worker, cold import, new page class. Owned by serve dev.",
    ),
    (
        "hmr",
        "Browser HMR",
        f"WebSocket at {HMR_PATH}. Morph page-unit ids. location.reload() only if morph fails.",
    ),
    (
        "css",
        "CSS watch",
        f"Sibling Tailwind --watch writes {OUTPUT_CSS_NAME}. Client HEAD-polls {CSS_URL_PREFIX}/{OUTPUT_CSS_NAME}. CSS save does not kill the worker.",
    ),
)

MODES = (
    ("dev", "serve dev", "origin + ui + channel + CSS watch. Daily author path."),
    ("prod", "serve prod", "clocks hard off. One uvicorn. Disk CSS. Does not replace deploy."),
    ("drop", "restart-channel", "One-shot SIGUSR1. Drops Channel RAM. Next *.py save still leaves Channel up."),
)


class Relay(Component):
    id = "relay"
    band = MorphState("dev")
    pulse = MorphState("idle")

    def render(self):
        rings = [
            article(
                span(title, className="kicker"),
                h2(title),
                p(body),
                className=f"clock-ring clock-{key}" + (" is-live" if self.band == key or key == "hmr" else ""),
                id=f"relay-{key}",
            )
            for key, title, body in CLOCKS
        ]
        doors = [
            button(
                title,
                type="button",
                className="btn" + (" btn-solid" if self.band == key else " btn-ghost"),
                **bind(self.choose, band=key),
            )
            for key, title, _ in MODES
        ]
        chosen = next((body for key, _, body in MODES if key == self.band), MODES[0][2])
        return div(
            hero(
                "Relay",
                "Three clocks. One foundry. Soft morph first.",
                "A .py save morphs matching [id]s. Hard reload is the fallback, never the happy path. Channel RAM drops only when you ask.",
            ),
            div(*rings, className="clock-pair relay-clocks"),
            div(
                article(
                    h2("Modes — not a flag soup"),
                    p("uxcompose serve without a mode exits 2. There is no --hmr, --css-watch, or --one-process."),
                    div(*doors, className="relay-doors"),
                    p(chosen, className="lede", id="relay-mode-copy"),
                    className="gate",
                    id="relay-modes",
                ),
                article(
                    h2("Soft morph"),
                    p("Idiomorph morphs document.body. Else replace live nodes whose id is in the new HTML. Else hard reload."),
                    p("Focus, selection, and scroll restore by id, else name."),
                    className="gate",
                    id="relay-morph",
                ),
                article(
                    h2("restart-channel"),
                    p("Not a sticky clock. One SIGUSR1 to the origin pidfile. Missing pidfile fails closed."),
                    button("Drop Channel RAM", type="button", **bind(self.drop)),
                    p(f"HMR_PATH {HMR_PATH}", className="mono"),
                    p(f"sheet {CSS_URL_PREFIX}/{OUTPUT_CSS_NAME}", className="mono"),
                    p(f"pulse {self.pulse}", className="mono", id="relay-pulse"),
                    className="gate",
                    id="relay-drop",
                ),
                className="gate-row",
            ),
            id=self.id,
            className="room",
        )

    @action(caps=())
    def choose(self, band: str = "dev"):
        if band not in {k for k, _, _ in MODES}:
            band = "dev"
        self.band = band
        self.pulse = "tock" if self.pulse == "tick" else "tick"
        return update_with(self)

    @action(caps=())
    def drop(self):
        self.pulse = "dropped"
        self.band = "drop"
        return update_with(self)
