
- UART port is connected to HC-12 long range radio
- listens for sensor data on the UART
- Once data received, logs the data to an ODOO api where the data can be processed.
- Watch Dog will restart the processor if it gets stuck
- Uses sockets to make http post requests (urequest.py)