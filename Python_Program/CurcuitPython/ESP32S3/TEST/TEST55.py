import board, busio
i2c = busio.I2C(scl=board.GPIO9, sda=board.GPIO8)
print("ok")