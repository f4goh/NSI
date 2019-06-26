"""
timer irq
the ESP32 has 4 hardware timers. For this example, we will use timer 0.
"""
   
import machine
 
led = machine.Pin(16, machine.Pin.OUT)
timer = machine.Timer(0)


def handleInterrupt(timer):
    global ledState
    ledState^=1
    led.value(ledState)

ledState=0

timer.init(freq=1000, mode=machine.Timer.PERIODIC, callback=handleInterrupt)
#timer.init(period=1000, mode=machine.Timer.PERIODIC, callback=handleInterrupt)

 
while True:
      pass

