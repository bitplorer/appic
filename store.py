"""Foundry Host memory. Domain stock lives here — never on MorphState.

Isolation: no ux_channel. Quantity is RefState on Components; this module
is the Host DB for commissions, bag, ledger, notices, kiln queue, thrown
bodies, locked recipes, vitrine, briefs, the studio floor, sky climate,
the shared hearth the Night Watch keeps, occupancy, the circadian clock,
the vessel on the cloth, kintsugi joins, gifts, lineage, the living score,
the chorus of hands, eclipse climate, the companion vessel, and wax seals.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any

IST = timezone(timedelta(hours=5, minutes=30))

BANDS = ("night", "dawn", "noon", "dusk")
STAGES = ("brief", "thrown", "glazed", "firing", "drawn", "mended", "gifted")
BREAKS = ("lip", "belly", "foot")
DESTINATIONS = ("keep", "send", "archive")
PITCHES = ("C", "D", "E", "F", "G", "A", "B")
VOICES = ("wheel", "glaze", "kiln", "watch")
CHORUS_ORDERS = ("rise", "fall", "pulse")
ECLIPSE_PHASES = ("clear", "wax", "full", "wane")
ROOM_PITCH = {
    "table": "G",
    "now": "A",
    "vessel": "E",
    "watch": "D",
    "kiln": "C",
    "wheel": "F",
    "glaze": "B",
    "vitrine": "A",
    "kintsugi": "E",
    "gift": "C",
    "score": "G",
    "chorus": "D",
    "eclipse": "C",
    "duet": "F",
    "provenance": "B",
    "threshold": "A",
    "brief": "G",
    "air": "E",
    "lineage": "D",
}

# Staff: five paths. Notes sit on or between them. No public `line` tag.
STAFF_LINES = (16, 28, 40, 52, 64)
NOTE_Y = {"B": 22, "A": 28, "G": 34, "F": 40, "E": 46, "D": 52, "C": 64}


def ist_hour() -> int:
    return datetime.now(IST).hour


def band_for_hour(h: int) -> str:
    h = int(h) % 24
    if 5 <= h < 8:
        return "dawn"
    if 8 <= h < 16:
        return "noon"
    if 16 <= h < 22:
        return "dusk"
    return "night"


def clock_label(h: int) -> str:
    return f"{int(h) % 24:02d}:00"


def _now() -> str:
    return datetime.now(IST).strftime("%H:%M:%S")


def waveform_d(band: str) -> str:
    """Resonance of the hearth. Peak is denser. Idle is a still line."""
    key = str(band or "idle")
    if key in ("peak", "middle"):
        return "M0 18 Q8 2 16 18 T32 18 T48 18 T64 18 T80 18 T96 18 T112 18 T128 18 T144 18 T160 18 T176 18 T192 18 T208 18"
    if key in ("soak", "first", "warm"):
        return "M0 18 Q16 8 32 18 T64 18 T96 18 T128 18 T160 18 T192 18 T224 18"
    if key in ("cool", "last"):
        return "M0 18 Q24 12 48 18 T96 18 T144 18 T192 18"
    if key in ("done",):
        return "M0 18 Q40 14 80 18 T160 18 T240 18"
    return "M0 18 L240 18"


def staff_line_d(y: int, width: int = 240) -> str:
    return f"M0 {y} L{width} {y}"


def note_cy(pitch: str) -> int:
    return NOTE_Y.get(str(pitch or "G"), 34)


VESSEL_BODY = (
    "M50 10 C36 10 28 22 28 36 L32 86 C32 102 40 114 50 114 "
    "C60 114 68 102 68 86 L72 36 C72 22 64 10 50 10 Z"
)
VESSEL_WELL = (
    "M50 26 C42 26 40 34 40 40 L42 72 C42 80 46 84 50 84 "
    "C54 84 58 80 58 72 L60 40 C60 34 58 26 50 26 Z"
)
CRACKS = {
    "lip": "M34 22 Q50 30 66 22",
    "belly": "M32 54 Q50 44 68 60",
    "foot": "M40 96 Q50 88 60 96",
}


def crack_d(where: str) -> str:
    return CRACKS.get(str(where or ""), "")


@dataclass
class Host:
    notice: str = ""
    intent: str = "hold the table"
    pulse: int = 0
    bag: list[str] = field(default_factory=list)
    ledger: list[dict[str, Any]] = field(default_factory=list)
    commissions: list[dict[str, Any]] = field(default_factory=list)
    pending_fire: dict[str, Any] | None = None
    last_firing: dict[str, Any] | None = None
    authed: str = ""
    thrown: list[dict[str, Any]] = field(default_factory=list)
    wheel_piece: dict[str, Any] | None = None
    recipes: list[dict[str, Any]] = field(default_factory=list)
    locked_glaze: dict[str, Any] | None = None
    vitrine: list[dict[str, Any]] = field(default_factory=list)
    ratings: dict[str, str] = field(default_factory=dict)
    briefs: list[dict[str, Any]] = field(default_factory=list)
    last_brief: dict[str, Any] | None = None
    hands: list[str] = field(default_factory=list)
    sky_band: str = "night"
    firing: bool = False
    heat_remain: int = 0
    watch_bells: list[str] = field(default_factory=list)
    atmosphere: str = "oxidation"
    cone: int = 10
    window: str = "today"
    day: str = "thu"
    remain_h: int = 14
    _piece_n: int = 0
    clock_h: int = field(default_factory=ist_hour)
    auto_sky: bool = True
    occupied: list[str] = field(default_factory=list)
    heat_trace: list[int] = field(default_factory=list)
    vessel: dict[str, Any] | None = None
    lineage: list[dict[str, Any]] = field(default_factory=list)
    gifts: list[dict[str, Any]] = field(default_factory=list)
    repairs: list[dict[str, Any]] = field(default_factory=list)
    join_n: int = 0
    score: list[dict[str, Any]] = field(default_factory=list)
    voices: list[str] = field(default_factory=lambda: list(VOICES))
    chorus_order: str = "rise"
    eclipse: bool = False
    eclipse_phase: str = "clear"
    eclipse_n: int = 0
    duet: dict[str, Any] | None = None
    seals: list[dict[str, Any]] = field(default_factory=list)
    seal_n: int = 0

    def log(self, verb: str, detail: str = "", kind: str = "morph") -> None:
        self.ledger.append(
            {"at": _now(), "verb": verb, "detail": detail, "kind": kind}
        )
        self.ledger = self.ledger[-48:]
        self.pulse += 1

    def next_id(self) -> str:
        self._piece_n += 1
        return f"p{self._piece_n:03d}"

    def score_write(self, verb: str, room: str = "", pitch: str = "") -> dict[str, Any]:
        """Every named verb is a note. Host stock, never MorphState(list). SCORE-1."""
        room = str(room or (self.occupied[0] if self.occupied else "table"))
        pitch = pitch if pitch in PITCHES else ROOM_PITCH.get(room, "G")
        row = {
            "id": f"n{len(self.score) + 1:03d}",
            "at": _now(),
            "verb": str(verb or "rest"),
            "room": room,
            "pitch": pitch,
        }
        self.score.append(row)
        self.score = self.score[-32:]
        return row

    def press_seal(self, verb: str, cap: str = "wax.press") -> dict[str, Any]:
        """One-shot wax. Parent is the previous seal. PROVENANCE-1."""
        parent = str(self.seals[-1]["id"]) if self.seals else "house"
        self.seal_n += 1
        row = {
            "id": f"s{self.seal_n:03d}",
            "parent": parent,
            "verb": str(verb or "press"),
            "cap": str(cap or "wax.press"),
            "at": _now(),
            "room": self.occupied[0] if self.occupied else "table",
        }
        self.seals.append(row)
        self.seals = self.seals[-24:]
        self.log(str(verb or "wax.press"), row["id"], "cap")
        return row

    def veil(self, phase: str = "full") -> str:
        """Name an eclipse. Light is occluded. ECLIPSE-1."""
        phase = phase if phase in ECLIPSE_PHASES else "full"
        if phase == "clear":
            return self.unveil()
        self.eclipse = True
        self.eclipse_phase = phase
        self.eclipse_n += 1
        self.auto_sky = False
        self.notice = f"The house is named {phase} eclipse."
        self.log("eclipse.veil", phase)
        self.score_write("eclipse.veil", "eclipse", "C")
        return phase

    def unveil(self) -> str:
        self.eclipse = False
        self.eclipse_phase = "clear"
        self.notice = "The umbra lifted."
        self.log("eclipse.unveil", "clear")
        self.score_write("eclipse.unveil", "eclipse", "G")
        return "clear"

    def seat_duet(
        self,
        *,
        stage: str = "drawn",
        clay: str = "",
        glaze: str = "",
        note: str = "",
        piece_id: str = "",
    ) -> dict[str, Any]:
        """Companion vessel. Presence identity is the duet id. DUET-1."""
        current = dict(self.duet or {})
        row = {
            "id": piece_id or current.get("id") or f"d{self.next_id()[1:]}",
            "stage": stage if stage in STAGES else str(current.get("stage") or "drawn"),
            "clay": clay or current.get("clay") or "stoneware",
            "glaze": glaze or current.get("glaze") or "tenmoku",
            "note": note or current.get("note") or "The other hand.",
            "break": current.get("break") or "",
            "join": current.get("join") or "",
            "parent": current.get("parent") or "house",
        }
        self.duet = row
        return row

    def pass_duet(self) -> dict[str, Any] | None:
        """Share presence from the cloth to the companion cradle. XOR share."""
        if not self.vessel:
            return None
        row = dict(self.vessel)
        row["id"] = f"d{str(row.get('id') or '000')[1:]}" if str(row.get("id") or "").startswith("p") else str(row.get("id") or self.next_id())
        self.duet = row
        self.notice = "The vessel crossed to the companion."
        self.log("duet.pass", str(row.get("id")))
        self.score_write("duet.pass", "duet", "F")
        return row

    def _line(self, row: dict[str, Any]) -> None:
        self.lineage.append(
            {
                "id": str(row.get("id") or ""),
                "parent": str(row.get("parent") or "house"),
                "stage": str(row.get("stage") or ""),
                "clay": str(row.get("clay") or ""),
                "glaze": str(row.get("glaze") or ""),
                "at": _now(),
            }
        )
        self.lineage = self.lineage[-64:]

    def seat(
        self,
        *,
        stage: str,
        clay: str = "",
        glaze: str = "",
        note: str = "",
        parent: str = "",
        piece_id: str = "",
    ) -> dict[str, Any]:
        """Seat a vessel on the cloth. Presence identity is the piece id."""
        current = dict(self.vessel or {})
        stage = stage if stage in STAGES else str(current.get("stage") or "brief")
        row = {
            "id": piece_id or current.get("id") or self.next_id(),
            "stage": stage,
            "clay": clay or current.get("clay") or "porcelain",
            "glaze": glaze or current.get("glaze") or "ash",
            "note": note or current.get("note") or "",
            "break": current.get("break") or "",
            "join": current.get("join") or "",
            "parent": parent or current.get("parent") or "house",
        }
        self.vessel = row
        self._line(row)
        return row

    def crack(self, where: str) -> dict[str, Any] | None:
        if not self.vessel:
            return None
        if where not in BREAKS:
            where = "belly"
        self.vessel["break"] = where
        self.vessel["join"] = ""
        self.log("vessel.crack", where)
        self.notice = f"A break at the {where}."
        return self.vessel

    def mend(self, where: str = "") -> dict[str, Any] | None:
        """Kintsugi. Brass is the join. Host stock, never MorphState(int)."""
        if not self.vessel:
            return None
        join = where if where in BREAKS else (self.vessel.get("break") or "belly")
        self.vessel["join"] = join
        self.vessel["break"] = ""
        self.vessel["stage"] = "mended"
        self.join_n += 1
        self.repairs.append(
            {
                "id": self.vessel.get("id"),
                "join": join,
                "at": _now(),
                "clay": self.vessel.get("clay"),
            }
        )
        self.repairs = self.repairs[-24:]
        self._line(self.vessel)
        self.log("kintsugi.join", str(join), "cap")
        self.press_seal("repair.join", "repair.join")
        self.notice = f"Brass holds the {join}."
        return self.vessel

    def gift(self, dest: str) -> dict[str, Any] | None:
        """The vessel leaves the house. Presence ends. Host stock."""
        if not self.vessel:
            return None
        if dest not in DESTINATIONS:
            dest = "send"
        row = dict(self.vessel)
        row["dest"] = dest
        row["stage"] = "gifted"
        row["at"] = _now()
        self.gifts.append(row)
        self.gifts = self.gifts[-24:]
        vid = str(row.get("id") or "")
        self.vitrine = [p for p in self.vitrine if str(p.get("id")) != vid]
        self._line(row)
        self.log("gift.send", f"{vid}/{dest}", "cap")
        self.press_seal("gift.send", "gift.send")
        self.notice = "The vessel left the cloth."
        self.vessel = None
        return row

    def draw(self, piece: dict[str, Any] | None) -> dict[str, Any]:
        row = dict(piece or {})
        row.setdefault("id", self.next_id())
        row.setdefault("band", "done")
        self.vitrine.append(row)
        self.vitrine = self.vitrine[-24:]
        self.seat(
            stage="drawn",
            clay=str(row.get("clay") or ""),
            glaze=str(row.get("glaze") or ""),
            note=str(row.get("note") or ""),
            piece_id=str(row.get("id") or ""),
        )
        return row

    def light(self, piece: dict[str, Any] | None) -> None:
        self.firing = True
        self.heat_remain = 12
        self.last_firing = dict(piece or {})
        self.pending_fire = None
        self.heat_trace.append(12)
        self.heat_trace = self.heat_trace[-24:]
        self.seat(
            stage="firing",
            clay=str((piece or {}).get("clay") or ""),
            glaze=str((piece or {}).get("glaze") or ""),
            note=str((piece or {}).get("note") or ""),
        )

    def tick_heat(self) -> str:
        """Advance shared hearth heat. Returns the kiln band name."""
        if not self.firing:
            return "idle"
        self.heat_remain = max(0, int(self.heat_remain) - 1)
        self.heat_trace.append(int(self.heat_remain))
        self.heat_trace = self.heat_trace[-24:]
        if self.heat_remain <= 0:
            self.firing = False
            self.heat_remain = 0
            self.notice = "Drawn from the kiln."
            self.log("kiln.drawn", str((self.last_firing or {}).get("clay", "")), "cap")
            self.draw(
                {
                    "clay": (self.last_firing or {}).get("clay", "clay"),
                    "glaze": (self.last_firing or {}).get("glaze", "glaze"),
                    "note": (self.last_firing or {}).get("note", ""),
                    "band": "done",
                }
            )
            return "done"
        if self.heat_remain <= 2:
            return "cool"
        if self.heat_remain <= 5:
            return "peak"
        if self.heat_remain <= 8:
            return "soak"
        return "warm"

    def sync_sky(self) -> str:
        if self.auto_sky:
            self.sky_band = band_for_hour(self.clock_h)
        if self.sky_band not in BANDS:
            self.sky_band = "night"
        return self.sky_band

    def tick_clock(self) -> str:
        self.clock_h = (int(self.clock_h) + 1) % 24
        if self.eclipse and self.eclipse_phase == "full":
            self.eclipse_phase = "wane"
        elif self.eclipse and self.eclipse_phase == "wane":
            self.unveil()
        return self.sync_sky()

    def occupy(self, room: str) -> None:
        room = str(room or "").strip()
        if not room:
            return
        already = bool(self.occupied) and self.occupied[0] == room
        self.occupied = [room] + [r for r in self.occupied if r != room]
        self.occupied = self.occupied[:8]
        if not already:
            self.score_write(f"walk.{room}", room)

    def kpi(self) -> dict[str, int]:
        return {
            "pulse": self.pulse,
            "bag": len(self.bag),
            "seals": len(self.seals) or sum(1 for row in self.ledger if row.get("kind") == "cap"),
            "commissions": len(self.commissions),
            "thrown": len(self.thrown),
            "drawn": len(self.vitrine),
            "heat": int(self.heat_remain),
            "present": len(self.occupied),
            "joins": int(self.join_n),
            "gifts": len(self.gifts),
            "notes": len(self.score),
            "voices": len(self.voices),
        }


def _seed(host: Host) -> Host:
    host.sync_sky()
    host.briefs = [
        {"intent": "a bowl that holds night", "at": "05:12:00"},
        {"intent": "a lip thin enough to vanish", "at": "05:40:00"},
    ]
    host.last_brief = host.briefs[-1]
    host.thrown = [
        {"id": "p001", "clay": "porcelain", "stage": "open"},
        {"id": "p002", "clay": "stoneware", "stage": "trim"},
    ]
    host.vitrine = [
        {
            "id": "p000",
            "clay": "porcelain",
            "glaze": "celadon",
            "band": "done",
            "note": "thin lip, still warm in the hand",
        }
    ]
    host.hands = ["the table is lit", "a pulse crossed the cloth"]
    host.occupied = ["table"]
    host.heat_trace = [0, 0, 2, 4, 7, 9, 8, 6, 4, 2, 0]
    host.seat(
        stage="drawn",
        clay="porcelain",
        glaze="celadon",
        note="thin lip, still warm in the hand",
        piece_id="p000",
    )
    host.seat_duet(
        stage="thrown",
        clay="stoneware",
        glaze="tenmoku",
        note="The other hand waits.",
        piece_id="d002",
    )
    host.score_write("house.open", "table", "G")
    host.score_write("vessel.seat", "vessel", "E")
    host.press_seal("house.open", "channel.boot")
    host.notice = "The house is listening."
    host.log("house.open", host.sky_band)
    return host


HOST = _seed(Host())
