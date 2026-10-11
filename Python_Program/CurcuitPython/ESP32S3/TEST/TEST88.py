import board, busio
import i2cdisplaybus
import adafruit_ssd1306

print("start")
displayio.release_displays()
i2c = busio.I2C(scl=board.GPIO9, sda=board.GPIO8)
print("i2c ok")
bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
print("bus ok")
import adafruit_displayio_ssd1306
print("lib ok")
display = adafruit_displayio_ssd1306.SSD1306(bus, width=128, height=64)
print("display ok")