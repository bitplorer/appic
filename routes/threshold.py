"""Page unit — threshold.py → GET /threshold.

Surfaces as doors. scan_surfaces + validate_surfaces + RouterHooks evidence.
THRESHOLD-1. Walking a door is Clock A. This is not the lattice of names.
"""
from __future__ import annotations

from pathlib import Path

from ux_compose import (
    Component,
    MorphState,
    RouterHooks,
    SurfaceError,
    a,
    action,
    button,
    control,
    div,
    h1,
    h2,
    li,
    mark_dirty,
    notify,
    p,
    scan_surfaces,
    section,
    span,
    ul,
    update_with,
    validate_surfaces,
)
from store import HOST

ROOT = Path(__file__).resolve().parent.parent

HOUSE_DOORS = (
    ("/", "Table", "index"),
    ("/score", "Score", "score"),
    ("/chorus", "Chorus", "chorus"),
    ("/eclipse", "Eclipse", "eclipse"),
    ("/duet", "Duet", "duet"),
    ("/provenance", "Seals", "provenance"),
    ("/vessel", "Vessel", "vessel"),
    ("/now", "Now", "now"),
    ("/watch", "Watch", "watch"),
    ("/docs", "Law", "docs"),
)


def _catalog() -> tuple[list, list[str], str]:
    try:
        surfaces = scan_surfaces(ROOT, base_directory="routes", fail_closed=False)
        errors = validate_surfaces(surfaces, fail=False)
        pages = [s for s in surfaces if getattr(s, "is_page", False)]
        return pages, list(errors or ()), ""
    except SurfaceError as exc:
        return [], list(getattr(exc, "errors", None) or [str(exc)]), str(exc)
    except Exception as exc:
        return [], [], type(exc).__name__


class Threshold(Component):
    id = "threshold"
    door = MorphState("score")
    dirty = MorphState("idle")

    def render(self):
        HOST.occupy("threshold")
        pages, errors, err = _catalog()
        n = len(pages)
        n_act = sum(len(getattr(s, "actions", ()) or ()) for s in pages)
        hooks = list(getattr(RouterHooks, "__slots__", ()) or ("resolve_unit", "accept_symbol", "on_route"))
        named = str(self.door or "score")
        doors = [
            li(
                a(
                    span(label, className="voice-name"),
                    span(href, className="muted"),
                    href=href,
                    className="door-link" + (" is-on" if named == key else ""),
                ),
                id=f"door-{key}",
                className="door-card",
            )
            for href, label, key in HOUSE_DOORS
        ]
        segs = [
            button(
                label,
                type="button",
                className="seg is-on" if named == key else "seg",
                **control("threshold.look", door=key),
            )
            for _href, label, key in HOUSE_DOORS[:6]
        ]
        return section(
            span("Threshold", className="eyebrow"),
            h1("A door is a surface.", className="display"),
            p(
                "scan_surfaces reads routes/. validate_surfaces seals the bundle. "
                "RouterHooks bind Clock A to the live unit. Walking is GET. "
                "This room is the house as a catalog of doors — not /lattice.",
                className="lede",
            ),
            div(
                div(
                    span("bundle", className="eyebrow"),
                    h2(f"{n} pages", className="sight-title"),
                    p(f"{n_act} actions. Hooks: {', '.join(str(h) for h in hooks)}.", className="sight-law"),
                    p(err or (f"{len(errors)} catalog notes." if errors else "The catalog sealed."), className="muted"),
                    className="paper",
                    id="threshold-card",
                ),
                div(
                    span("sight", className="eyebrow"),
                    h2(named, className="sight-title"),
                    p("Name a door, then walk it. Clock A. Caps stay on Clock B.", className="sight-law"),
                    div(*segs, className="segs", role="radiogroup", aria_label="Named door"),
                    className="paper",
                ),
                className="kiln-split",
            ),
            ul(*doors, className="door-row", id="threshold-doors", aria_label="House doors"),
            id=self.id,
            className="room threshold-room",
            data_door=named,
        )

    @action(caps=())
    def look(self, door: str = "score"):
        keys = {row[2] for row in HOUSE_DOORS}
        self.door = door if door in keys else "score"
        HOST.log("threshold.look", str(self.door))
        HOST.score_write("threshold.look", "threshold", "A")
        mark_dirty(self)
        return update_with(self, extra_ops=[notify(str(self.door))])
