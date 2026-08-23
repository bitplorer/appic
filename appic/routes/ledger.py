"""Page unit: ledger.py → Ledger — calendar Cap, KPI, settings Cap, doctor."""
from __future__ import annotations

from appic.store import HOST
from appic.ux import (
    Component,
    MorphState,
    RefState,
    action,
    act,
    article,
    div,
    doctor,
    h1,
    h2,
    h3,
    li,
    maybe_plan,
    notify,
    p,
    section,
    span,
    tick,
    ul,
    update_with,
)

MONTHS = (("july", "July"), ("august", "August"), ("september", "September"))
DAYS = (14, 15, 20, 21, 27)


class Ledger(Component):
    id = "ledger"
    month = MorphState("august")
    day = RefState(20)
    copied = MorphState(False)
    phase = MorphState("hold")
    pct = RefState(42)
    stamp = MorphState("idle")

    def render(self):
        report = doctor([], fail=False)
        caps = report.capabilities or {}
        month = str(self.month or "august")
        day = int(self.day or 20)
        booked = set(int(x) for x in (HOST.booked or ()))
        months = [
            act("ledger.set_month", lab, kind="chip-on" if key == month else "chip", key=key)
            for key, lab in MONTHS
        ]
        cells = [
            act(
                "ledger.pick",
                f"{d}{' ·' if d in booked else ''}",
                kind="chip-on" if d == day else "chip",
                n=str(d),
            )
            for d in DAYS
        ]
        cap_rows = [
            li(
                span(k, className="mono"),
                span("on" if v else "off", className="chip" + (" is-on" if v else "")),
                className="spread cap-row",
            )
            for k, v in caps.items()
        ]
        teaching = [li(t) for t in (report.teaching or [])[:4]]
        k = HOST.kpi
        return section(
            div(
                h1("Ledger"),
                p("Named month. Day silent. Book, wipe, and doctor sit on this table.", className="muted"),
                className="section-head",
            ),
            div(
                article(
                    p("Bench", className="kicker"),
                    h2("Calendar"),
                    div(*months, className="chip-row"),
                    div(*cells, className="chip-row"),
                    act("ledger.book", "Book this bench", kind="primary"),
                    p(f"Held {sorted(booked)} in {month}", className="muted tiny"),
                    className="card stack",
                ),
                article(
                    p("Derived", className="kicker"),
                    h2("House KPI"),
                    div(
                        _kpi("Open", k["open"]),
                        _kpi("Fired", k["fired"]),
                        _kpi("Held", k["held"]),
                        _kpi("Placed", k["placed"]),
                        className="kpi-row",
                    ),
                    p(f"Progress {int(self.pct)}% · {self.phase}", className="mono"),
                    div(
                        act("ledger.advance", "Advance fire", kind="ghost"),
                        act("ledger.copy", "Copy house id" if not self.copied else "Copied", kind="text"),
                        className="row",
                    ),
                    className="card stack",
                ),
                className="split",
            ),
            div(
                article(
                    p("Doctor", className="kicker"),
                    h2("Capabilities"),
                    ul(*cap_rows, className="cap-list"),
                    p(f"L{report.level_available} · ok={report.ok}", className="mono"),
                    className="card stack",
                ),
                article(
                    p("Teaching", className="kicker"),
                    h2("Unlocks"),
                    ul(*teaching, className="hit-list") if teaching else p("Full stack available.", className="muted"),
                    className="card stack",
                ),
                className="split",
            ),
            article(
                p("Settings", className="kicker"),
                h2("House"),
                div(
                    act("ledger.set_locale", "EN", kind="chip-on" if HOST.locale == "en" else "chip", key="en"),
                    act("ledger.set_locale", "FR", kind="chip-on" if HOST.locale == "fr" else "chip", key="fr"),
                    act("ledger.set_density", "Room", kind="chip-on" if HOST.density == "room" else "chip", key="room"),
                    act("ledger.set_density", "Tight", kind="chip-on" if HOST.density == "tight" else "chip", key="tight"),
                    act("ledger.set_motion", "Present", kind="chip-on" if HOST.motion == "present" else "chip", key="present"),
                    act("ledger.set_motion", "Still", kind="chip-on" if HOST.motion == "still" else "chip", key="still"),
                    act("ledger.toggle_consent", "Consent on" if HOST.consent else "Consent off", kind="chip-on" if HOST.consent else "chip"),
                    act("ledger.toggle_line", "Online" if HOST.online else "Offline", kind="chip-on" if HOST.online else "chip"),
                    className="chip-row",
                ),
                act("ledger.wipe", "Wipe local house", kind="danger"),
                p("Wipe is a Cap. Isolation: this module never imports the wire.", className="muted tiny"),
                className="card stack",
            ),
            id=self.id,
            className="page",
        )

    @action(caps=())
    def set_month(self, key: str = "august", **kwargs):
        self.month = key
        return update_with(self)

    @action(caps=())
    def pick(self, n: str = "20", **kwargs):
        self.day = int(n or 20)
        tick(self)
        return update_with(self)

    @action(caps=("calendar.book",))
    def book(self, **kwargs):
        d = int(self.day or 20)
        if d not in HOST.booked:
            HOST.booked.append(d)
        tick(self)
        return update_with(self, maybe_plan("book", "#ledger", ms=140), extra_ops=[notify(f"Booked {self.month} {d}")])

    @action(caps=())
    def advance(self, **kwargs):
        self.pct = min(100, int(self.pct or 0) + 8)
        self.phase = "fire" if self.pct >= 70 else "hold"
        tick(self)
        return update_with(self)

    @action(caps=())
    def copy(self, **kwargs):
        self.copied = True
        return update_with(self, extra_ops=[notify("appic-house-01")])

    @action(caps=())
    def set_locale(self, key: str = "en", **kwargs):
        HOST.locale = key
        return update_with(self)

    @action(caps=())
    def set_density(self, key: str = "room", **kwargs):
        HOST.density = key
        return update_with(self)

    @action(caps=())
    def set_motion(self, key: str = "present", **kwargs):
        HOST.motion = key
        return update_with(self)

    @action(caps=())
    def toggle_consent(self, **kwargs):
        HOST.consent = not HOST.consent
        return update_with(self)

    @action(caps=())
    def toggle_line(self, **kwargs):
        HOST.online = not HOST.online
        return update_with(self, extra_ops=[notify("Online" if HOST.online else "Offline")])

    @action(caps=("settings.wipe",))
    def wipe(self, **kwargs):
        HOST.lines = []
        HOST.wishlist = []
        HOST.compare = []
        HOST.notice = "House wiped"
        tick(self)
        return update_with(self, extra_ops=[notify("Wiped")])


def _kpi(label: str, n: int):
    return div(
        span(str(n), className="kpi-n"),
        span(label, className="kpi-l"),
        className="kpi",
    )
