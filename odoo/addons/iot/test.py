data = 'b''\x01\x02\x01\x05\x0b21.6C,62.0%\xc2\xae\x04'''
print(type(data))

data = data.encode('utf-8')
print(type(data))

# def decode()
# print(data.decode('UTF-8'))
# print(data[0])
# print(data[1])
# print(data[2])
# print(data[3])
# print(data[4])

def decode_message(message):
    result = {
        'from_adr' : ord(message[1]),
        'to_adr' : ord(message[2]),
        'function' : ord(message[3]),
        'size' : ord(message[4]),
        'body' : message[5:5+ord(message[4])],
        'crc' : ord(message[5+ord(message[4])]),
        
        }
    return result

def compute_crc8_atm(datagram, initial_value=0):
    crc = initial_value
    # Iterate bytes in data
    for byte in datagram:
        # Iterate bits in byte
        for _ in range(0, 8):
            if (crc >> 7) ^ (byte & 0x01):
                crc = ((crc << 1) ^ 0x07) & 0xFF
            else:
                crc = (crc << 1) & 0xFF
            # Shift to next bit
            byte = byte >> 1
    return crc


print(data)

decoded = decode_message(data.decode('UTF-8'))
print(decoded)
