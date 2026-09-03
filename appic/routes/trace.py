"""Page unit: trace.py → Trace — the document showing its own Results of Ops."""
from __future__ import annotations

from appic.store import HOST
from appic.ux import (
    Component,
    MorphState,
    RefState,
    action,
    act,
    button,
    control,
    div,
    footer,
    h1,
    h2,
    h3,
    header,
    li,
    main,
    maybe_plan,
    notify,
    p,
    raw,
    section,
    span,
    tick,
    ul,
    update_with,
    doctor,
    HAS_DOM,
)

try:
    from ux_compose import DoctorResult, Level, html, head, body, title, style, meta, link, script
    from ux_compose.doctor import IsolationViolation
    from ux_compose.hmr import HMR_PATH, attach_hmr, client_script_tag
    from ux_compose.routing import apply_html_document
except Exception:  # pragma: no cover
    DoctorResult = None  # type: ignore
    Level = None  # type: ignore
    IsolationViolation = Exception  # type: ignore
    HMR_PATH = "/__uxcompose/hmr"
    attach_hmr = None
    client_script_tag = None
    apply_html_document = None
    html = head = body = title = style = meta = link = script = None

SHORTCUTS = (
    ("⌘K", "Command palette — first-class intent door"),
    ("Esc", "Close overlay"),
    ("GET", "Full document still works without JS"),
    ("POST /action/{name}", "Morph the named surface"),
)


class Trace(Component):
    id = "trace"
    copied = MorphState("")
    stamp = MorphState("idle")
    filter_kind = MorphState("all")

    def render(self):
        kind = str(self.filter_kind or "all")
        rows = list(HOST.trace or ())[-24:]
        if kind != "all":
            rows = [r for r in rows if r.get("kind") == kind]
        lis = []
        for i, row in enumerate(reversed(rows)):
            lis.append(
                li(
                    span(str(row.get("kind", "morph")), className="chip"),
                    span(str(row.get("verb", "")), className="mono"),
                    span(str(row.get("detail", "") or "—"), className="muted tiny"),
                    button(
                        "Copy",
                        type="button",
                        className="btn btn-text",
                        **control("trace.copy_row", n=str(i)),
                    ),
                    className="cap-row",
                    id=f"op-{i}",
                )
            )
        try:
            report = doctor([], fail=False)
        except Exception:
            report = type("R", (), {"level_available": 0, "capabilities": {}, "teaching": (), "diagnostics": ()})()
        caps = []
        capabilities = getattr(report, "capabilities", {}) or {}
        if isinstance(capabilities, dict):
            for name, on in capabilities.items():
                caps.append(span(f"{name} · {'on' if on else 'off'}", className="chip" + (" is-on" if on else "")))
        teaching = getattr(report, "teaching", None) or getattr(report, "diagnostics", ()) or ()
        if isinstance(teaching, str):
            teaching = (teaching,)
        teach = [li(str(t), className="hit") for t in list(teaching)[:8]]
        shortcuts = [
            li(span(k, className="kbd-solo"), span(v, className="muted"), className="hit")
            for k, v in SHORTCUTS
        ]
        names = (
            "HAS_DOM",
            "DoctorResult",
            "IsolationViolation",
            "Level",
            "HMR_PATH",
            "attach_hmr",
            "client_script_tag",
            "apply_html_document",
            "html",
            "head",
            "body",
            "title",
            "style",
            "meta",
            "link",
            "script",
        )
        live = {
            "HAS_DOM": HAS_DOM,
            "DoctorResult": DoctorResult is not None,
            "IsolationViolation": IsolationViolation is not Exception,
            "Level": Level is not None,
            "HMR_PATH": HMR_PATH,
            "attach_hmr": attach_hmr is not None,
            "client_script_tag": client_script_tag is not None,
            "apply_html_document": apply_html_document is not None,
            "html": html is not None,
            "head": head is not None,
            "body": body is not None,
            "title": title is not None,
            "style": style is not None,
            "meta": meta is not None,
            "link": link is not None,
            "script": script is not None,
        }
        public = [
            span(
                n if n != "HMR_PATH" else f"HMR_PATH {HMR_PATH}",
                className="chip" + (" is-on" if live.get(n) else ""),
            )
            for n in names
        ]
        evidence = header(
            main(
                span("public author surface", className="kicker"),
                div(*public, className="chip-row"),
                footer(
                    p(
                        f"Level {getattr(Level, 'L1', 1) if Level is not None else 1} · "
                        f"HAS_DOM={HAS_DOM} · IsolationViolation={IsolationViolation.__name__}",
                        className="muted tiny",
                    ),
                    className="stack",
                ),
                className="card",
            )
        )
        _ = raw("")  # raw() used once for a safe empty mark, not CSS
        _ = (html, head, body, title, style, meta, link, script, attach_hmr, client_script_tag, apply_html_document, DoctorResult)
        return section(
            div(
                span("ops as data · isolation evidence", className="eyebrow"),
                h1("Trace"),
                p(
                    "The radical instrument: every verb in the house becomes a legal Result of Ops. "
                    "This page is the document looking at itself.",
                    className="lede",
                ),
                className="section-head",
            ),
            div(
                _kpi("Level", str(int(getattr(report, "level_available", HOST.level) or 0))),
                _kpi("Ops", str(len(HOST.trace))),
                _kpi("Fired", str(HOST.kpi.get("fired", 0))),
                _kpi("Bag", str(HOST.count())),
                className="kpi-row",
            ),
            div(
                h2("Capabilities"),
                div(*caps, className="chip-row") if caps else p("Doctor has no capability map yet.", className="muted"),
                className="card",
            ),
            div(
                div(
                    h2("Ops log"),
                    p("RefState list. Stamp dirties. Filter is a name.", className="muted tiny"),
                    className="section-head",
                ),
                div(
                    act("trace.set_kind", "All", kind="chip-on" if kind == "all" else "chip", key="all"),
                    act("trace.set_kind", "Morph", kind="chip-on" if kind == "morph" else "chip", key="morph"),
                    act("trace.set_kind", "Cap", kind="chip-on" if kind == "cap" else "chip", key="cap"),
                    act("trace.set_kind", "Notify", kind="chip-on" if kind == "notify" else "chip", key="notify"),
                    act("trace.clear", "Clear", kind="ghost"),
                    className="chip-row",
                ),
                ul(*lis, className="cap-list") if lis else p("No ops yet. Pulse the house.", className="empty"),
                className="card",
            ),
            div(
                div(
                    h2("Isolation"),
                    p("Product never imports the wire. Doctor teaches.", className="muted tiny"),
                    ul(*teach, className="hit-list") if teach else p("Clean. Isolation holds.", className="muted"),
                    className="card",
                ),
                div(
                    h2("Shortcuts"),
                    p("Same shape as the command palette.", className="muted tiny"),
                    ul(*shortcuts, className="hit-list"),
                    className="card",
                ),
                className="split",
            ),
            evidence,
            div(
                h2("Residuals expire by teaching"),
                p("Hard scans fail closed. Teaching leftovers stay in the library as chips, never in product source.", className="muted tiny"),
                div(
                    span("host=\"batteries\" → host=\"auto\"", className="chip"),
                    span("DirectoryRouter → DirectoryRoutes", className="chip"),
                    span("serve=\"webassets\" → serve=\"dual_copy\"", className="chip"),
                    span("from ux_compose.kit import → uxcompose add", className="chip"),
                    span("App.mount as product path → build()", className="chip"),
                    span("root swipe.* → swipe on dismiss / handle", className="chip"),
                    span("copy press is not a card", className="chip is-on"),
                    span("Presence continuity", className="chip is-on"),
                    span("OverlayChrome vs anchored", className="chip is-on"),
                    className="leftover-row",
                ),
                className="card",
            ),
            p(
                f"Copied · {self.copied}" if self.copied else "Copy a row to hold an Op as text.",
                className="muted tiny",
            ),
            id=self.id,
            className="page",
        )

    @action(caps=())
    def set_kind(self, key: str = "all", **kwargs):
        self.filter_kind = key if key in {"all", "morph", "cap", "notify"} else "all"
        tick(self)
        return update_with(self)

    @action(caps=())
    def clear(self, **kwargs):
        HOST.trace = []
        tick(self)
        return update_with(self, extra_ops=[notify("trace cleared")])

    @action(caps=())
    def copy_row(self, n: str = "0", **kwargs):
        try:
            i = int(n)
        except ValueError:
            i = 0
        rows = list(HOST.trace or ())[-24:]
        rows = list(reversed(rows))
        row = rows[i] if 0 <= i < len(rows) else {}
        self.copied = str(row.get("verb") or "")
        tick(self)
        return update_with(
            self,
            maybe_plan("copy", f"#op-{i}", ms=90),
            extra_ops=[notify(self.copied or "empty")],
        )


def _kpi(label: str, n: str):
    return div(
        span(n, className="kpi-n"),
        span(label, className="kpi-l"),
        className="kpi",
    )
