"""Page unit: commission.py → Commission — wizard covering remaining field types."""
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
    form,
    h1,
    h2,
    input_,
    label,
    maybe_plan,
    notify,
    p,
    section,
    span,
    textarea,
    tick,
    update_with,
)

STEPS = (("intent", "Intent"), ("material", "Material"), ("finish", "Finish"), ("seal", "Seal"))
FINISHES = (("oil", "Oil"), ("wax", "Wax"), ("raw", "Raw"))
EXTRAS = (("cloth", "Care cloth"), ("box", "Gift box"), ("note", "Hand note"))


class Commission(Component):
    id = "commission"
    step = MorphState("intent")
    title = MorphState("A piece for the table")
    finish = MorphState("oil")
    extras = RefState(("cloth",))
    note = RefState("")
    thickness = RefState(18)
    window = MorphState("august")
    iso = RefState("2026-08-27")
    files = RefState(())
    secret = RefState("")
    reveal = MorphState(False)
    otp = RefState("")
    draft = RefState("")
    dirty = MorphState(False)
    valid = MorphState("idle")
    stamp = MorphState("idle")

    def render(self):
        step = str(self.step or "intent")
        segs = [
            act(
                "commission.set_step",
                lab,
                kind="chip-on" if key == step else "chip",
                key=key,
            )
            for key, lab in STEPS
        ]
        body = self._body(step)
        return section(
            div(
                h1("Commission"),
                p("Named step is MorphState. Magnitudes silent. Seal is a Cap.", className="muted"),
                className="section-head",
            ),
            div(*segs, className="chip-row"),
            body,
            id=self.id,
            className="page",
        )

    def _body(self, step: str):
        if step == "intent":
            n = len(str(self.note or ""))
            return div(
                h2("What should exist"),
                form(
                    label("Working title"),
                    input_(
                        type="text",
                        name="title",
                        value=str(self.title or ""),
                        className="field",
                        **control("commission.save_title"),
                    ),
                    label(f"Note · {n}/180"),
                    textarea(
                        str(self.note or ""),
                        name="note",
                        rows="4",
                        className="field",
                        maxlength="180",
                    ),
                    button("Hold draft", type="submit", className="btn btn-primary", **control("commission.save_intent")),
                    className="stack",
                    method="post",
                    action="/action/commission.save_intent",
                    data_ux="1",
                ),
                p("Autosave marks dirty without charging.", className="muted tiny"),
                className="card stack",
            )
        if step == "material":
            finish = str(self.finish or "oil")
            picked = set(self.extras or ())
            radios = [
                act("commission.set_finish", lab, kind="chip-on" if key == finish else "chip", key=key)
                for key, lab in FINISHES
            ]
            checks = [
                act(
                    "commission.toggle_extra",
                    lab,
                    kind="chip-on" if key in picked else "chip",
                    key=key,
                )
                for key, lab in EXTRAS
            ]
            return div(
                h2("Material"),
                p("Finish is a name. Extras are a silent set.", className="muted"),
                div(*radios, className="chip-row"),
                div(*checks, className="chip-row"),
                p(f"Thickness {int(self.thickness or 18)} mm", className="mono"),
                div(
                    act("commission.thinner", "Thinner", kind="ghost"),
                    act("commission.thicker", "Thicker", kind="ghost"),
                    className="row",
                ),
                className="card stack",
            )
        if step == "finish":
            shown = str(self.secret or "") if self.reveal else "········"
            files = ", ".join(self.files or ()) or "none"
            return div(
                h2("Finish window"),
                div(
                    act("commission.set_window", "July", kind="chip-on" if self.window == "july" else "chip", key="july"),
                    act("commission.set_window", "August", kind="chip-on" if self.window == "august" else "chip", key="august"),
                    act("commission.set_window", "September", kind="chip-on" if self.window == "september" else "chip", key="september"),
                    className="chip-row",
                ),
                p(f"ISO held silently · {self.iso}", className="mono"),
                p(f"References · {files}", className="muted"),
                act("commission.drop", "Drop a reference", kind="ghost", name="bench-sketch.svg"),
                p(f"Atelier code · {shown}", className="mono"),
                act("commission.toggle_reveal", "Reveal" if not self.reveal else "Hide", kind="text"),
                form(
                    input_(type="text", name="secret", placeholder="House code", className="field", value=str(self.secret or "")),
                    button("Store", type="submit", className="btn btn-ghost", **control("commission.set_secret")),
                    className="row",
                    method="post",
                    action="/action/commission.set_secret",
                    data_ux="1",
                ),
                className="card stack",
            )
        sealed = str(self.valid)
        return div(
            h2("Seal"),
            p("OTP digits are silent. Verify is orders.place-adjacent identity — a Cap.", className="muted"),
            form(
                input_(
                    type="text",
                    name="otp",
                    inputmode="numeric",
                    maxlength="4",
                    placeholder="••••",
                    className="field field-otp",
                    value=str(self.otp or ""),
                ),
                button("Verify", type="submit", className="btn btn-primary", **control("commission.verify")),
                className="row",
                method="post",
                action="/action/commission.verify",
                data_ux="1",
            ),
            span(sealed, className="chip"),
            act("commission.next", "Place commission", kind="primary") if sealed == "ok" else None,
            className="card stack",
        )

    @action(caps=())
    def set_step(self, key: str = "intent", **kwargs):
        if key in dict(STEPS):
            self.step = key
        return update_with(self, maybe_plan("step", "#commission", ms=160))

    @action(caps=())
    def save_title(self, title: str = "", **kwargs):
        if title:
            self.title = title
        self.dirty = True
        tick(self)
        return update_with(self)

    @action(caps=())
    def save_intent(self, title: str = "", note: str = "", **kwargs):
        if title:
            self.title = title
        self.note = (note or "")[:180]
        self.draft = self.note
        self.dirty = False
        tick(self)
        self.step = "material"
        return update_with(self, extra_ops=[notify("Intent held")])

    @action(caps=())
    def set_finish(self, key: str = "oil", **kwargs):
        self.finish = key
        return update_with(self)

    @action(caps=())
    def toggle_extra(self, key: str = "", **kwargs):
        have = set(self.extras or ())
        if key in have:
            have.remove(key)
        else:
            have.add(key)
        self.extras = tuple(sorted(have))
        tick(self)
        return update_with(self)

    @action(caps=())
    def thinner(self, **kwargs):
        self.thickness = max(8, int(self.thickness or 18) - 2)
        tick(self)
        return update_with(self)

    @action(caps=())
    def thicker(self, **kwargs):
        self.thickness = min(40, int(self.thickness or 18) + 2)
        tick(self)
        return update_with(self)

    @action(caps=())
    def set_window(self, key: str = "august", **kwargs):
        self.window = key
        month = {"july": "07", "august": "08", "september": "09"}.get(key, "08")
        self.iso = f"2026-{month}-27"
        tick(self)
        return update_with(self)

    @action(caps=())
    def drop(self, name: str = "sketch.svg", **kwargs):
        self.files = tuple(self.files or ()) + (name,)
        tick(self)
        return update_with(self, extra_ops=[notify(f"Held {name}")])

    @action(caps=())
    def toggle_reveal(self, **kwargs):
        self.reveal = not bool(self.reveal)
        return update_with(self)

    @action(caps=())
    def set_secret(self, secret: str = "", **kwargs):
        self.secret = secret
        tick(self)
        return update_with(self)

    @action(caps=("identity.verify",))
    def verify(self, otp: str = "", **kwargs):
        self.otp = (otp or "").strip()
        ok = self.otp == "2048" or len(self.otp) == 4
        self.valid = "ok" if ok else "err"
        tick(self)
        return update_with(self, extra_ops=[notify("Verified" if ok else "Need four digits (try 2048)")])

    @action(caps=("orders.place",))
    def next(self, **kwargs):
        HOST.commissions.append(
            {
                "title": str(self.title),
                "finish": str(self.finish),
                "extras": tuple(self.extras or ()),
                "iso": str(self.iso),
            }
        )
        HOST.kpi["open"] = int(HOST.kpi.get("open", 0)) + 1
        self.step = "intent"
        self.valid = "idle"
        tick(self)
        return update_with(self, extra_ops=[notify("Commission placed")])
