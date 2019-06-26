from onewire import OneWire
from ds18x20 import DS18X20
from machine import Pin
from time import sleep_ms
import time
import sys

bus = OneWire( Pin(12) )
ds = DS18X20( bus )
roms = ds.scan()
for rom in roms:
    print( rom )
    
while True:
    try:
        ds.convert_temp()
        #attendre OBLIGATOIREMENT 750ms
        sleep_ms( 750 )
        for rom in roms:
            temp_celsius = ds.read_temp(rom)
            print( "Temp: %s" % temp_celsius )        
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        sys.exit()
