from machine import UART
import machine, neopixel
import time
from machine import Pin
from machine import WDT

import random
import json
import urequests as requests
from secrets import secrets



#Watch Dog time out after 30 seconds
wdt = WDT(timeout=300000) 

p0 = Pin(8, mode=Pin.OUT , pull = Pin.PULL_UP,value=1)
print("Set device to AT mode incase in sleep mode\r\n")
p0.off()
time.sleep(0.1)

print("Exit AT mode\r\n")
p0.on()
time.sleep(0.1)

# setup
np = neopixel.NeoPixel(machine.Pin(2), 1)

uart = UART(1, baudrate=9600, tx=6, rx=7)
uart.init(9600, bits=8, parity=None, stop=1)
    
uart.any()
uart.read()




def updateODOO(data):
  HOST = secrets['odoo_host']
  DB   = secrets['odoo_db']
  USER = secrets['odoo_user']
  PASS = secrets['odoo_password']
 
 
  def json_rpc(url, method, params):
      data = {
          "jsonrpc": "2.0",
          "method": method,
          "params": params,
          "id": random.randint(0, 1000000000),
      }
 
      req = requests.post(url=url, data=json.dumps(data).encode(), headers={"Content-Type":"application/json"})
      reply = req.json()
      if reply.get("error"):
          raise Exception(reply["error"])
      return reply["result"]
 
  def call(url, service, method, *args):
      return json_rpc(url, "call", {"service": service, "method": method, "args": args})
 
  url = "https://%s/jsonrpc" % (HOST)
  uid = call(url, "common", "login", DB, USER, PASS)
 
  #rpc_version =  call(url,"common","version")
  #print(rpc_version)
 
  # create a new note
  note_id = call(url, "object", "execute", DB, uid, PASS, 'iot.event', 'create', data)
  print(note_id)

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(secrets['ssid'], secrets['ssid_password'])
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


do_connect()





print("Starting serial reader")
while True:
    if uart.any():
        np[0] = (0, 1, 0) 
        np.write()
        time.sleep(0.1)        

        #updateODOO()
        updateODOO({
              'device_id':1,
              'data':str(uart.read())
          })
       
        np[0] = (0, 0, 0) 
        np.write()
    wdt.feed()
