import os, sys
from pyGPIO.gpio import gpio, connector
import time

pin=4

gpio.setcfg(connector.GPIOp4, 1)


gpio.output(connector.GPIOp4, 1)
time.sleep(5)
gpio.output(connector.GPIOp4, 0)
print("end")