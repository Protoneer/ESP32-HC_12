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


def encode_message(data):    
    start = str(chr(1))
    size = len(data['body'])
    end = str(chr(4))

    result = start
    
    result = str(chr(data['from_adr']))
    result += str(chr(data['to_adr']))
    result += str(chr(data['function']))
    result += str(chr(size))
    result += data['body']
    
    crc = compute_crc8_atm(result.encode('ascii'))
    result = start + result + str(chr(crc)) + end
    
    
    
    return result

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
1=
