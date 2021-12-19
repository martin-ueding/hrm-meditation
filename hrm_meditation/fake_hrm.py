import random
import math

from hrm_meditation.interfaces import HeartRateMonitor


class FakeHeartRateMonitor(HeartRateMonitor):
    def __init__(self):
        self.step = 0

    def get_heart_rate(self) -> int:
        self.step += 1
        return int(80 + 20 * math.cos(self.step * 2 * math.pi / 30) + random.gauss(0, 5))
