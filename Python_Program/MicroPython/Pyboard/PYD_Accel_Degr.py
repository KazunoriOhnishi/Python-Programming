# PYD_Accel_Degr.py
import pyb
accel = pyb.Accel()
light = pyb.LED(3)
SENSITIVITY = 3
import math
import pyb

while True:
    x = accel.x()
    y = accel.y()
    z = accel.z()
    Angle = math.atan2(y, z)
    Angle = math.degrees(Angle)
    print("\r角度: %.2f 度    " % Angle, end="")

    if abs(x) > SENSITIVITY:
        light.on()
    else:
        light.off()

    pyb.delay(100)


