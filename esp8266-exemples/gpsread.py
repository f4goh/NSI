"""
esp32 pinout
ValueError: UART(2) does not existgpio16 rx relié à la sortie GPS
gpio17 tx
"""
import uasyncio as asyncio
from machine import UART

#uart = UART(2, 9600)
uart=UART(0,9600)


async def receiver():
    sreader = asyncio.StreamReader(uart)
    while True:
        res = await sreader.readline()
        print('Recieved', nmea)
        nmea=res.split(b',')
        if nmea[0]==b'$GPGGA':
            print('Recieved', nmea)
            #print(int(float(nmea[1].decode())),end=',')
            #print('latitude :',float(nmea[2].decode()),end=',')
            #print(' longitude :',float(nmea[4].decode()))


loop = asyncio.get_event_loop()
loop.create_task(receiver())
loop.run_forever()