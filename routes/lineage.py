"""Page unit — lineage.py → GET /lineage.

Family tree of vessels. Owned Tree kit, shell=False, NODES from Host stock.
Not the kit demo at /tree. Not a Pulse room.
"""
from __future__ import annotations

from ux_compose import (
    a,
    div,
    h1,
    p,
    section,
    span,
)
from components.tree import Tree as TreeCard
from store import HOST


class Lineage(TreeCard):
    id = "lineage"

    def _nodes(self):
        rows = [("house", None, "House")]
        seen = {"house"}
        for rec in HOST.lineage:
            key = str(rec.get("id") or "")
            if not key or key in seen:
                # stage hops reuse id — suffix the stage so the tree can open
                stage = str(rec.get("stage") or "")
                key = f"{key}-{stage}" if stage else key
            if not key or key in seen:
                continue
            parent = str(rec.get("parent") or "house")
            if parent not in seen:
                parent = "house"
            clay = str(rec.get("clay") or "clay")
            stage = str(rec.get("stage") or "")
            label = f"{key} · {clay} · {stage}".strip(" ·")
            rows.append((key, parent, label))
            seen.add(key)
        if len(rows) == 1:
            rows.append(("p000", "house", "p000 · porcelain · drawn"))
        return tuple(rows)

    def render(self, *, shell=None, **slots):
        HOST.occupy("lineage")
        tree = super().render(shell=False, **slots)
        return section(
            span("Lineage", className="eyebrow"),
            h1("What the house remembers.", className="display"),
            p(
                "A tree of vessels. Nodes are Host stock. Expanded names are MorphState. "
                "The kit demo at /tree stays a kit room. This is the house memory. "
                "Parent is the house until a piece is seated; stage hops keep the id.",
                className="lede",
            ),
            div(
                tree,
                className="paper lineage-card",
                id="lineage-card",
            ),
            div(
                a("Sit with the vessel", href="/vessel", className="btn-primary"),
                a("Walk the vitrine", href="/vitrine", className="btn-ghost"),
                className="hero-actions",
            ),
            id=self.id,
            className="room lineage-room",
        )
