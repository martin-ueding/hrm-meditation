"""
This code is inspired by https://github.com/fg1/BLEHeartRateLogger/blob/master/BLEHeartRateLogger.py by fg1.
"""
import pexpect  # type: ignore

from hrm_meditation.interfaces import HeartRateMonitor


class GarminHeartRateMonitor(HeartRateMonitor):
    def __init__(self):
        self.gatt = pexpect.spawn(
            "gatttool", ["-b", "FA:1F:75:28:5B:2C", "-t", "random", "--interactive"]
        )
        self.gatt.expect(r"\[LE\]>")
        self.gatt.sendline("connect")

        rcode = self.gatt.expect(["Connection successful.", r"\[CON\]"], timeout=10)
        if rcode == 0:
            self.gatt.expect(r"\[LE\]>", timeout=10)
        else:
            raise RuntimeError("Could not connect to the HRM.")

    def get_heart_rate(self) -> int:
        self.gatt.sendline("char-read-hnd 0x0027")
        self.gatt.expect("Characteristic value/descriptor: .. (..) .*", timeout=10)
        reading = int(self.gatt.match.group(1), base=16)
        return reading
