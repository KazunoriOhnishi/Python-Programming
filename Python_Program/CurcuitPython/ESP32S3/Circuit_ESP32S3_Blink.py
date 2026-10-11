# Circuit_ESP32S3_Blink.py
import board
import digitalio
import time

# LEDピンの設定(ボード内蔵LEDのピンを指定)
# Raspberry Pi Picoの場合は board.LED
led = digitalio.DigitalInOut(board.GPIO2)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.2)
    led.value = False
    time.sleep(0.2)
