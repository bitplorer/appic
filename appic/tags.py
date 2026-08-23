"""HTML tag trees that match the ux-compose author surface.

render() may return these nodes or strings. Progressive Superpower: the same
call shape as ux-dom tags (div, h1, button, …) without requiring Python 3.14.
"""
from __future__ import annotations

from typing import Any, Iterable

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
    amp, lt, gt, quot = chr(38)+'amp;', chr(38)+'lt;', chr(38)+'gt;', chr(38)+'quot;'
    return text.replace("&", amp).replace("<", lt).replace(">", gt).replace('"', quot)
def _attr_name(key: str) -> str:
    mapped = _ATTR.get(key)
    if mapped:
        return mapped
    if key.startswith("data_") or key.startswith("aria_"):
        return key.replace("_", "-")
    if key in {"viewBox", "strokeWidth"}:
        return "viewBox" if key == "viewBox" else "stroke-width"
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


def _child(node: Any) -> str:
    if node is None or node is False:
        return ""
    if isinstance(node, (tuple, list)):
        return "".join(_child(x) for x in node)
    if isinstance(node, Tag):
        return str(node)
    return str(node)


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


def _factory(name: str):
    def make(*children: Any, **attrs: Any) -> Tag:
        return Tag(name, *children, **attrs)

    make.__name__ = name
    return make


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
textarea = _factory("textarea")
ul = _factory("ul")
ol = _factory("ol")
li = _factory("li")
header = _factory("header")
footer = _factory("footer")
aside = _factory("aside")
section = _factory("section")
article = _factory("article")
nav = _factory("nav")
main = _factory("main")
label = _factory("label")
table = _factory("table")
thead = _factory("thead")
tbody = _factory("tbody")
tr = _factory("tr")
th = _factory("th")
td = _factory("td")
svg = _factory("svg")
path = _factory("path")
rect = _factory("rect")
circle = _factory("circle")
line = _factory("line")


def raw(html_str: str) -> str:
    return html_str


HAS_TAGS = True
