try:
  import usocket as socket
except:
  import socket
  
try:
  import urequests as requests
except:
  import requests


import machine  
import utime
import network
from machine import Pin
from utime import sleep
import dht

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Redmi'
password = 'facil6789'

phone_number = '+573014292053'
api_key = '3108133'
message = '%C2%A1%C2%A1Alerta%21%21%20La%20temperatura%20ha%20subido%20a%20m%C3%A1s%20de%2030%C2%B0' #YOUR MESSAGE HERE (URL ENCODED)https://www.urlencoder.io/

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

#sensor = dht.DHT22(Pin(14))
sensor = dht.DHT11(Pin(14))
led = Pin(15, Pin.OUT)
led2 = Pin(2, Pin.OUT)