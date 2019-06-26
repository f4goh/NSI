"""
analog read
"""

import machine
import time
adc = machine.ADC(0)

while True:
    valeur=adc.read()
    print(valeur)
    time.sleep(1)
    
