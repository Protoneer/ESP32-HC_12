import machine, neopixel , time
from machine import UART,ADC,Pin

## LED
np = neopixel.NeoPixel(machine.Pin(2), 1)
np[0] = (0, 5, 0) 
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


np[0] = (0, 0, 0) 
np.write()
time.sleep(1)






p5 = Pin(5,Pin.IN)
adc = ADC(p5,atten=ADC.ATTN_11DB)




## avg the reading
#calibration = 0.0054245
#values = [0,0,0,0,0,0,0,0,0,0]
#while True:
#    np[0] = (50, 0, 0) 
#    np.write()

#    values.pop(0)
#    values.append(adc.read())
#    #print(sum(values)/len(values))
#    voltage = sum(values)/len(values) * calibration
#    voltage = round(voltage , 2)
#    print(str(voltage) + 'V : ' + str(adc.read())) 
#    #machine.deepsleep(500)
    
#    #transmit
#    uart.write(str(voltage) + 'V : ' + str(adc.read()))
    
#    np[0] = (0, 0, 0) 
#   np.write()

    
#    time.sleep(60)

calibration = 0.0054245
adc_value = adc.read()
voltage = round(adc_value * calibration , 2)
print(str(voltage) + 'V : ' + str(adc_value) )  
uart.write(str(voltage) + 'V : ' + str(adc_value) )


machine.deepsleep(60000)
