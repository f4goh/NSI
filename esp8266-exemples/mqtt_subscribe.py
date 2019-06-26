from umqtt.robust import MQTTClient
import network
import sys
import time
from time import sleep_ms
from machine import Pin
from onewire import OneWire
from ds18x20 import DS18X20

def cb(topic, msg):
    print((topic, msg))
    freeHeap = float(str(msg,'utf-8'))
    print("free heap size = {} bytes".format(freeHeap))

sta_if = network.WLAN(network.STA_IF)
print(sta_if.active())
print(sta_if.ifconfig())

myMqttClient = b"micropython"

THINGSPEAK_URL = b"broker.shiftr.io"
THINGSPEAK_USER_ID = b'weatherSensors'
THINGSPEAK_MQTT_API_KEY = b'bme280Sensors'
client = MQTTClient(client_id=myMqttClient,
                    server=THINGSPEAK_URL,
                    user=THINGSPEAK_USER_ID,
                    password=THINGSPEAK_MQTT_API_KEY,
                    ssl=False)
client.set_callback(cb)

try:
    client.connect()
    print("connection ok");    
    client.subscribe("/sensors/temperature")
except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
    sys.exit()

bus = OneWire(Pin(12))
ds = DS18X20(bus)

# Scanner tous les périphériques sur le bus
# Chaque périphérique à une adresse spécifique
roms = ds.scan()
for rom in roms:
   print( rom )

PUBLISH_PERIOD_IN_SEC = 30

while True:
    try:
        ds.convert_temp()
        # attendre OBLIGATOIREMENT 750ms
        sleep_ms( 750 )        
        for rom in roms:
            temp_celsius = ds.read_temp(rom)
            print( "Temp: %s" % temp_celsius )
        client.publish("/sensors/temperature", str(temp_celsius))
        print("publish ok");
        client.wait_msg()
        print("wait next publish");
        time.sleep(PUBLISH_PERIOD_IN_SEC)
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        client.disconnect()
        sys.exit()

print("exit")
