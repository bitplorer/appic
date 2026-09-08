"""Product-facing ux-compose imports + XOR-safe motion helpers.

Isolation Law: never import ux_channel or CEK from this package.

Author door: re-export official ``act`` / ``mark_dirty`` / ``field`` / ``status`` /
``optional_*`` from ``ux_compose``. Do not invent a second helper world.
``act()`` posts ``/act/{action}``. Presence extras (share / stagger) stay here.
"""
from __future__ import annotations

from typing import Any

from ux_compose import (
    HAS_DOM,
    App,
    AttachNote,
    Component,
    MorphState,
    RefState,
    a,
    action,
    act as _compose_act,
    article,
    aside,
    attach_notes,
    bind,
    button,
    circle,
    control,
    div,
    doctor,
    fade,
    field,
    footer,
    form,
    h1,
    h2,
    h3,
    header,
    input_,
    label,
    li,
    main,
    mark_dirty,
    morph_play,
    nav,
    notify,
    optional_fade,
    optional_plan,
    optional_slide,
    p,
    path,
    raw,
    rect,
    rise,
    scene,
    section,
    slide,
    span,
    status,
    svg,
    ul,
    update_with as _compose_update_with,
)
from ux_dom.dom import table, tbody, td, textarea, th, thead, tr

HAS_TAGS = True


def act(
    action_name: str,
    label: str,
    *,
    kind: str = "secondary",
    target: str = "#stage",
    on: str | None = None,
    **args: Any,
):
    """Official author door. POST form to ``/act/{action}``. Same signature."""
    tree = _compose_act(
        action_name, label, kind=kind, target=target, on=on, **args
    )
    if isinstance(tree, str):
        return raw(tree)
    return tree


def optional_share(name: str, key: str, leave: str, arrive: str, *, ms: int = 140):
    """Presence cookbook: share key is identity, not a CSS class."""
    if scene is None or rise is None:
        return None
    try:
        return (
            scene(name)
            .share(key, leave=leave, arrive=arrive, recipe=rise.enter(ms=ms))
            .enter(arrive, rise.enter(ms=ms))
        )
    except Exception:
        return None


def optional_stagger(name: str, ids: list[str], *, ms: int = 90):
    """Presence cookbook: stagger_in on survivors so they do not remount."""
    if scene is None or rise is None:
        return None
    try:
        return scene(name).stagger_in(ids, rise.enter(ms=ms))
    except Exception:
        return None


def _plan_ops(plan: Any) -> list[Any]:
    if plan is None or isinstance(plan, str):
        return []
    try:
        from ux_behavior.ops import Op
    except Exception:
        Op = None  # type: ignore
    raw_ops = getattr(plan, "ops", None)
    if callable(raw_ops):
        try:
            raw_ops = raw_ops()
        except Exception:
            raw_ops = None
    if not raw_ops:
        return []
    out: list[Any] = []
    items = raw_ops if isinstance(raw_ops, list) else [raw_ops]
    for item in items:
        if Op is not None and isinstance(item, Op):
            out.append(item)
            continue
        if isinstance(item, dict) and str(item.get("op") or "") == "transition.play":
            payload = {k: v for k, v in item.items() if k != "op"}
            if Op is not None:
                out.append(Op("transition", "play", payload))
    return out


def update_with(component: Any, *rest: Any, extra_ops: Any = None, html: Any = None, **kwargs: Any):
    """Legal ui.dom.morph + optional transition.play + extra_ops (notify).

    Compatible with the compose author seat:
        update_with(self, scene(...), extra_ops=[notify("…")])
    XOR: plans carry no html=; html= may live on the morph payload only.
    """
    extra = extra_ops if extra_ops is not None else kwargs.get("extra_ops")
    if extra is None:
        extra = []
    elif not isinstance(extra, list):
        extra = [extra]
    try:
        from ux_behavior.ops import update as ui_update
    except Exception:
        return _compose_update_with(component, html=html)
    target = getattr(component, "id", None) or "component"
    tid = str(target) if str(target).startswith("#") else f"#{target}"
    markup = html
    if markup is None:
        try:
            markup = str(component.render())
        except Exception:
            markup = ""
    ops: list[Any] = [ui_update(tid, markup)]
    for item in rest:
        ops.extend(_plan_ops(item))
    for op in extra:
        if op is not None:
            ops.append(op)
    return ops


__all__ = [
    "App",
    "AttachNote",
    "Component",
    "HAS_DOM",
    "HAS_TAGS",
    "MorphState",
    "RefState",
    "a",
    "act",
    "action",
    "article",
    "aside",
    "attach_notes",
    "bind",
    "button",
    "circle",
    "control",
    "div",
    "doctor",
    "fade",
    "field",
    "footer",
    "form",
    "h1",
    "h2",
    "h3",
    "header",
    "input_",
    "label",
    "li",
    "main",
    "mark_dirty",
    "morph_play",
    "nav",
    "notify",
    "optional_fade",
    "optional_plan",
    "optional_share",
    "optional_slide",
    "optional_stagger",
    "p",
    "path",
    "raw",
    "rect",
    "rise",
    "scene",
    "section",
    "span",
    "status",
    "svg",
    "table",
    "tbody",
    "td",
    "textarea",
    "th",
    "thead",
    "tr",
    "ul",
    "update_with",
]
