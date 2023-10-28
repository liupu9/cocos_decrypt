import struct

def _hexToDecimal(data, offset):
    if offset <= 0:
        return 0
    return struct.unpack(">I", data[:offset])[0]
 
 
def LOBYTE(d):
    return d & 0xff
 
 
def _decodePng(data, magic, rounds):
    dthis = bytearray(data)
 
    v7 = [0] * 4
    a2 = struct.pack("<i", magic)
    v7[1] = a2[2]
    v7[3] = a2[0]
    v7[0] = v5 = magic >> 24
    v7[2] = a2[1]
 
    i = 0
    if rounds > 0:
        while 1:
            i += 1
            dthis[i-1] ^= v5
            if i == rounds:
                break
            v5 = LOBYTE(v7[i % 4])
    return dthis
 
 
def decodePng(data, size):
    v14 = _hexToDecimal(data[-4:], 4)
    v16 = _hexToDecimal(data[-8:], 4)
    if size >= v16:
        ret = _decodePng(data, v14 - 2048, v16)
        ret[-1] = 130
        ret[-2] = 96
        ret[-3] = 66
        ret[-4] = 174
        ret[-5] = 68
        ret[-6] = 78
        ret[-7] = 69
        ret[-8] = 73
    return ret