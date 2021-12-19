class HeartRateMonitor:
    def get_heart_rate(self) -> int:
        raise NotImplementedError()


class Observable:
    def feed_measurement(self, measurement: int):
        raise NotImplementedError()

    def get_observable(self) -> float:
        raise NotImplementedError()
