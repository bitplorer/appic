"""Copy press — the ownership ritual. Not a catalog stem."""
from __future__ import annotations

from ux_compose import Component, h1, li, p, section, span, ul
from ux_compose.kit.catalog import CATALOG, ALIASES, list_components, resolve
from ux_compose.kit.copy import find_app_root


class Copy(Component):
    id = "copy"

    def render(self):
        entries = list_components()
        root = find_app_root()
        alias = resolve("treeview")
        stems = [e.get("stem", "") for e in entries]
        return section(
            span("Press", className="eyebrow"),
            h1("Own the file. The library keeps the source of truth.", className="display"),
            p(
                f"{len(CATALOG)} stems. Alias treeview → {alias.get('stem')}. "
                f"ALIASES={dict(ALIASES)}. App root {root}.",
                className="lede",
            ),
            p("Do not copy kit/copy.py or kit/catalog.py as widgets. uxcompose add is the ritual.", className="lede"),
            ul(*[li(n) for n in stems], className="stem-list"),
            id=self.id,
            className="room",
        )
