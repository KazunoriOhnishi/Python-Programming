# ESP_WROOM_MPU_SSD.py

from mpu6050 import MPU6050
import ssd1306
from machine import I2C, Pin
import time
import math
PI = 3.1415

# I2Cインスタンスはここで1つだけ生成し、両方で共有する
i2c = I2C(1, scl=Pin(25), sda=Pin(26), freq=100000)

oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

mpu = MPU6050(i2c)       # 同じi2cインスタンスを渡す
mpu.MPU_Init()

while True:
    ax, ay, az = mpu.MPU_Get_Accelerometer()
    gx, gy, gz = mpu.MPU_Get_Gyroscope()
    Angle = -math.atan2(ay, az) * (180 / PI)

    oled.fill(0)
    oled.text("--- MPU6050 ---", 0, 0)
    oled.text("Angle: {:.2f}".format(Angle), 0, 20)
    oled.text("Gyro: {:.2f}".format(gy), 0, 40)
    oled.show()

    print("Angle : Angle={:.2f}".format(Angle))
    print("Gyro  : Gyro={:.2f}".format(gy))
    print(i2c.scan())
    print()

    time.sleep(0.2)