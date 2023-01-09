# ESP32-HC_12

## Folder Structure
- __reciever__ - Receives sensor data and log to Odoo database
- __sensor/*__ - Sensor Nodes that transmit data
- __odoo/addons/* - Odoo Addons that collects the data

## Hardware
- __M5 Stamp C3__ doco - https://docs.m5stack.com/en/core/stamp_c3
- __HC-12__ https://www.allaboutcircuits.com/projects/understanding-and-implementing-the-hc-12-wireless-transceiver-module/

## Wiring 
- ESP32 Pin 6 = radio rx
- ESP32 Pin 7 = radio tx
- ESP32 Pin 8 = Radio Set
- ESP32 Gnd = Radio GND
- ESP32 3V3 = Radio VCC


