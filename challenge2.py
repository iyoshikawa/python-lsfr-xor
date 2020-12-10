# imports
import os
import sys


class Challenge():

    # Definitions
    def __init__(self, data, contents, file):
        self.data = data
        self.initialValue = contents
        self.file = file
        self.read_data()
        self.crpyt()
    
    def read_data(self):
        # Pass in the file that is needed to be read and read that file
        # example python3 challenge2.py [path/to/text/file]
        # allows for only one file read at a time, but prevents any errors if handling
        # more than one file
        with open(sys.argv[1], 'r') as f:
            self.initialValue = f.readlines()

    def crpyt(self): #  returns byte string
        result = self.data
        numBits = self.initialValue.bit_length() - 1

        while True:
            result = (result << 1)
            xor = result ^ numBits # XOR variable = x ^ x
            if xor != 0:
                result ^= self.initialValue
            yield result
            print(xor)


if __name__ == '__main__':
    pass          