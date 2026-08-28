"""Compose owned kit cards into a room tree. Isolation: no ux_channel."""
from __future__ import annotations

from appic.store import HOST
from appic.ux import article, div, h1, h2, p, section, span


def hero(kicker: str, title: str, lede: str):
    return section(
        span(kicker, className="kicker"),
        h1(title),
        p(lede, className="lede"),
        className="hero",
    )


def cards(*sids: str):
    out = []
    for sid in sids:
        inst = (HOST.pieces or {}).get(sid)
        if inst is None:
            continue
        try:
            tree = inst.render()
        except Exception:
            continue
        out.append(article(tree, className="kit-card", data_kit=sid))
    return out


def room(kicker: str, title: str, lede: str, *sids: str, rid: str):
    return div(
        hero(kicker, title, lede),
        div(*cards(*sids), className="kit-grid"),
        id=rid,
        className="room",
    )
