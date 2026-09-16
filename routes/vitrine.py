"""Page unit — vitrine.py → GET /vitrine. Drawn work. Rating is a named star."""
from __future__ import annotations

from ux_compose import (
    Component,
    MorphState,
    RefState,
    action,
    a,
    article,
    button,
    control,
    div,
    h1,
    h2,
    mark_dirty,
    notify,
    p,
    section,
    span,
    update_with,
)
from store import HOST

STARS = (("one", "Quiet"), ("two", "Held"), ("three", "Even"), ("four", "Bright"), ("five", "Keeps"))


class Vitrine(Component):
    id = "vitrine"
    which = MorphState("")
    rating = MorphState("three")
    dirty = MorphState("idle")
    empty_seen = RefState(0)

    def _pieces(self):
        return list(HOST.vitrine)

    def _current(self):
        pieces = self._pieces()
        key = str(self.which or "")
        for row in pieces:
            if row.get("id") == key:
                return row
        return pieces[-1] if pieces else None

    def render(self):
        pieces = self._pieces()
        current = self._current()
        if not pieces:
            return section(
                span("Vitrine", className="eyebrow"),
                h1("Nothing drawn yet.", className="display"),
                p(
                    "The shelf is empty until a firing finishes. "
                    "Throw, glaze, place, then keep the fire overnight.",
                    className="lede",
                ),
                div(
                    a("Throw a body", href="/wheel", className="btn-primary"),
                    a("Keep the fire", href="/kiln", className="btn-ghost"),
                    className="hero-actions",
                ),
                id=self.id,
                className="room emptystate",
            )
        cards = [
            button(
                span(row.get("clay", "clay"), className="card-title"),
                span(f"{row.get('glaze', 'glaze')} · {row.get('band', 'drawn')}", className="muted"),
                type="button",
                className="map-card is-on" if current and current.get("id") == row.get("id") else "map-card",
                **control("vitrine.show", piece=str(row.get("id"))),
            )
            for row in pieces
        ]
        cur_id = str(current.get("id") if current else "")
        rate = str(self.rating or "three")
        stars = [
            button(
                label,
                type="button",
                className="seg is-on" if rate == key else "seg",
                **control("vitrine.rate", star=key),
            )
            for key, label in STARS
        ]
        return section(
            span("Vitrine", className="eyebrow"),
            h1("What the fire kept.", className="display"),
            p(
                "The shelf is Host stock. Which piece is MorphState. "
                "How it sits is a named star — never MorphState(int).",
                className="lede",
            ),
            div(
                article(
                    span("piece", className="eyebrow"),
                    h2(
                        f"{current.get('clay', 'clay')} · {current.get('glaze', 'glaze')}" if current else "—",
                        className="sight-title",
                    ),
                    p(current.get("note") or "Drawn from the kiln.", className="sight-law") if current else p(""),
                    p(str(HOST.ratings.get(cur_id, rate)), className="mono"),
                    div(*stars, className="segs", role="radiogroup", aria_label="How it sits"),
                    className="paper vitrine-hero",
                    id="vitrine-hero",
                ),
                div(*cards, className="map-grid", id="vitrine-shelf"),
                className="kiln-split",
            ),
            id=self.id,
            className="room",
        )

    @action(caps=())
    def show(self, piece: str = ""):
        ids = {str(row.get("id")) for row in self._pieces()}
        self.which = piece if piece in ids else (next(iter(ids), ""))
        mark_dirty(self)
        HOST.log("vitrine.show", str(self.which))
        return update_with(self, extra_ops=[notify(str(self.which))])

    @action(caps=())
    def rate(self, star: str = "three"):
        keys = {k for k, _ in STARS}
        self.rating = star if star in keys else "three"
        cur = self._current()
        if cur:
            HOST.ratings[str(cur.get("id"))] = str(self.rating)
            HOST.log("vitrine.rate", str(self.rating))
        mark_dirty(self)
        return update_with(self, extra_ops=[notify(str(self.rating))])
