# STM32_mpu6050.py
import machine

class accel:

    def __init__(self, i2c, addr=0x68):
        self.iic = i2c
        self.addr = addr
        self.iic.writeto_mem(self.addr, 0x6B, bytearray([0]))

    def get_values(self):
        r = self.iic.readfrom_mem(self.addr, 0x3B, 14)

        def to_int(h, l):
            return (
                (h << 8 | l) if not h & 0x80 else -(((h ^ 255) << 8) | (l ^ 255) + 1)
            )

        return {
            "AcX": to_int(r[0], r[1]),
            "AcY": to_int(r[2], r[3]),
            "AcZ": to_int(r[4], r[5]),
            "Tmp": to_int(r[6], r[7]) / 340.0 + 36.53,
            "GyX": to_int(r[8], r[9]),
            "GyY": to_int(r[10], r[11]),
            "GyZ": to_int(r[12], r[13]),
        }
