# SEGE — Expert System for Energy Management (Python)

SEGE (Smart Expert-based Grid Energy) is a **rule-based expert system** for energy management in a simplified off-grid / microgrid scenario.  
It uses **forward chaining** to apply energy rules based on:
- estimated solar availability (via simulated data or LDR categories),
- battery state (simulated SoC),
- load demand,
- time-of-day context.

The system outputs:
- an operating mode (NORMAL / CHARGE_MAX / ECONOMY / ECONOMY_STRICT),
- load actions (allow/deny non-critical loads),
- an explanation (which rules fired and why).

## Features
- Clean separation: facts, rules, inference engine, decision layer, explanation
- Deterministic and explainable decision-making
- Designed to be extended later with sensors, APIs (weather/irradiance), or ML prediction

## Project Structure
