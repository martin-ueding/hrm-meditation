import time

import click

from hrm_meditation.fake_hrm import FakeHeartRateMonitor
from hrm_meditation.garmin_hrm import GarminHeartRateMonitor
from hrm_meditation.observables import ExponentialMovingAverage


@click.command()
def main():
    hrm = FakeHeartRateMonitor()
    ema_obs = ExponentialMovingAverage()
    for i in range(10):
        heart_rate = hrm.get_heart_rate()
        ema_obs.feed_measurement(heart_rate)
        ema = ema_obs.get_observable()
        output = [" "] * 80
        output[int((ema - 40) / 2)] = "o"
        output[(heart_rate - 40) // 2] = "#"
        print(f"{heart_rate:3d}", "[", "".join(output), "]")


if __name__ == "__main__":
    main()
