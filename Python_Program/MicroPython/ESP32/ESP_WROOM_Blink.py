# ESP_WROOM_Blink.py

from time import sleep_ms
from machine import Pin

led=Pin(2,Pin.OUT)
try:
    while True:
        led.value(1)        #Set led turn on
        sleep_ms(1000)
        led.value(0)        #Set led turn off
        sleep_ms(1000)
except:
    pass





