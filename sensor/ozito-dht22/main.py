# 6 TX
# 7 RX
# 8 Radio set

# 9 DHT




import machine, neopixel , time
from machine import UART,ADC,Pin

# Run settings
on_start_print_radio_settings = False
deep_sleep_mode = False
transmit_interval = 30


# dht
import dht
d = dht.DHT22(machine.Pin(9))
time.sleep(2)
    
    

print("Start Serial")
radio_uart = UART(1, baudrate=9600, tx=6, rx=7)
radio_uart.init(9600, bits=8, parity=None, stop=1)
radio_uart.any()
radio_uart.read()

radio_set_pin = Pin(8, mode=Pin.OUT , pull = Pin.PULL_UP,value=1)

def radio_settings(set_pin, uart):
    result = "Get Radio Config: "
    
    set_pin.off()
    time.sleep(0.1)

    uart.write('AT+V\r')
    time.sleep(0.1)

    uart.write('AT+RX\r')
    time.sleep(0.2)
    
    result = radio_uart.read()
    
    set_pin.on()
    time.sleep(0.1)
    return result

def radio_sleep(set_pin, uart):
    result = "Set radio to sleep: "
    set_pin.off()
    time.sleep(0.1)

    uart.write('AT+SLEEP\r')
    time.sleep(0.1)

    result = radio_uart.read()
    time.sleep(0.1)

    set_pin.on()
    time.sleep(0.1)
    return result
    

def radio_wake(set_pin, uart):
    result = "Wakeup radio."
    set_pin.off()
    time.sleep(0.1)
    set_pin.on()
    time.sleep(0.1)
    return result



if on_start_print_radio_settings:
    print(radio_settings(radio_set_pin,radio_uart))

#print(radio_sleep(radio_set_pin,radio_uart))
#print(radio_wake(radio_set_pin,radio_uart))


# transmit mode
radio_set_pin.on()
time.sleep(0.1)







#p5 = Pin(5,Pin.IN)
#adc = ADC(p5,atten=ADC.ATTN_11DB)





def read_voltage():
    calibration = 0.0054245
    adc_value = adc.read()
    voltage = round(adc_value * calibration , 2)
    print(str(voltage) + 'V : ' + str(adc_value) )
    return str(voltage) + 'V : ' + str(adc_value)


toggle = True
led = Pin(15, mode=Pin.OUT ,value=1)

if deep_sleep_mode:
    print(radio_wake(radio_set_pin,radio_uart))
    
    radio_uart.write(read_voltage())
    time.sleep(0.5)

    print(radio_sleep(radio_set_pin,radio_uart))    
    machine.deepsleep(transmit_interval * 1000)
else:
    while True:
        print("Send")
        #radio_uart.write(read_voltage())
        
        d.measure()
        temp = d.temperature()
        humid = d.humidity()
        print(str(temp)+'C')
        print(str(humid)+'%')

        radio_uart.write(str(temp) + 'C,' + str(humid) + '%')
        time.sleep(transmit_interval)
        toggle = not toggle
        led.value(toggle)
        
