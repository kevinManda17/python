from __future__ import annotations

import random
from datetime import datetime

from data.ldr_simulation import LDRThresholds, simulate_ldr_raw, ldr_to_light_level
from knowledge.facts import (
    EnergyFacts,
    time_to_period,
    soc_to_battery_level,
    watts_to_load_demand,
)
from knowledge.rules import build_rules
from engine.inference_engine import ForwardChainingEngine
from decision.energy_manager import EnergyManager
from explanation.explanation import format_facts, format_decision


def simulate_battery_soc() -> float:
    """
    Simulate battery state-of-charge in percent (0..100).
    """
    return round(random.uniform(10, 95), 1)


def simulate_load_watts() -> float:
    """
    Simulate load demand in watts.
    """
    return round(random.uniform(80, 600), 1)


def main() -> None:
    now = datetime.now()

    # 1) Simulate / read raw values
    thresholds = LDRThresholds(low=350, medium=650)
    ldr_raw = simulate_ldr_raw(now=now, noise=40)
    battery_soc = simulate_battery_soc()
    load_watts = simulate_load_watts()

    # 2) Convert to categorical facts
    facts = EnergyFacts(
        time_period=time_to_period(now),
        light_level=ldr_to_light_level(ldr_raw, thresholds),
        battery_level=soc_to_battery_level(battery_soc),
        load_demand=watts_to_load_demand(load_watts),
        ldr_raw=ldr_raw,
        battery_soc=battery_soc,
        load_watts=load_watts,
    )

    # 3) Build knowledge base and run inference
    rules = build_rules()
    engine = ForwardChainingEngine(rules)
    manager = EnergyManager(engine)

    decision = manager.decide(facts)

    # 4) Print a full explanation
    print("=" * 60)
    print("SEGE — Expert System for Energy Management")
    print(f"Timestamp: {now.isoformat(timespec='seconds')}")
    print("=" * 60)
    print(format_facts(facts))
    print("-" * 60)
    print(format_decision(decision))
    print("=" * 60)


if __name__ == "__main__":
    main()
