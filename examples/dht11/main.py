# refer to https://docs.micropython.org/en/latest/esp32/quickref.html#dht-driver

import dht
import machine

dht_sensor = dht.DHT11(machine.Pin(23))
dht_sensor.measure()
print("temperature:", dht_sensor.temperature())
print("humidity:", dht_sensor.humidity())
