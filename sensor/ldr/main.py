from machine import ADC, Pin
import time
pin = Pin(34, Pin.IN)  

while True:
    adc = ADC(pin)        # create an ADC object acting on a pin
    print(adc.read())  # read a raw analog value in the range 0-65535
    time.sleep(0.1)

