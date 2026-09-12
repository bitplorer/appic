"""Page unit — index.py → GET /. The Table is a constellation."""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    act,
    bind,
    button,
    control,
    div,
    h1,
    h2,
    mark_dirty,
    notify,
    optional_plan,
    p,
    section,
    span,
    status,
    update_with,
    a,
    ul,
    li,
    dl,
    dt,
    dd,
    hr,
)
from store import HOST

STARS = (
    ("door", "/login", "Door", 12, 22, "Login + OTP. Secrets on RefState. Caps on the hinge."),
    ("desk", "/sidebar", "Desk", 30, 10, "Sidebar, Tabs, Command, Toast. Caps off chrome."),
    ("house", "/house", "House", 52, 8, "Anchored family. Typeahead hits-slot law."),
    ("visit", "/visit", "Visit", 74, 16, "Stepper, Plans, Calendar, Dialog confirm."),
    ("signal", "/typeahead", "Signal", 90, 32, "Wave 1. delay:300 · longpress · swipe."),
    ("author", "/author", "Author", 92, 54, "act / mark_dirty / field / optional_*."),
    ("press", "/copy", "Press", 80, 76, "copy_component. Not a card."),
    ("skin", "/skin", "Skin", 62, 88, "WebAssets. ETag. dual_copy leftover."),
    ("ship", "/deploy", "Ship", 42, 86, "prepare_deploy. Six providers."),
    ("chrome", "/overlay", "Edge", 22, 80, "OverlayChrome vs anchored family."),
    ("notes", "/notes", "Notes", 8, 62, "AttachNote. Silence was the defect."),
    ("atelier", "/atelier", "Atelier", 16, 44, "Presence. Kit Cut 1 shell=False."),
    ("lattice", "/lattice", "Lattice", 38, 30, "Surfaces. Caps as seals."),
    ("trace", "/trace", "Trace", 58, 20, "Doctor. Hard vs teaching vs store-clone."),
    ("clocks", "/clocks", "Clocks", 70, 44, "GET is Clock A. Action is Clock B."),
    ("forge", "/forge", "Forge", 48, 58, "Chart · Tree · Diff · Mockup."),
    ("kiln", "/countdown", "Kiln", 28, 70, "Countdown remaining is RefState."),
    ("market", "/market", "Hall", 84, 18, "Hero · Pricing · LogoCloud · Newsletter."),
    ("cut", "/cut", "Cut", 6, 38, "Cut C. Empty Content-Type is bad_request."),
    ("boot", "/boot", "Boot", 44, 42, "Channel.boot is the Cap door. Redis wins."),
)


class Index(Component):
    id = "index"
    sight = MorphState("table")
    greeting = MorphState("The table is lit")
    dirty = MorphState("idle")

    def _star(self):
        key = str(self.sight or "table")
        for row in STARS:
            if row[0] == key:
                return row
        return ("table", "/", "Table", 50, 50, "The document is the composition root made visible.")

    def render(self):
        seen = self._star()
        kpi = HOST.kpi()
        stars = [
            button(
                span("", className="star-dot", aria_hidden="true"),
                span(label, className="star-name"),
                type="button",
                className="star is-on" if self.sight == key else "star",
                id=f"star-{key}",
                data_room=key,
                title=law,
                **control("index.look", room=key),
            )
            for key, href, label, x, y, law in STARS
        ]
        return section(
            div(
                span("nocturnal foundry · ux-compose 0.1.0 · kit-81 · Cut C", className="eyebrow"),
                h1(
                    span(str(self.greeting), className="display"),
                    span("APPIC", className="word-lg"),
                    className="hero-title",
                ),
                p(
                    "A constitution you can walk. Sight a star (MorphState), then walk it (Clock A GET). "
                    "Caps are wax seals. Channel.boot is the hinge. Empty Content-Type is bad_request.",
                    className="lede",
                ),
                div(
                    act("index.knock", "Pulse the table", kind="primary", target="#index"),
                    a("Open the door", href="/enter", className="btn-ghost"),
                    a("Commission a piece", href="/commission", className="btn-ghost"),
                    className="hero-actions",
                ),
                status(HOST.notice or "The kiln is quiet.", kind="note"),
                className="hero-copy",
            ),
            div(
                div(*stars, className="sky", id="sky", role="list"),
                div(
                    span("sighted", className="eyebrow"),
                    h2(seen[2], className="sight-title"),
                    p(seen[5], className="sight-law"),
                    a("Walk this room", href=seen[1], className="btn-primary"),
                    className="sight-card",
                    id="sight",
                ),
                className="constellation",
            ),
            hr(className="rule"),
            dl(
                dt("Pulse"),
                dd(str(kpi["pulse"])),
                dt("Bag"),
                dd(str(kpi["bag"])),
                dt("Seals spent"),
                dd(str(kpi["seals"])),
                dt("Commissions"),
                dd(str(kpi["commissions"])),
                className="kpi",
            ),
            ul(
                li(a("81 kit rooms", href="/house")),
                li(a("Doctor residuals", href="/trace")),
                li(a("The written law", href="/docs")),
                li(a("Clock A / Clock B", href="/clocks")),
                li(a("Cut C type seal", href="/cut")),
                li(a("Channel.boot", href="/boot")),
                className="quick"),
            id=self.id,
            className="table-room",
        )

    @action(caps=())
    def look(self, room: str = "table"):
        keys = {row[0] for row in STARS}
        self.sight = room if room in keys else "table"
        HOST.log("index.sight", str(self.sight))
        return update_with(self, optional_plan("sight", "#sight"), extra_ops=[notify(str(self.sight))])

    @action(caps=())
    def knock(self):
        HOST.pulse += 1
        mark_dirty(self)
        self.greeting = "The table heard you"
        HOST.notice = "A pulse crossed the cloth."
        return update_with(self, extra_ops=[notify("pulsed")])
