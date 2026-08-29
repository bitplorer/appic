"""ux-dom tag surface for Unified Component.render().

Authors write::

    from ux_compose import Component, div, h1, button, control

    class Cart(Component):
        def render(self):
            return div(h1(f"Items: {self.count}"), id=self.id)

This module re-exports tags when ux-dom is installed (Python ≥3.14).
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


class _Tag:
    """Call-shape compatible with ux-dom tags when the specialist is absent."""

    def __init__(self, tag: str, *children: Any, **attrs: Any):
        self.name = tag
        self.children = children
        self.attrs = attrs

    def __str__(self) -> str:
        parts: list[str] = []
        for key, value in self.attrs.items():
            if value is None or value is False:
                continue
            name = _ATTR.get(key, key)
            if key.startswith("data_") or key.startswith("aria_"):
                name = key.replace("_", "-")
            elif key not in _ATTR:
                if key in {"viewBox", "strokeWidth"}:
                    name = "viewBox" if key == "viewBox" else "stroke-width"
                else:
                    name = key.replace("_", "-")
            if value is True:
                parts.append(f" {name}")
                continue
            amp, lt, gt, quot = (
                chr(38) + "amp;",
                chr(38) + "lt;",
                chr(38) + "gt;",
                chr(38) + "quot;",
            )
            text = (
                str(value)
                .replace("&", amp)
                .replace("<", lt)
                .replace(">", gt)
                .replace('"', quot)
            )
            parts.append(f' {name}="{text}"')
        open_ = f"<{self.name}{''.join(parts)}>"
        if self.name in _VOID:
            return open_[:-1] + " />"
        inner = "".join(
            "" if c is None or c is False else str(c) if not isinstance(c, (tuple, list)) else "".join(str(x) for x in c)
            for c in self.children
        )
        return f"{open_}{inner}</{self.name}>"

    def __html__(self) -> str:
        return str(self)

    def __iter__(self) -> Iterable[Any]:
        yield self

    def render(self) -> str:
        return str(self)


def _factory(name: str):
    def make(*children: Any, **attrs: Any) -> _Tag:
        return _Tag(name, *children, **attrs)

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
            "`pip install ux-dom`. HTML strings in render() still work at L1."
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
