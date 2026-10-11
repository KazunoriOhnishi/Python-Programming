# Circuit_STM_Blink.py
import board
import digitalio
import time

# LEDピンの設定(ボード内蔵LEDのピンを指定)
led = digitalio.DigitalInOut(board.C13)
led.direction = digitalio.Direction. OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
