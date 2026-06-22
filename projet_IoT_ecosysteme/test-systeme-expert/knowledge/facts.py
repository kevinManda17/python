from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class EnergyFacts:
    """
    Fact base: the system state used by the expert system.

    Categories are chosen to support clear rule-based reasoning.
    """
    time_period: str              # "NIGHT" | "DAY"
    light_level: str              # "LOW" | "MEDIUM" | "HIGH"
    battery_level: str            # "CRITICAL" | "LOW" | "NORMAL" | "HIGH"
    load_demand: str              # "LOW" | "MEDIUM" | "HIGH"

    # Optional details (kept for logging and future upgrades)
    ldr_raw: int | None = None
    battery_soc: float | None = None   # 0..100
    load_watts: float | None = None    # arbitrary


def time_to_period(now: datetime) -> str:
    """
    Simple time-of-day classifier.
    """
    return "DAY" if 6 <= now.hour < 18 else "NIGHT"


def soc_to_battery_level(soc_percent: float) -> str:
    """
    Convert a numeric state-of-charge (0..100) into categories.
    """
    if soc_percent < 20:
        return "CRITICAL"
    if soc_percent < 40:
        return "LOW"
    if soc_percent < 70:
        return "NORMAL"
    return "HIGH"


def watts_to_load_demand(load_watts: float) -> str:
    """
    Convert a numeric load level into categories.

    You can tune these thresholds depending on your scenario.
    """
    if load_watts < 150:
        return "LOW"
    if load_watts < 400:
        return "MEDIUM"
    return "HIGH"
