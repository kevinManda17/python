from __future__ import annotations

import math
import random
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class LDRThresholds:
    """
    Thresholds for mapping an LDR raw reading to a categorical light level.

    Because the LDR is not calibrated, thresholds are pragmatic and can be tuned
    from observation. The only requirement is that low < medium.
    """
    low: int = 350
    medium: int = 650


def simulate_ldr_raw(now: datetime | None = None, noise: int = 40) -> int:
    """
    Simulate an LDR reading (0..1023) with a day-night pattern.

    - At night: lower readings (darker).
    - During the day: higher readings (brighter).
    - Adds bounded random noise.

    This is useful for development without any physical sensor.
    """
    now = now or datetime.now()
    hour = now.hour + now.minute / 60.0

    # Daylight curve: peak around midday (12:00), low around midnight.
    # Convert hour to angle so that noon = pi/2 and midnight = -pi/2.
    angle = (hour - 6.0) / 12.0 * math.pi  # approx sunrise around 6, sunset around 18
    base = int((math.sin(angle) * 0.5 + 0.5) * 900)  # 0..900
    base = max(0, min(1023, base))

    n = random.randint(-abs(noise), abs(noise))
    raw = base + n
    return max(0, min(1023, raw))


def ldr_to_light_level(raw_value: int, thresholds: LDRThresholds) -> str:
    """
    Convert a raw LDR value to a categorical light level.

    Returns one of: "LOW", "MEDIUM", "HIGH".
    """
    if raw_value < thresholds.low:
        return "LOW"
    if raw_value < thresholds.medium:
        return "MEDIUM"
    return "HIGH"
