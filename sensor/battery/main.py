import machine, neopixel
import time
from machine import UART
from machine import Pin


## LED
np = neopixel.NeoPixel(machine.Pin(2), 1)
np[0] = (0, 0, 0)  # set to blue, quarter brightness
np.write()



print("Start Serial")
uart = UART(1, baudrate=9600, tx=6, rx=7)
uart.init(9600, bits=8, parity=None, stop=1)
uart.any()
uart.read()

# Transmit mode
print("Transmit mode")
p0 = Pin(8, mode=Pin.OUT , pull = Pin.PULL_UP,value=1)
p0.on()
time.sleep(0.1)

np[0] = (0, 1, 0) 
np.write()
time.sleep(1)





from machine import ADC,Pin
import time
p5 = Pin(5,Pin.IN)
#p5 = Pin(5,Pin.IN,Pin.PULL_DOWN)
adc = ADC(p5,atten=ADC.ATTN_11DB)
#adc = ADC(p5)

# avg the reading
calibration = 0.0054245
values = [0,0,0,0,0,0,0,0,0,0]
while True:
    values.pop(0)
    values.append(adc.read())
    #print(sum(values)/len(values))
    voltage = sum(values)/len(values) * calibration
    voltage = round(voltage , 2)
    print(str(voltage) + 'V : ' + str(adc.read())) 
    #machine.deepsleep(500)
    
    #transmit
    uart.write(str(voltage) + 'V : ' + str(adc.read()))
    
    time.sleep(60)
