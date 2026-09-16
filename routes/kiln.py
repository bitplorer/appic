"""Page unit — kiln.py → GET /kiln. The firing is a named band, remaining is RefState."""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    button,
    control,
    div,
    h1,
    h2,
    li,
    mark_dirty,
    notify,
    optional_plan,
    p,
    progress,
    section,
    span,
    ul,
    update_with,
)
from store import HOST

BANDS = ("idle", "warm", "soak", "peak", "cool", "done")
BAND_COPY = {
    "idle": "The hearth is dark. Light it when a piece is waiting.",
    "warm": "Bisque rising. Steam leaves the body.",
    "soak": "The glaze is still. Hold the heat.",
    "peak": "The seal is hottest. Do not open the door.",
    "cool": "The fire is leaving. The piece is learning to stay.",
    "done": "Drawn. The wax is spent. Walk it to the hall.",
}
SCHEDULE = (
    ("warm", "Warm", "Steam off the clay."),
    ("soak", "Soak", "Glaze holds still."),
    ("peak", "Peak", "The wax seal is hottest."),
    ("cool", "Cool", "The fire leaves first."),
    ("done", "Drawn", "A piece that stays."),
)


def _band_for(remain: int, firing: bool) -> str:
    if not firing:
        return "idle"
    if remain <= 0:
        return "done"
    if remain <= 2:
        return "cool"
    if remain <= 5:
        return "peak"
    if remain <= 8:
        return "soak"
    return "warm"


class Kiln(Component):
    id = "kiln"
    band = MorphState("idle")
    remain = RefState(0)
    piece = RefState("")
    dirty = MorphState("idle")

    def _n(self) -> int:
        try:
            return max(0, int(self.remain or 0))
        except (TypeError, ValueError):
            return 0

    def _pct(self) -> int:
        n = self._n()
        if str(self.band or "idle") == "idle":
            return 0
        return max(0, min(100, int(((12 - n) / 12) * 100)))

    def render(self):
        band = str(self.band or "idle")
        if band not in BANDS:
            band = "idle"
        n = self._n()
        pct = self._pct()
        piece = str(self.piece or "") or (
            f"{HOST.pending_fire.get('clay')} · {HOST.pending_fire.get('glaze')}"
            if HOST.pending_fire
            else ""
        )
        waiting = bool(HOST.pending_fire) and band == "idle"
        lanes = [
            li(
                span(title, className="card-title"),
                span(body, className="muted"),
                className="fire-lane is-on" if key == band else "fire-lane",
            )
            for key, title, body in SCHEDULE
        ]
        return section(
            span("Kiln", className="eyebrow"),
            h1("Keep the fire overnight.", className="display"),
            p(
                "The band is MorphState. Remaining heat is RefState. "
                "A commission waits on the Host, never on the client plane.",
                className="lede",
            ),
            div(
                div(
                    span("hearth", className="eyebrow"),
                    div("", className="ember", aria_hidden="true"),
                    p(
                        piece or "No piece on the shelf.",
                        className="hearth-piece",
                    ),
                    p(str(n), className="stat", role="timer", aria_live="polite"),
                    p(BAND_COPY.get(band, ""), className="muted"),
                    a("Walk to the vitrine", href="/vitrine", className="btn-ghost") if band == "done" else span(""),
                    className=f"hearth band-{band}",
                    data_band=band,
                    id="hearth",
                ),
                div(
                    span("schedule", className="eyebrow"),
                    h2(band.title(), className="sight-title"),
                    p(BAND_COPY.get(band, ""), className="sight-law"),
                    progress(
                        value=str(pct),
                        max="100",
                        className="fire-bar",
                        role="progressbar",
                        aria_valuemin="0",
                        aria_valuemax="100",
                        aria_valuenow=str(pct),
                        aria_label="Firing progress",
                    ),
                    ul(*lanes, className="fire-lanes", role="list"),
                    div(
                        button(
                            "Light the kiln" if waiting or band == "idle" else "Hold",
                            type="button",
                            className="btn-primary",
                            **control("kiln.light"),
                        ),
                        button(
                            "Advance the fire",
                            type="button",
                            className="btn-ghost",
                            **control("kiln.tick"),
                        ),
                        className="hero-actions",
                    ),
                    className="paper",
                    id="kiln-card",
                ),
                className="kiln-split",
            ),
            id=self.id,
            className="room",
            data_band=band,
        )

    @action(caps=())
    def light(self):
        pending = HOST.pending_fire or HOST.last_firing
        if not pending and HOST.commissions:
            pending = HOST.commissions[-1]
        if not pending:
            HOST.notice = "Commission a piece before the fire."
            return update_with(self, extra_ops=[notify("empty shelf")])
        self.piece = f"{pending.get('clay', 'clay')} · {pending.get('glaze', 'glaze')}"
        self.remain = 12
        self.band = "warm"
        mark_dirty(self)
        HOST.pending_fire = None
        HOST.last_firing = dict(pending)
        HOST.notice = "The kiln is lit."
        HOST.log("kiln.light", str(self.piece))
        return update_with(
            self,
            optional_plan("hearth", "#hearth"),
            extra_ops=[notify("warm")],
        )

    @action(caps=())
    def tick(self):
        if str(self.band or "idle") in ("idle", "done"):
            return update_with(self, extra_ops=[notify(str(self.band or "idle"))])
        n = max(0, self._n() - 1)
        self.remain = n
        self.band = _band_for(n, True)
        mark_dirty(self)
        if self.band == "done":
            HOST.notice = "Drawn from the kiln."
            HOST.log("kiln.drawn", str(self.piece), "cap")
            HOST.draw(
                {
                    "clay": (HOST.last_firing or {}).get("clay", "clay"),
                    "glaze": (HOST.last_firing or {}).get("glaze", "glaze"),
                    "note": (HOST.last_firing or {}).get("note", ""),
                    "band": "done",
                }
            )
        return update_with(
            self,
            optional_plan("hearth", "#hearth"),
            extra_ops=[notify(str(self.band))],
        )
