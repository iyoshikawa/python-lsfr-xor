import re
import sys
import os

# statically setting the variables
data = "apple"
initialValue = 0x87654321

def cipher(data, initialValue):
    # iterate through the data by character(char)
    for char in data:
        # We then want to set the first bit to one if it is one.
        rightShift = 1 & initialValue

        # shifting the initial value to the right and get the first byte
        initialValue >>= 1  
        if rightShift:
            initialValue ^= 0x95 # xor the data and assign that back to the variable to be stored
        yield char ^ initialValue

print(bytes(cipher(b'apple', 0x95)))
print(bytes(cipher(b'\xbe\x8a\r\xc7\xa5', 0x95)))
