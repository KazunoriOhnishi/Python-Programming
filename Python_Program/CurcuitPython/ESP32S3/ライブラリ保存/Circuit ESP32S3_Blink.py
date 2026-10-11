# Circuit ESP32S3_Blink.py

import time
import math
import board, busio
import adafruit_ssd1306
import adafruit_mpu6050

i2c = busio.I2C(scl=board.GPIO9, sda=board.GPIO8)

# OLED (SSD1306) : framebuf方式
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

# MPU6050(同じi2cを共有)
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    ax, ay, az = mpu.acceleration   # m/s^2
    gx, gy, gz = mpu.gyro           # rad/s

    angle = -math.atan2(ay, az) * (180 / math.pi)
    gy_deg = math.degrees(gy)       # deg/s

    # OLED表示
    display.fill(0)
    display.text("--- MPU6050 ---", 0, 0, 1)
    display.text("Angle: {:.2f}".format(angle), 0, 20, 1)
    display.text("Gyro: {:.2f}".format(gy_deg), 0, 40, 1)
    display.show()

    print("Angle : Angle={:.2f}".format(angle))
    print("Gyro  : Gyro={:.2f}".format(gy_deg))
    print()

    time.sleep(0.2)