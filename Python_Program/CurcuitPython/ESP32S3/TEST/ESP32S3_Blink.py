# ESP32S3Blink.py
from machine import Pin
import time

led = Pin(2, Pin.OUT)   # D13 = GPIO48

while True:
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
