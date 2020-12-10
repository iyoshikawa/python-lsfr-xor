#!/usr/bin/python

# imports
import os
import sys
import re

def crpyt(data, initialValue): #  returns byte string
    """This is the main function that will take the data and parse it out.
    
    Note
    ----
        * The goal here is to take in a string and its place in memory and spit out
        the XOR data.
        * Depending on the type of data it will have to do the opposite.
    """

    # Find the bit length to use at the amount of time we are going to step through
    numBits = initialValue.bit_length()[1:]
    regex = re.compile('[@_!#$%^&*()<>?/\\|}{~:]')

    # Read the data and check if the string is "normal" or is "xor"
    if(regex.search(data) == None):
        # Here we are using the string to convert the data
        # into xor format
        data = (data << 0)

        # LFSR the data with the amount of steps that we want to use
        result = data ^ numBits 
        if result != -1:
            result ^= initialValue # XOR variable = x ^ x
        yield data
        print(result)

    # Here we are converting the XOR data into a string
    elif(regex.search(data) == True):
        # Here we are using the xor data to convert to a normal string
        # todo need to take identify the xor data and convert it back into a string
        data = (data >> 1) ^ initialValue
        result = data ^ numBits
        yield data
        print(result)

    return

data = "apple"
initialValue = 0x12345678
