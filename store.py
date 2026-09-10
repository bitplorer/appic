"""Host store — quantities and lists live here, never on MorphState.

Channel session plane refuses quantity MorphState. The foundry ledger
is RefState on page units plus this Host notebook for commissions.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")


@dataclass
class Commission:
    sku: str
    glaze: str
    plan: str
    note: str
    at: str = field(default_factory=_now)


@dataclass
class Host:
    commissions: list[Commission] = field(default_factory=list)
    bag: dict[str, int] = field(default_factory=dict)
    ledger: list[dict[str, Any]] = field(default_factory=list)
    authed: bool = False
    member: str = ""

    def add_bag(self, sku: str, n: int = 1) -> int:
        self.bag[sku] = int(self.bag.get(sku) or 0) + n
        self.ledger.append({"op": "bag.add", "sku": sku, "n": n, "at": _now()})
        return self.bag[sku]

    def bag_count(self) -> int:
        return sum(self.bag.values())

    def place(self, sku: str, glaze: str, plan: str, note: str) -> Commission:
        item = Commission(sku=sku, glaze=glaze, plan=plan, note=note)
        self.commissions.append(item)
        self.ledger.append({"op": "orders.place", "sku": sku, "at": item.at})
        return item


HOST = Host()

CATALOG = (
    {
        "sku": "basin",
        "name": "Night basin",
        "lede": "Stoneware. Wide rim. Holds water like a held breath.",
        "price": 180,
    },
    {
        "sku": "lamp",
        "name": "Tallow lamp",
        "lede": "Spun brass, smoked glass. One quiet flame.",
        "price": 240,
    },
    {
        "sku": "board",
        "name": "Oak board",
        "lede": "Waxed, then rested. Grain running the long way.",
        "price": 90,
    },
    {
        "sku": "cup",
        "name": "Kiln cup",
        "lede": "Thrown thin. Ash glaze. Fits the hand, not the shelf.",
        "price": 48,
    },
)
