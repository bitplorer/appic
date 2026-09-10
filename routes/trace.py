"""Doctor residuals expire by teaching. Isolation is hard."""
from __future__ import annotations

from foundry import app as get_app
from ux_compose import Component, a, div, h1, li, p, section, span, ul


class Trace(Component):
    id = "trace"

    def render(self):
        handle = get_app()
        report = getattr(handle, "_doctor", None) if handle is not None else None
        chips = []
        if report is not None:
            for attr in ("surfaces", "routes", "errors", "warnings", "residuals"):
                val = getattr(report, attr, None)
                if val:
                    chips.append(span(f"{attr} · {val}", className="chip"))
            notes = []
            for name in dir(report):
                if name.startswith("scan") or name.endswith("_scans"):
                    continue
            findings = getattr(report, "findings", None) or getattr(report, "items", None)
            if findings:
                notes = [li(str(item)) for item in list(findings)[:24]]
            else:
                notes = [li("Doctor ran at boot. Isolation is hard. Kit-import residuals expire by teaching.")]
        else:
            chips = [span("doctor pending", className="chip")]
            notes = [li("The composition root has not published a report yet.")]
        return section(
            span("scan families", className="kicker"),
            h1("Trace"),
            p(
                "Isolation and dual-Document fail closed. "
                "Kit-import, leftover aliases, render-chrome, docs collision, CEK host, "
                "and store-clone residuals expire by teaching.",
                className="lede",
            ),
            div(*chips, className="chip-row"),
            ul(*notes, className="law-list paper"),
            a("Back to law", href="/docs", className="btn-ghost"),
            id=self.id,
            className="page",
        )
