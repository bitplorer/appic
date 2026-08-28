"""ux-dom tag surface for Unified Component.render().

Authors write::

    from ux_compose import Component, div, h1, button, control

    class Cart(Component):
        def render(self):
            return div(h1(f"Items: {self.count}"), id=self.id)

This module re-exports tags when ux-dom is installed (Python ≥3.14).
On Python 3.10–3.13 it ships a local Tag shim so kit copies still render.
It does **not** re-export ux-dom's Component class.

Why not inherit ux-dom Component (or Tags)?
    Freeze is fixable: skip construct render(), republish _entry from live
    render(). That is not the reason.

    The MRO is the reason. Tree verbs (add/remove/get/clear, and whatever
    ux-dom adds next) live on the same instance as @action names. A shared
    MRO collides now or later. Fail closed: Component.__init_subclass__
    rejects ux-dom tree bases.

    Dual inheritance stays forbidden from product code. Authors return tags.
"""

from __future__ import annotations

from typing import Any, Iterable

HAS_DOM = False

# Populated when ux-dom is installed. Stay None on the offline shim path.
div = span = h1 = h2 = h3 = p = a = button = form = input_ = None
ul = li = header = footer = aside = section = article = nav = main = None
label = svg = path = rect = circle = None
html = head = body = title = style = meta = link = script = None
raw = None

try:
    from ux_dom.dom import (  # type: ignore
        a,
        article,
        aside,
        body,
        button,
        circle,
        div,
        footer,
        form,
        h1,
        h2,
        h3,
        head,
        header,
        html,
        input_,
        label,
        li,
        link,
        main,
        meta,
        nav,
        p,
        path,
        rect,
        script,
        section,
        span,
        style,
        svg,
        title,
        ul,
    )
    from ux_dom.dom.src.utils.dom_util import raw  # type: ignore

    HAS_DOM = True
except ImportError:  # pragma: no cover
    pass


_VOID = frozenset(
    {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "source",
        "track",
        "wbr",
    }
)
_ATTR = {
    "className": "class",
    "classname": "class",
    "htmlFor": "for",
    "html_for": "for",
    "cls": "class",
}


def _esc(value: Any) -> str:
    text = str(value)
    amp = chr(38) + "amp;"
    lt = chr(38) + "lt;"
    gt = chr(38) + "gt;"
    quot = chr(38) + "quot;"
    return text.replace("&", amp).replace("<", lt).replace(">", gt).replace('"', quot)


def _attr_name(key: str) -> str:
    mapped = _ATTR.get(key)
    if mapped:
        return mapped
    if key.startswith("data_") or key.startswith("aria_"):
        return key.replace("_", "-")
    if key == "viewBox":
        return "viewBox"
    if key == "strokeWidth":
        return "stroke-width"
    return key.replace("_", "-")


def _attrs(attrs: dict[str, Any]) -> str:
    parts: list[str] = []
    for key, value in attrs.items():
        if value is None or value is False:
            continue
        name = _attr_name(key)
        if value is True:
            parts.append(f" {name}")
            continue
        parts.append(f' {name}="{_esc(value)}"')
    return "".join(parts)


class Tag:
    def __init__(self, tag: str, *children: Any, **attrs: Any):
        self.name = tag
        self.children = children
        self.attrs = attrs

    def __str__(self) -> str:
        inner = "".join(_child(c) for c in self.children)
        open_ = f"<{self.name}{_attrs(self.attrs)}>"
        if self.name in _VOID:
            return open_[:-1] + " />"
        return f"{open_}{inner}</{self.name}>"

    def __html__(self) -> str:
        return str(self)

    def __iter__(self) -> Iterable[Any]:
        yield self

    def render(self) -> str:
        return str(self)


def _child(node: Any) -> str:
    if node is None or node is False:
        return ""
    if isinstance(node, (tuple, list)):
        return "".join(_child(x) for x in node)
    if isinstance(node, Tag):
        return str(node)
    return str(node)


def _factory(name: str):
    def make(*children: Any, **attrs: Any) -> Tag:
        return Tag(name, *children, **attrs)

    make.__name__ = name
    return make


if not HAS_DOM:
    html = _factory("html")
    head = _factory("head")
    body = _factory("body")
    title = _factory("title")
    style = _factory("style")
    meta = _factory("meta")
    link = _factory("link")
    script = _factory("script")
    div = _factory("div")
    span = _factory("span")
    h1 = _factory("h1")
    h2 = _factory("h2")
    h3 = _factory("h3")
    p = _factory("p")
    a = _factory("a")
    button = _factory("button")
    form = _factory("form")
    input_ = _factory("input")
    ul = _factory("ul")
    li = _factory("li")
    header = _factory("header")
    footer = _factory("footer")
    aside = _factory("aside")
    section = _factory("section")
    article = _factory("article")
    nav = _factory("nav")
    main = _factory("main")
    label = _factory("label")
    svg = _factory("svg")
    path = _factory("path")
    rect = _factory("rect")
    circle = _factory("circle")

    def raw(html_str: str) -> str:  # type: ignore[misc]
        return html_str


def require_dom() -> None:
    if not HAS_DOM:
        raise ImportError(
            "ux-dom is not installed. Tag trees need Python ≥3.14 and "
            "`pip install ux-dom`. The local Tag shim still renders HTML strings at L1."
        )


__all__ = [
    "HAS_DOM",
    "require_dom",
    "raw",
    "html",
    "head",
    "body",
    "title",
    "style",
    "meta",
    "link",
    "script",
    "div",
    "span",
    "h1",
    "h2",
    "h3",
    "p",
    "a",
    "button",
    "form",
    "input_",
    "ul",
    "li",
    "header",
    "footer",
    "aside",
    "section",
    "article",
    "nav",
    "main",
    "label",
    "svg",
    "path",
    "rect",
    "circle",
]
