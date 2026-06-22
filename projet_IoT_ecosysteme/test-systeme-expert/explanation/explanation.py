from __future__ import annotations

from typing import List

from knowledge.facts import EnergyFacts
from decision.energy_manager import EnergyDecision


def format_facts(facts: EnergyFacts) -> str:
    lines = []
    lines.append("FACTS (categorical)")
    lines.append(f"- Time period: {facts.time_period}")
    lines.append(f"- Light level: {facts.light_level} (raw={facts.ldr_raw})")
    lines.append(f"- Battery level: {facts.battery_level} (SoC={facts.battery_soc}%)")
    lines.append(f"- Load demand: {facts.load_demand} (load={facts.load_watts}W)")
    return "\n".join(lines)


def format_decision(decision: EnergyDecision) -> str:
    lines: List[str] = []
    lines.append("DECISION")
    lines.append(f"- Mode: {decision.mode}")
    lines.append(f"- Allow non-critical loads: {decision.allow_non_critical}")

    lines.append("\nACTIONS")
    for a in decision.actions:
        lines.append(f"- {a}")

    lines.append("\nFIRED RULES")
    if decision.fired_rules:
        for r in decision.fired_rules:
            lines.append(f"- {r}")
    else:
        lines.append("- (none)")

    lines.append("\nRATIONALE")
    if decision.rationale:
        for reason in decision.rationale:
            lines.append(f"- {reason}")
    else:
        lines.append("- (no rationale recorded)")

    return "\n".join(lines)
