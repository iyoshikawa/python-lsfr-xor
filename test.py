import os
import sys
import re

data = "apple"
initialValue = 0x12345678
numBits = initialValue.bit_length()
regex = re.compile('[@_!#$%^&*()<>?/\\|}{~:]')

# Read the  and check if the string is "normal" or is "xor"
if(regex.search(data) == None):
    # converting the string to the bytes and iterate through to each character to get the acutal number.
    data = bytes(data, encoding='utf-8')
    for char in data:
        print(char)
    data = char << 8
    print(data)
    # data = (data << 0)

    # LFSR the  with the amount of steps that we want to use
    #result = data ^ numBits 
    #if result != -1:
    #    result ^= initialValue # XOR variable = x ^ x
    print(data) 
    #print(result)

# Here we are converting the XOR  into a string
elif(regex.search() == True):
    # Here we are using the xor  to convert to a normal string
    # todo need to take identify the xor  and convert it back into a string
    data = (data << 0) ^ initialValue
    result = data ^ numBits
    print(data) 
    print(result)


