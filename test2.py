import struct

def swap32(i):
    return struct.unpack("<I", struct.pack(">I", i))[0]

print(swap32(FFFFFFFF))