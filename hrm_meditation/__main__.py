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
        if heart_rate > ema + 2:
            color = "🔴"
        elif heart_rate >= ema - 2:
            color = "🟡"
        else:
            color = "🟢"
        print(f"Step {i:3d}: HR {heart_rate:3d}/min, HR EMA: {ema:5.1f}/min. {color}")


if __name__ == "__main__":
    main()
