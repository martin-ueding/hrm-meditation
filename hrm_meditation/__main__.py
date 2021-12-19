import click
import time

from hrm_meditation.garmin_hrm import GarminHeartRateMonitor


@click.command()
def main():
    hrm = GarminHeartRateMonitor()
    for i in range(5):
        rate = hrm.get_heart_rate()
        print(rate)
        time.sleep(3)


if __name__ == "__main__":
    main()