import board, busio
import adafruit_ssd1306

i2c = busio.I2C(scl=board.GPIO9, sda=board.GPIO8, frequency=100000)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

oled.fill(0)
oled.text("Hello", 0, 0, 1)
oled.text("ESP32-S3", 0, 16, 1)
oled.show()
print("show ok")