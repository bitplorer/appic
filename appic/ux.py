"""Product-facing ux-compose imports + XOR-safe motion helpers.

Isolation Law: never import ux_channel or CEK from this package.

Author door: re-export official ``act`` / ``tick`` / ``field`` / ``status`` /
``maybe_*`` from ``ux_compose``. Do not invent a second helper world.
``act()`` posts ``/act/{action}``. Presence extras (share / stagger) stay here.
"""
from __future__ import annotations

from typing import Any

from ux_compose import (
    App,
    AttachNote,
    Component,
    MorphState,
    RefState,
    action,
    attach_notes,
    bind,
    control,
    doctor,
    field,
    morph_play,
    notify,
    status,
    tick,
    maybe_fade,
    maybe_plan,
    maybe_slide,
    update_with as _compose_update_with,
)
from ux_compose import act as _compose_act

try:
    from ux_compose import HAS_DOM
except Exception:  # pragma: no cover
    HAS_DOM = False

try:
    from ux_compose import scene, rise, fade, slide
except Exception:  # pragma: no cover
    scene = rise = fade = slide = None

from appic.tags import (
    HAS_TAGS,
    a,
    article,
    aside,
    button,
    circle,
    div,
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
    nav,
    p,
    path,
    raw,
    rect,
    section,
    span,
    svg,
    table,
    tbody,
    td,
    textarea,
    th,
    thead,
    tr,
    ul,
)


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


def maybe_share(name: str, key: str, leave: str, arrive: str, *, ms: int = 140):
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


def maybe_stagger(name: str, ids: list[str], *, ms: int = 90):
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
    Channel stamp only allows ui.dom.morph / log.append / transition.play / …
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
    "MorphState",
    "RefState",
    "HAS_TAGS",
    "HAS_DOM",
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
    "maybe_fade",
    "maybe_plan",
    "maybe_share",
    "maybe_slide",
    "maybe_stagger",
    "morph_play",
    "nav",
    "notify",
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
    "tick",
    "tr",
    "ul",
    "update_with",
]
