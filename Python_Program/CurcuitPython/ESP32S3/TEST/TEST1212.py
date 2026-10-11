import board, busio, displayio
import i2cdisplaybus
import adafruit_ssd1306

displayio.release_displays()
i2c = busio.I2C(scl=board.GPIO9, sda=board.GPIO8, frequency=100000)
bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(bus, width=128, height=64)
print("display ok")