import machine 
from time import sleep
import bme280       #importing BME280 library
 
i2c=machine.SoftI2C(sda=machine.Pin(21), scl=machine.Pin(22), freq=400000)    #initializing the I2C method 
 
 
while True:
  bme = bme280.BME280(i2c=i2c)          #BME280 object created
  print(bme.values)
  sleep(10)           #delay of 10s
