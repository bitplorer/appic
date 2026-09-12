"""Page unit — GET /boot. Channel.boot is the Cap door. Redis wins."""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    control,
    div,
    h1,
    h2,
    p,
    section,
    span,
    article,
    dl,
    dt,
    dd,
    mark_dirty,
    notify,
    optional_fade,
    status,
    update_with,
    button,
    AttachNote,
    attach_notes,
)
from ux_compose.doctor import scan_store_precedence, scan_store_clone
from pathlib import Path

from store import HOST


DOORS = (
    ("cap", "Cap door", "Channel.boot is the compose door. Not ActionRegistry.from_config. wire/ frozen imports only."),
    ("redis", "Redis wins", "Channel prefers REDIS_URL. UXCOMPOSE_STATE_STORE is ignored when Redis is set. Do not export both."),
    ("sqlite", "FileStateStore", "When REDIS_URL is unset, compose prepares one sqlite path. Channel.boot opens Channel's store."),
    ("clone", "Store clone", "Doctor scan_store_clone fails closed if FileStateStore reappears in the product tree."),
)


class Boot(Component):
    id = "boot"
    sight = MorphState("cap")
    knocks = RefState(0)
    dirty = MorphState("idle")

    def _row(self):
        key = str(self.sight or "cap")
        for row in DOORS:
            if row[0] == key:
                return row
        return DOORS[0]

    def render(self):
        seen = self._row()
        n = int(self.knocks or 0)
        root = Path(__file__).resolve().parents[1]
        product_py = [
            str(p)
            for p in root.rglob("*.py")
            if "site-packages" not in str(p) and "/.venv/" not in str(p)
        ]
        clone_hits = scan_store_clone(product_py)
        prec_hits = scan_store_precedence()
        notes = list(attach_notes() or ())
        if not notes:
            notes = [
                AttachNote(
                    door="Channel.boot",
                    wanted="cek-runtime Cap Host",
                    reason="build(cek='require') after use_channel",
                    level_kept=2,
                )
            ]
        chips = [
            button(
                label,
                type="button",
                className="room-link is-on" if self.sight == key else "room-link",
                data_room=key,
                **control("boot.look", room=key),
            )
            for key, label, _ in DOORS
        ]
        return section(
            span("Boot", className="eyebrow"),
            h1("The door is Channel.boot.", className="display"),
            p(
                "Cap door honesty after channel #27. attach_cek still calls apply_host_adapter. "
                "Do not assume classic CapService when cek=require. Isolation: product never imports ux_channel.",
                className="lede",
            ),
            div(*chips, className="hero-actions"),
            article(
                span("sighted", className="eyebrow"),
                h2(seen[1], className="sight-title"),
                p(seen[2], className="sight-law"),
                status(HOST.notice or "The hinge is quiet.", kind="note"),
                className="paper",
                id="boot-sight",
            ),
            dl(
                dt("Knocks"),
                dd(str(n)),
                dt("store-clone"),
                dd("clean" if not clone_hits else str(len(clone_hits))),
                dt("precedence"),
                dd("clean" if not prec_hits else "both set"),
                dt("notes"),
                dd(str(len(notes))),
                className="kpi",
            ),
            div(
                button("Knock the door", type="button", className="btn-primary", **control("boot.knock")),
                className="hero-actions",
            ),
            p(
                notes[0].door + " · " + notes[0].wanted + " · " + notes[0].reason,
                className="lede",
            ),
            id=self.id,
            className="room",
        )

    @action(caps=())
    def look(self, room: str = "cap"):
        keys = {row[0] for row in DOORS}
        self.sight = room if room in keys else "cap"
        HOST.log("boot.look", str(self.sight))
        return update_with(
            self,
            optional_fade("boot-sight", "#boot-sight"),
            extra_ops=[notify(str(self.sight))],
        )

    @action(caps=())
    def knock(self):
        self.knocks = int(self.knocks or 0) + 1
        mark_dirty(self)
        HOST.notice = "Channel.boot holds the hinge."
        HOST.log("boot.knock", "cap-door")
        return update_with(self, extra_ops=[notify("knock")])
