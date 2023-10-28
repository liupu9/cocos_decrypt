import struct
 
def _hexToDecimal(data, offset):
    if offset <= 0:
        return 0
    return struct.unpack(">I", data[:offset])[0]
 
 
def LOBYTE(d):
    return d & 0xff
 
 
def decodeLuaData(data, size):
    v4 = bytearray(data)
    v15 = [0] * 4
    if size > 8 and data[0] == ord('a') and data[1] == ord('b') and data[2] == ord('c') and data[3] == ord('d'):
        # print("find special exts")
        v6 = _hexToDecimal(data[4:], 4)
 
        v15[3] = v6
        v15[2] = (v6 - 2048) >> 8
        v10 = (v6 - 2048) >> 24
        v15[1] = (v6 - 2048) >> 16
        v15[0] = (v6 - 2048) >> 24
 
        if size > 8:
            i = 0
            while 1:
                v13 = v4[8 + i]
                v4[i] = v13 ^ v10
                i += 1
                if size <= i + 8:
                    break
                v10 = LOBYTE(v15[i & 3])
        size -= 8
 
        return v4[:-8]