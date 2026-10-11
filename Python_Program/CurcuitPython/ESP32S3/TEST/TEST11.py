import board,busio
import time
i2c = busio.I2C(scl=board.GPIO9, sda=board.GPIO8)

while not i2c.try_lock():
    pass
print([hex(a) for a in i2c.scan()])
i2c.unlock()
