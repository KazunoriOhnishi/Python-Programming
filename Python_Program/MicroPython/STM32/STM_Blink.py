# STM_Blink.py
import machine
import time
# C13ピンを出力モードに設定
led = machine.Pin("C13", machine.Pin. OUT)
print("Lチカを開始します。終了するにはCtrl+Cを押してください。")
while True:
    led.value(0)
    time.sleep(0.5)
    led.value(1)
    time.sleep(0.5)
