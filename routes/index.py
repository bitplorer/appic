"""Page unit — index.py → GET /. The Table is a constellation."""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    action,
    act,
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
    svg,
    path,
)
from store import HOST, clock_label

STARS = (
    ("brief", "/brief", "Brief", 18, 20, "Named answers. Submit spends form.submit."),
    ("door", "/login", "Door", 12, 36, "Login + OTP. Secrets on RefState. Caps on the hinge."),
    ("wheel", "/wheel", "Wheel", 32, 14, "Named stage. RPM is RefState. Lift is public."),
    ("glaze", "/glaze", "Glaze", 50, 8, "Named oxide. Load is RefState. Lock spends glaze.lock."),
    ("make", "/commission", "Make", 68, 12, "Clay / glaze / fire. orders.place. Wax seal."),
    ("kiln", "/kiln", "Kiln", 82, 16, "Named band. Remaining heat is Host stock."),
    ("watch", "/watch", "Watch", 94, 32, "Night watch. Keep the shared hearth. Ring the bell."),
    ("air", "/atmosphere", "Air", 78, 38, "Named atmosphere. Cone is RefState. Morph then play."),
    ("vitrine", "/vitrine", "Vitrine", 92, 52, "Drawn work. Rating is a named star."),
    ("hands", "/hands", "Hands", 84, 66, "Studio floor. Log is RefState. role=log."),
    ("house", "/house", "House", 70, 82, "Anchored family. Typeahead hits-slot law."),
    ("hall", "/market", "Hall", 48, 88, "Hero, pricing (bind the button), newsletter."),
    ("forge", "/forge", "Forge", 26, 84, "Chart, tree, diff, mockup."),
    ("edge", "/overlay", "Edge", 10, 70, "OverlayChrome vs anchored family."),
    ("cut", "/cut", "Cut", 8, 52, "Cut C. Empty Content-Type is bad_request."),
    ("boot", "/boot", "Boot", 44, 42, "Channel.boot is the Cap door. Redis wins."),
    ("law", "/docs", "Law", 58, 28, "Written constitution. Swagger off."),
    ("trace", "/trace", "Trace", 74, 50, "Doctor: hard vs teaching vs store-clone."),
    ("press", "/copy", "Press", 62, 70, "copy_component. Not a card."),
    ("charge", "/charge", "Charge", 34, 38, "Intent is a nucleus. Wax is the seal. AttachNote."),
    ("orbit", "/orbit", "Orbit", 54, 58, "A firing is a window. Remaining hours are RefState."),
    ("ship", "/deploy", "Ship", 38, 64, "prepare_deploy. Six providers."),
    ("command", "/command", "Cmd", 22, 48, "OS palette. Query attaches. Not OverlayChrome."),
    ("desk", "/sidebar", "Desk", 16, 8, "Sidebar, Tabs, Command, Toast. Caps off chrome."),
    ("now", "/now", "Now", 50, 62, "Living instrument. Clock, occupancy, resonance, heat trace."),
    ("vessel", "/vessel", "Vessel", 42, 50, "The piece is the house. Presence-continuous with the cradle."),
    ("kintsugi", "/kintsugi", "Mend", 88, 44, "Named break. Brass is the join. repair.join."),
    ("gift", "/gift", "Gift", 96, 72, "Named destination. gift.send. The cradle empties."),
    ("lineage", "/lineage", "Lineage", 28, 56, "Tree of vessels. Host stock. Owned kit, shell=False."),
)

LOOP = ("brief", "wheel", "glaze", "make", "kiln", "watch", "air", "vitrine", "kintsugi", "gift")

BANDS = (("night", "Night"), ("dawn", "Dawn"), ("noon", "Noon"), ("dusk", "Dusk"))


def _filaments(sight: str = "table"):
    """Nucleus at 50,48. Public surface has no `line` tag — paths only."""
    strokes = [
        path(
            d=f"M50 48 L{x} {y}",
            fill="none",
            stroke="currentColor",
            stroke_width="0.55" if key == sight or key in LOOP else "0.35",
            className=" ".join(
                [
                    "filament",
                    f"filament-{key}",
                    "filament-loop" if key in LOOP else "",
                    "filament-on" if key == sight else "",
                ]
            ).strip(),
        )
        for key, _href, _label, x, y, _law in STARS
        if key != "now"
    ]
    return svg(
        *strokes,
        viewBox="0 0 100 100",
        preserveAspectRatio="none",
        className="sky-lines",
        aria_hidden="true",
    )


class Index(Component):
    id = "index"
    sight = MorphState("table")
    greeting = MorphState("The table is lit")
    band = MorphState("night")
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
        if HOST.auto_sky:
            sky = HOST.sync_sky()
        else:
            sky = str(self.band or HOST.sky_band or "night")
        if sky not in {k for k, _ in BANDS}:
            sky = HOST.sync_sky()
        stars = [
            button(
                span("", className="star-dot", aria_hidden="true"),
                span(label, className="star-name"),
                type="button",
                className=" ".join(
                    [
                        "star",
                        "is-on" if self.sight == key else "",
                        "star-loop" if key in LOOP else "",
                        "star-now" if key == "now" else "",
                        "star-vessel" if key == "vessel" else "",
                        "star-kintsugi" if key == "kintsugi" else "",
                    ]
                ).strip(),
                id=f"star-{key}",
                data_room=key,
                title=law,
                **control("index.look", room=key),
            )
            for key, href, label, x, y, law in STARS
        ]
        bands = [
            button(
                label,
                type="button",
                className="seg is-on" if sky == key else "seg",
                **control("index.shift", band=key),
            )
            for key, label in BANDS
        ]
        heat = "The kiln is holding." if HOST.firing else (HOST.notice or "The kiln is quiet.")
        present = [
            li(name, className="chip")
            for name in (HOST.occupied or ["table"])
        ]
        return section(
            div(
                span(
                    f"a house of making · {clock_label(HOST.clock_h)} · {sky} · kit-81 · vessel",
                    className="eyebrow",
                ),
                h1(
                    span(str(self.greeting), className="display"),
                    span("APPIC", className="word-lg"),
                    className="hero-title",
                ),
                p(
                    "A private atelier OS. Sight a star (MorphState), then walk it (Clock A GET). "
                    "The sky is a climate the whole house inhabits. The vessel is an inhabitant. "
                    "Brief → Wheel → Glaze → Make → Kiln → Watch → Air → Vitrine → Mend → Gift. "
                    "The cradle keeps the piece. Brass is the join. Caps are seals.",
                    className="lede",
                ),
                div(
                    act("index.knock", "Pulse the table", kind="primary", target="#index"),
                    a("Open the instrument", href="/now", className="btn-ghost"),
                    a("Sit the watch", href="/watch", className="btn-ghost"),
                    act("index.tick_clock", "Advance the hour", kind="ghost", target="#index"),
                    className="hero-actions",
                ),
                div(*bands, className="segs", role="radiogroup", aria_label="Sky band"),
                status(heat, kind="note"),
                className="hero-copy",
            ),
            div(
                div(
                    _filaments(str(self.sight or "table")),
                    div("", className="nucleus", aria_hidden="true"),
                    *stars,
                    className="sky",
                    id="sky",
                    role="list",
                    data_band=sky,
                    data_sight=str(self.sight or "table"),
                ),
                div(
                    span("sighted", className="eyebrow"),
                    h2(seen[2], className="sight-title"),
                    p(seen[5], className="sight-law"),
                    a("Walk this room", href=seen[1], className="btn-primary"),
                    span("present", className="eyebrow"),
                    ul(*present, className="chips", aria_label="Recent occupancy"),
                    className="sight-card",
                    id="sight",
                ),
                className="constellation",
            ),
            hr(className="rule"),
            dl(
                dt("Pulse"),
                dd(str(kpi["pulse"])),
                dt("Thrown"),
                dd(str(kpi["thrown"])),
                dt("Heat"),
                dd(str(kpi["heat"])),
                dt("Drawn"),
                dd(str(kpi["drawn"])),
                className="kpi",
            ),
            ul(
                li(a("The instrument", href="/now")),
                li(a("The vessel", href="/vessel")),
                li(a("The brief", href="/brief")),
                li(a("The wheel", href="/wheel")),
                li(a("The glaze lab", href="/glaze")),
                li(a("The kiln", href="/kiln")),
                li(a("The night watch", href="/watch")),
                li(a("The air", href="/atmosphere")),
                li(a("The vitrine", href="/vitrine")),
                li(a("Kintsugi", href="/kintsugi")),
                li(a("The gift", href="/gift")),
                li(a("Lineage", href="/lineage")),
                li(a("The written law", href="/docs")),
                className="quick"),
            id=self.id,
            className="table-room",
            data_band=sky,
        )

    @action(caps=())
    def look(self, room: str = "table"):
        keys = {row[0] for row in STARS}
        self.sight = room if room in keys else "table"
        HOST.occupy(str(self.sight))
        HOST.log("index.sight", str(self.sight))
        return update_with(self, optional_plan("sight", "#sight"), extra_ops=[notify(str(self.sight))])

    @action(caps=())
    def shift(self, band: str = "night"):
        keys = {k for k, _ in BANDS}
        self.band = band if band in keys else "night"
        HOST.auto_sky = False
        HOST.sky_band = str(self.band)
        mark_dirty(self)
        HOST.log("index.band", str(self.band))
        return update_with(self, extra_ops=[notify(str(self.band))])

    @action(caps=())
    def tick_clock(self):
        HOST.auto_sky = True
        sky = HOST.tick_clock()
        self.band = sky
        mark_dirty(self)
        HOST.log("index.clock", clock_label(HOST.clock_h))
        HOST.notice = f"The house is {sky} at {clock_label(HOST.clock_h)}."
        return update_with(self, extra_ops=[notify(sky)])

    @action(caps=())
    def knock(self):
        HOST.pulse += 1
        HOST.occupy("table")
        mark_dirty(self)
        self.greeting = "The table heard you"
        HOST.notice = "A pulse crossed the cloth."
        return update_with(self, extra_ops=[notify("pulsed")])
