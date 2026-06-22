from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

from knowledge.facts import EnergyFacts
from knowledge.rules import Rule


@dataclass
class InferenceResult:
    """
    Result of inference.
    """
    working_memory: Dict[str, Any]
    fired_rules: List[str]


class ForwardChainingEngine:
    """
    Simple forward-chaining inference engine.

    Strategy:
    - Sort rules by priority desc
    - Evaluate conditions in order
    - Fire the first rule that sets a 'mode' (or changes WM)
    - Continue until no new rule changes WM, or max_steps reached
    """
    def __init__(self, rules: List[Rule]) -> None:
        self.rules = sorted(rules, key=lambda r: r.priority, reverse=True)

    def run(self, facts: EnergyFacts, max_steps: int = 20) -> InferenceResult:
        wm: Dict[str, Any] = {"rationale": []}
        fired: List[str] = []

        for _ in range(max_steps):
            changed = False

            for rule in self.rules:
                if rule.condition(facts, wm):
                    before = self._snapshot(wm)
                    rule.action(facts, wm)
                    after = self._snapshot(wm)

                    if after != before:
                        fired.append(rule.name)
                        changed = True

                        # If a "mode" is set by a high-priority rule, we can stop early.
                        # This keeps the system deterministic and easy to explain.
                        if "mode" in wm and rule.priority >= 20:
                            return InferenceResult(working_memory=wm, fired_rules=fired)

            if not changed:
                break

        return InferenceResult(working_memory=wm, fired_rules=fired)

    @staticmethod
    def _snapshot(wm: Dict[str, Any]) -> Tuple:
        """
        Snapshot a subset of working memory relevant to decision-making.
        """
        return (
            wm.get("mode"),
            wm.get("allow_non_critical"),
            tuple(wm.get("rationale", [])),
        )
