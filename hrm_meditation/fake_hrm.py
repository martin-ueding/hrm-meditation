import math
import random

from hrm_meditation.interfaces import HeartRateMonitor


class FakeHeartRateMonitor(HeartRateMonitor):
    def __init__(self):
        self.step = 0

    def get_heart_rate(self) -> int:
        self.step += 1
        base = 80
        variable = 20 * math.cos(self.step * 2 * math.pi / 30)
        noise = random.gauss(0, 5)
        return int(base + variable + noise)
