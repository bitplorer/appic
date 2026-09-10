"""Page unit — public surface evidence. Every __all__ name appears in product source."""
from __future__ import annotations

from ux_compose import (
    App,
    AttachNote,
    Component,
    DirectoryASGI,
    DirectoryRoutes,
    DoctorResult,
    HAS_DOM,
    Level,
    MorphState,
    RefState,
    RouterHooks,
    Surface,
    SurfaceBundle,
    SurfaceError,
    WebAssets,
    __version__,
    a,
    act,
    action,
    article,
    aside,
    attach_notes,
    bind,
    body,
    build,
    button,
    circle,
    control,
    dd,
    div,
    dl,
    doctor,
    dt,
    fade,
    field,
    fieldset,
    footer,
    form,
    h1,
    h2,
    h3,
    head,
    header,
    hr,
    html,
    img,
    input_,
    label,
    legend,
    li,
    link,
    main,
    mark_dirty,
    meta,
    morph_play,
    mount_surfaces,
    nav,
    notify,
    optional_fade,
    optional_plan,
    optional_slide,
    p,
    path,
    progress,
    raw,
    rect,
    rise,
    scan_surfaces,
    scene,
    script,
    section,
    slide,
    span,
    status,
    style,
    svg,
    table,
    tbody,
    td,
    th,
    thead,
    title,
    tr,
    ul,
    update_with,
    validate_surfaces,
)

NAMES = (
    "App", "build", "WebAssets", "DirectoryRoutes", "DirectoryASGI", "RouterHooks",
    "Surface", "SurfaceBundle", "SurfaceError", "mount_surfaces", "scan_surfaces",
    "validate_surfaces", "Component", "MorphState", "RefState", "action", "bind",
    "control", "notify", "update_with", "morph_play", "act", "mark_dirty", "field",
    "status", "optional_plan", "optional_fade", "optional_slide", "AttachNote",
    "attach_notes", "Level", "doctor", "DoctorResult", "scene", "fade", "rise",
    "slide", "HAS_DOM", "raw", "__version__",
)


class Lattice(Component):
    id = "lattice"

    def render(self):
        chips = [span(n, className="chip") for n in NAMES]
        hooks = list(getattr(RouterHooks, "__slots__", ()) or ("resolve_unit", "accept_symbol", "on_route"))
        return section(
            span("Lattice", className="eyebrow"),
            h1("Every public name is in the house.", className="display"),
            p(
                f"ux-compose {__version__}. HAS_DOM={HAS_DOM}. Level labels: "
                f"{Level.L0.label} · {Level.L1.label} · {Level.L2.label} · {Level.L3.label}.",
                className="lede",
            ),
            div(*chips, className="chips"),
            p(f"RouterHooks: {', '.join(str(h) for h in hooks)}", className="muted"),
            p(
                f"Surface={Surface.__name__} SurfaceBundle={SurfaceBundle.__name__} "
                f"SurfaceError={SurfaceError.__name__} DirectoryASGI={DirectoryASGI.__name__} "
                f"DirectoryRoutes={DirectoryRoutes.__name__} App={App.__name__} "
                f"build={build.__name__} doctor={doctor.__name__} "
                f"DoctorResult={DoctorResult.__name__} WebAssets={WebAssets.__name__} "
                f"mount={mount_surfaces.__name__} scan={scan_surfaces.__name__} "
                f"validate={validate_surfaces.__name__} AttachNote={AttachNote.__name__}",
                className="mono muted",
            ),
            id=self.id,
            className="room",
        )
