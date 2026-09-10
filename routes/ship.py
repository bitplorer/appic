"""Ship — prepare_deploy for six providers. Does not upload secrets."""
from __future__ import annotations

from pathlib import Path

from ux_compose import Component, a, div, h1, li, p, section, span, ul
from ux_compose.deploy import prepare_deploy


class Ship(Component):
    id = "ship"

    def render(self):
        providers = ("docker", "fly", "render", "railway", "vps", "checklist")
        rows = []
        for name in providers:
            try:
                result = prepare_deploy(Path("."), provider=name, force=False)
                files = ", ".join(getattr(result, "files_written", []) or ["(already present)"])
                rows.append(li(f"{name} · {files}"))
            except Exception as exc:
                rows.append(li(f"{name} · {exc}"))
        return section(
            span("uxcompose deploy", className="kicker"),
            h1("Ship"),
            p(
                "prepare_deploy writes Docker / Fly / Render / Railway / VPS / checklist. "
                "It does not upload secrets. Serve prod is clocks hard off, not a replace for deploy.",
                className="lede",
            ),
            ul(*rows, className="law-list paper"),
            a("Health", href="/health", className="btn-ghost"),
            id=self.id,
            className="page",
        )
