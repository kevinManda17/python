from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List

from engine.inference_engine import ForwardChainingEngine, InferenceResult
from knowledge.facts import EnergyFacts


@dataclass
class EnergyDecision:
    mode: str
    allow_non_critical: bool
    actions: List[str]
    fired_rules: List[str]
    rationale: List[str]


class EnergyManager:
    """
    High-level decision layer that interprets inference results into actionable outputs.
    """
    def __init__(self, engine: ForwardChainingEngine) -> None:
        self.engine = engine

    def decide(self, facts: EnergyFacts) -> EnergyDecision:
        result: InferenceResult = self.engine.run(facts)

        wm: Dict[str, Any] = result.working_memory
        mode = wm.get("mode", "ECONOMY")
        allow_non_critical = bool(wm.get("allow_non_critical", False))
        rationale = list(wm.get("rationale", []))

        actions = self._build_actions(mode, allow_non_critical, facts)

        return EnergyDecision(
            mode=mode,
            allow_non_critical=allow_non_critical,
            actions=actions,
            fired_rules=result.fired_rules,
            rationale=rationale,
        )

    def _build_actions(self, mode: str, allow_non_critical: bool, facts: EnergyFacts) -> List[str]:
        actions: List[str] = []

        # Generic actions by mode
        if mode == "CHARGE_MAX":
            actions.append("Prioritize charging the battery (reduce discretionary loads).")
        elif mode == "ECONOMY_STRICT":
            actions.append("Aggressively reduce consumption to protect the battery.")
        elif mode == "ECONOMY":
            actions.append("Reduce consumption and avoid non-essential loads.")
        else:
            actions.append("Operate normally and maintain user comfort.")

        # Load shedding policy
        if allow_non_critical:
            actions.append("Non-critical loads: ALLOWED.")
        else:
            actions.append("Non-critical loads: DISABLED / SHED.")

        # Context-specific hints (optional)
        if facts.time_period == "NIGHT" and facts.battery_level in {"LOW", "CRITICAL"}:
            actions.append("Night-time conservation recommended due to limited production.")

        if facts.light_level == "HIGH" and facts.time_period == "DAY":
            actions.append("Daylight available: consider scheduling energy-intensive tasks now.")

        return actions
