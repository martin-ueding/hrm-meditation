from hrm_meditation.interfaces import Observable


class ExponentialMovingAverage(Observable):
    def __init__(self):
        self.value = None
        self.decay = 0.9

    def feed_measurement(self, measurement: int):
        if self.value:
            self.value = self.decay * self.value + (1 - self.decay) * measurement
        else:
            self.value = measurement

    def get_observable(self) -> float:
        return self.value
