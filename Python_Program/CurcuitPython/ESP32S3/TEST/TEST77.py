import time
import math
import board
import busio
import displayio
import terminalio
import i2cdisplaybus
import adafruit_displayio_ssd1306
import adafruit_mpu6050
from adafruit_display_text import label

displayio.release_displays()

i2c = busio.I2C(scl=board.GPIO9, sda=board.GPIO8)

# OLED (SSD1306)
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# MPU6050(同じi2cを共有)
mpu = adafruit_mpu6050.MPU6050(i2c)

# 表示用ラベル
group = displayio.Group()
title = label.Label(terminalio.FONT, text="--- MPU6050 ---", x=0, y=6)
angle_label = label.Label(terminalio.FONT, text="", x=0, y=26)
gyro_label = label.Label(terminalio.FONT, text="", x=0, y=46)
group.append(title)
group.append(angle_label)
group.append(gyro_label)
display.root_group = group

while True:
    ax, ay, az = mpu.acceleration   # m/s^2
    gx, gy, gz = mpu.gyro           # rad/s

    angle = -math.atan2(ay, az) * (180 / math.pi)
    gy_deg = math.degrees(gy)

    angle_label.text = "Angle: {:.2f}".format(angle)
    gyro_label.text = "Gyro: {:.2f}".format(gy_deg)

    print("Angle : Angle={:.2f}".format(angle))
    print("Gyro  : Gyro={:.2f}".format(gy_deg))
    print()

    time.sleep(0.2)