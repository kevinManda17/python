from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, Any, List

from knowledge.facts import EnergyFacts


@dataclass(frozen=True)
class Rule:
    """
    A rule in the knowledge base.

    - name: identifier
    - condition: checks whether the rule applies
    - action: updates working memory / produces recommendations
    - priority: higher runs first (important when multiple rules match)
    """
    name: str
    condition: Callable[[EnergyFacts, Dict[str, Any]], bool]
    action: Callable[[EnergyFacts, Dict[str, Any]], None]
    priority: int = 0


def build_rules() -> List[Rule]:
    """
    Knowledge base for energy management.

    Working memory keys used:
    - mode: "NORMAL" | "CHARGE_MAX" | "ECONOMY" | "ECONOMY_STRICT"
    - allow_non_critical: bool
    - rationale: list[str]
    """
    rules: List[Rule] = []

    # --- Strict protection rules ---
    rules.append(Rule(
        name="R_STRICT_1_CRITICAL_BATT_AND_LOW_LIGHT",
        priority=100,
        condition=lambda f, wm: (f.battery_level == "CRITICAL" and f.light_level == "LOW"),
        action=_set_mode("ECONOMY_STRICT", allow_non_critical=False,
                         msg="Battery is CRITICAL and light is LOW -> enforce ECONOMY_STRICT and shed non-critical loads.")
    ))

    rules.append(Rule(
        name="R_STRICT_2_CRITICAL_BATT_AT_NIGHT",
        priority=90,
        condition=lambda f, wm: (f.battery_level == "CRITICAL" and f.time_period == "NIGHT"),
        action=_set_mode("ECONOMY_STRICT", allow_non_critical=False,
                         msg="Battery is CRITICAL at NIGHT -> enforce ECONOMY_STRICT and shed non-critical loads.")
    ))

    # --- Economy rules ---
    rules.append(Rule(
        name="R_ECO_1_LOW_BATT_AND_MEDIUM_OR_LOW_LIGHT",
        priority=70,
        condition=lambda f, wm: (f.battery_level == "LOW" and f.light_level in {"LOW", "MEDIUM"}),
        action=_set_mode("ECONOMY", allow_non_critical=False,
                         msg="Battery is LOW and light is not HIGH -> set ECONOMY and limit non-critical loads.")
    ))

    rules.append(Rule(
        name="R_ECO_2_HIGH_LOAD_WITH_NOT_HIGH_BATT",
        priority=60,
        condition=lambda f, wm: (f.load_demand == "HIGH" and f.battery_level in {"LOW", "CRITICAL"}),
        action=_set_mode("ECONOMY", allow_non_critical=False,
                         msg="Load demand is HIGH while battery is LOW/CRITICAL -> set ECONOMY and shed non-critical loads.")
    ))

    # --- Charging / utilization rules ---
    rules.append(Rule(
        name="R_CHARGE_1_HIGH_LIGHT_AND_LOW_BATT",
        priority=50,
        condition=lambda f, wm: (f.light_level == "HIGH" and f.battery_level in {"LOW", "CRITICAL"} and f.time_period == "DAY"),
        action=_set_mode("CHARGE_MAX", allow_non_critical=False,
                         msg="High light during DAY and battery LOW/CRITICAL -> prioritize charging (CHARGE_MAX), limit non-critical loads.")
    ))

    rules.append(Rule(
        name="R_CHARGE_2_HIGH_LIGHT_AND_NORMAL_BATT",
        priority=40,
        condition=lambda f, wm: (f.light_level == "HIGH" and f.battery_level == "NORMAL" and f.time_period == "DAY"),
        action=_set_mode("NORMAL", allow_non_critical=True,
                         msg="High light during DAY and battery NORMAL -> NORMAL mode, allow non-critical loads.")
    ))

    # --- Default / normal operation rules ---
    rules.append(Rule(
        name="R_NORMAL_1_HIGH_BATT",
        priority=30,
        condition=lambda f, wm: (f.battery_level == "HIGH"),
        action=_set_mode("NORMAL", allow_non_critical=True,
                         msg="Battery is HIGH -> NORMAL mode, allow non-critical loads.")
    ))

    rules.append(Rule(
        name="R_NORMAL_2_MEDIUM_LOAD_AND_NORMAL_BATT",
        priority=20,
        condition=lambda f, wm: (f.load_demand in {"LOW", "MEDIUM"} and f.battery_level == "NORMAL"),
        action=_set_mode("NORMAL", allow_non_critical=True,
                         msg="Load is LOW/MEDIUM and battery NORMAL -> NORMAL mode.")
    ))

    # Fallback: if nothing else matches
    rules.append(Rule(
        name="R_FALLBACK_SAFE",
        priority=-10,
        condition=lambda f, wm: True,
        action=_set_mode("ECONOMY", allow_non_critical=False,
                         msg="Fallback rule -> ECONOMY and limit non-critical loads as a safe default.")
    ))

    return rules


def _set_mode(mode: str, allow_non_critical: bool, msg: str) -> Callable[[EnergyFacts, Dict[str, Any]], None]:
    def _action(facts: EnergyFacts, wm: Dict[str, Any]) -> None:
        wm["mode"] = mode
        wm["allow_non_critical"] = allow_non_critical
        wm.setdefault("rationale", []).append(msg)
    return _action
