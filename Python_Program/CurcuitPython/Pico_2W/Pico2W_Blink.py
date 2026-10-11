# Pico2W_Blink.py
import board
import digitalio
import time

# LEDピンの設定（ボード内蔵LEDのピンを指定）
# Raspberry Pi Picoの場合は board.LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True   # LED点灯
    time.sleep(0.5)    # 0.5秒待つ
    led.value = False  # LED消灯
    time.sleep(0.5)    # 0.5秒待つ

