"""
scan i2c esp32
Scan i2c bus...
i2c devices found: 1
Decimal address:  60  | Hexa address:  0x3c
"""

from machine import Pin, I2C
from bme280 import *

i2c = I2C(scl=Pin(5), sda=Pin(4))
bmp = BME280(i2c=i2c, address=0x76 )

print(bmp.values)

