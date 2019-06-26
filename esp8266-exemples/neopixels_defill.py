"""
Neopixels
"""
NBPIXELS=4

import machine, neopixel, time
np = neopixel.NeoPixel(machine.Pin(14), NBPIXELS)

def defilement(color):
    for p in range(NBPIXELS):
        np[p] = color
        np[(p-1)%NBPIXELS]=(0,0,0)
        np.write()
        time.sleep_ms(100)

while(True):
    for c in range(0,256):
        defilement((c,255-c,0))




