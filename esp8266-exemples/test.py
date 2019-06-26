import machine
import uasyncio as asyncio

led1 = machine.Pin(2, machine.Pin.OUT)
led2 = machine.Pin(15, machine.Pin.OUT)


async def blink(led, delay):  # coroutine
    while True:
        print(led, "on")
        led.on()
        await asyncio.sleep_ms(delay)
        print(led, "off")
        led.off()
        await asyncio.sleep_ms(delay)


# boucle d’événements
loop = asyncio.get_event_loop()
loop.create_task(blink(led1, 500))  # Schedule ASAP
loop.create_task(blink(led2, 1000))  # Schedule ASAP
loop.run_forever()
