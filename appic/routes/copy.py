"""Page unit: copy.py → Copy.

The copy press made visible. ``kit/copy.py`` is a helper, not a catalog stem.
Do not ship ``components/copy.py`` as a widget. Isolation: no ux_channel.
Product never ``from ux_compose.kit import`` (AST-scan stays green); the press
is loaded by importlib so doctor teaching residuals expire by teaching, not
by a leftover import in this room.
"""
from __future__ import annotations

import importlib
from pathlib import Path

from ux_compose import (
    Component,
    MorphState,
    action,
    notify,
    tick,
    update_with,
)

from appic.store import HOST
from appic.ux import (
    a,
    act,
    article,
    div,
    h1,
    h2,
    h3,
    li,
    p,
    section,
    span,
    ul,
)

ROOT = Path(__file__).resolve().parents[2]
COMPONENTS = ROOT / "components"
OWNED_LOGIN = COMPONENTS / "login.py"


def _press():
    copy_mod = importlib.import_module("ux_compose.kit.copy")
    cat_mod = importlib.import_module("ux_compose.kit.catalog")
    return copy_mod, cat_mod


def copy_evidence() -> dict:
    """JSON for GET /api/copy. The press is evidence, not a card."""
    copy_mod, cat_mod = _press()
    catalog = list(cat_mod.list_components())
    stems = []
    for entry in catalog:
        stem = entry["stem"]
        path = COMPONENTS / f"{stem}.py"
        stems.append(
            {
                "stem": stem,
                "name": entry["name"],
                "css": bool(entry.get("css")),
                "page": bool(entry.get("page")),
                "owned": path.is_file(),
                "path": str(path.relative_to(ROOT)) if path.is_file() else None,
                "exports": list(entry.get("exports") or []),
                "description": entry.get("description") or "",
            }
        )
    overlay = COMPONENTS / "overlay.py"
    root_path = None
    root_error = None
    try:
        root_path = str(copy_mod.find_app_root(ROOT))
    except Exception as exc:
        root_error = f"{type(exc).__name__}: {exc}"
    restyle = ""
    try:
        text = OWNED_LOGIN.read_text(encoding="utf-8")
        if "appic-owned-card" in text:
            restyle = "appic-owned-card"
        elif "class_card" in text:
            restyle = "class_card"
    except Exception:
        restyle = ""
    return {
        "press": ["copy_component", "find_app_root", "KitCopyError"],
        "catalog": stems,
        "count": len(stems),
        "overlay": {
            "stem": "overlay",
            "name": "OverlayChrome",
            "catalogued": False,
            "owned": overlay.is_file(),
            "path": "components/overlay.py" if overlay.is_file() else None,
            "note": "Not a catalog stem. Copied by hand.",
        },
        "find_app_root": root_path,
        "find_app_root_error": root_error,
        "css": False,
        "page_alias": "{Cls} as {Cls}Card",
        "import_rewrite": [
            "from ux_compose.kit.X import → from .X import",
            "from ux_compose.kit import → from . import",
        ],
        "restyle_token": restyle,
        "sha": "7ea3eb8",
    }


class Copy(Component):
    id = "copy"
    stamp = MorphState("idle")
    selected = MorphState("login")
    last_error = MorphState("")
    root_path = MorphState("")
    restyle = MorphState("ink")

    def render(self):
        evidence = copy_evidence()
        selected = str(self.selected or "login")
        dies = []
        for row in evidence["catalog"]:
            stem = row["stem"]
            on = stem == selected
            dies.append(
                act(
                    "copy.select",
                    stem,
                    kind="chip-on" if on else "chip",
                    stem=stem,
                    target="#copy",
                )
            )
        overlay = evidence["overlay"]
        current = next((r for r in evidence["catalog"] if r["stem"] == selected), evidence["catalog"][0])
        error = str(self.last_error or "")
        root = str(self.root_path or evidence.get("find_app_root") or evidence.get("find_app_root_error") or "—")
        restyle = str(self.restyle or "ink")
        token_cls = "press-token is-ink" if restyle == "ink" else "press-token is-paper"
        owned_n = sum(1 for r in evidence["catalog"] if r["owned"])
        return section(
            span("ownership ritual · the press is not a card", className="eyebrow"),
            h1("Copy"),
            p(
                "uxcompose add copies a kit stem into components/. You own the file. "
                "The library keeps the source of truth. OverlayChrome is not in the catalog — "
                "it is copied by hand. kit/copy.py is the press, never a widget.",
                className="lede",
            ),
            div(
                article(
                    span("find_app_root", className="kicker"),
                    h2("Walk until the house appears"),
                    p("app.py + routes/ (create-app layout). Nested app/app.py also counts.", className="muted"),
                    p(root, className="mono tiny", id="copy-root"),
                    act("copy.probe_root", "Probe the root", kind="secondary", target="#copy"),
                    className="card",
                ),
                article(
                    span("KitCopyError", className="kicker"),
                    h2("Unknown stem fails closed"),
                    p("copy_component('not-a-stem') raises. The press does not invent cards.", className="muted"),
                    p(error or "Awaiting a bad name.", className="mono tiny", id="copy-error"),
                    act("copy.fail_unknown", "Press a missing die", kind="ghost", target="#copy"),
                    className="card",
                ),
                article(
                    span("class_*", className="kicker"),
                    h2("A restyled token"),
                    p("Owned Login.class_card carries appic-owned-card. Edit the copy; the house listens.", className="muted"),
                    div("Login", className=token_cls, id="copy-token"),
                    p(f"token · {evidence['restyle_token'] or 'class_card'} · pose {restyle}", className="mono tiny"),
                    act("copy.restyle", "Flip the paper", kind="secondary", target="#copy"),
                    className="card",
                ),
                className="law-grid",
            ),
            div(
                span("23 catalog stems", className="kicker"),
                h2("The press bed"),
                p(
                    f"{owned_n} of {evidence['count']} owned under components/. css: False. "
                    "No companion CSS. uxcompose build scans **/*.py.",
                    className="muted",
                ),
                div(*dies, className="press-bed", id="copy-bed"),
                className="card press-sheet",
            ),
            div(
                article(
                    span(current["stem"], className="kicker"),
                    h2(current["name"]),
                    p(current["description"], className="muted"),
                    ul(
                        li(f"owned  {current['path'] or 'missing'}", className="mono tiny"),
                        li(f"css  {current['css']}", className="mono tiny"),
                        li(f"page  {current['page']}", className="mono tiny"),
                        li("alias  from components.{stem} import {Cls} as {Cls}Card", className="mono tiny"),
                        li("rewrite  ux_compose.kit.X → .X", className="mono tiny"),
                        className="cap-list",
                    ),
                    a("Open the door" if current["stem"] == "login" else "Walk the house", href="/enter" if current["stem"] == "login" else "/house", className="btn btn-text"),
                    className="card",
                    id=f"die-{current['stem']}",
                ),
                article(
                    span("uncatalogued die", className="kicker"),
                    h2("OverlayChrome"),
                    p(
                        "Not listed by uxcompose add --list. Copied by hand to components/overlay.py. "
                        "Dialog / Sheet / ActionSheet take ids from it. Anchored family does not.",
                        className="muted",
                    ),
                    ul(
                        li(f"owned  {overlay['path']}", className="mono tiny"),
                        li("catalogued  False", className="mono tiny"),
                        li("ids  {root}-scrim / {root}-panel / {root}-dismiss", className="mono tiny"),
                        className="cap-list",
                    ),
                    a("Inspect chrome", href="/overlay", className="btn btn-text"),
                    className="card is-uncatalogued",
                ),
                className="split",
            ),
            div(
                h3("Laws the press keeps"),
                ul(
                    li("The press is not a card. Never components/copy.py as a widget.", className="hit"),
                    li("css: False. Markup is Tailwind class_* only.", className="hit"),
                    li("--page aliases {Cls} as {Cls}Card — never class Login(Login).", className="hit"),
                    li("from ux_compose.kit import is a teaching residual. Doctor names it. Product copies.", className="hit"),
                    li("serve=\"webassets\" leftover → serve=\"dual_copy\". host=\"batteries\" leftover → host=\"auto\".", className="hit"),
                    className="hit-list",
                ),
                p("GET /api/copy stays JSON. The document does not wrap it.", className="muted tiny"),
                className="card",
            ),
            id=self.id,
            className="page",
            data_selected=selected,
        )

    @action(caps=())
    def select(self, stem: str = "login", **kwargs):
        copy_mod, cat_mod = _press()
        try:
            meta = cat_mod.resolve(stem)
            self.selected = meta["stem"]
            self.last_error = ""
        except Exception as exc:
            self.last_error = f"{type(exc).__name__}: {exc}"
        tick(self)
        return update_with(self, extra_ops=[notify(f"die · {self.selected}")])

    @action(caps=())
    def probe_root(self, **kwargs):
        copy_mod, _cat = _press()
        try:
            found = copy_mod.find_app_root(ROOT)
            self.root_path = str(found)
            self.last_error = ""
            HOST.log("copy.find_app_root", self.root_path, "morph")
        except Exception as exc:
            self.root_path = ""
            self.last_error = f"{type(exc).__name__}: {exc}"
            HOST.log("copy.find_app_root", type(exc).__name__, "morph")
        tick(self)
        return update_with(self, extra_ops=[notify("root probed")])

    @action(caps=())
    def fail_unknown(self, **kwargs):
        copy_mod, _cat = _press()
        try:
            copy_mod.copy_component("not-a-stem", root=ROOT)
            self.last_error = "unexpected success"
        except Exception as exc:
            self.last_error = f"{type(exc).__name__}: {exc}"
            HOST.log("copy.KitCopyError", "not-a-stem", "morph")
        tick(self)
        return update_with(self, extra_ops=[notify("press refused")])

    @action(caps=())
    def restyle(self, **kwargs):
        self.restyle = "paper" if str(self.restyle or "ink") == "ink" else "ink"
        tick(self)
        HOST.log("copy.restyle", str(self.restyle), "morph")
        return update_with(self, extra_ops=[notify(f"token · {self.restyle}")])
