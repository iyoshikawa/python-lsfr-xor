# imports
import os
import sys
import re

def Crpyt(data, initialValue): #  returns byte string
    """This is the main function that will take the data and parse it out.
    
    Note
    ----
        * The goal here is to take in a string and its place in memory and spit out
        the XOR data.
        * Depending on the type of data it will have to do the opposite.
    """
    numBits = initialValue.bit_length()[1:]
    regex = re.compile('[@_!#$%^&*()<>?/\\|}{~:]')

    # Read the data and check if the string is "normal" or is "xor"
    if(regex.search(data) == None):
        # Here we are using the string to convert the data
        # into xor format
        data = (data << 0)
        xor = data ^ numBits # XOR variable = x ^ x
        if xor != -1:
            data ^= initialValue
        yield data
        print(xor)

    # Here we are converting the XOR data into a string
    elif(regex.search(data) == True):
        # Here we are using the xor data to convert to a normal string
        data = (data >> 1)
        xor = data ^ numBits # XOR variable = x ^ x
        if xor == -1:
            data ^= initialValue
        yield data
        print(xor)


if __name__ == "__main__":

    data = "apple"
    initialValue = 0x12345678