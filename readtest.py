#here we go boys
import csv
from itertools import repeat
import binascii

#format output funct
def format(bytestring):
    hexstring = binascii.hexlify(bytestring).decode('ascii')
    escapecodes = map(''.join, zip(repeat(r' '), *[iter(hexstring)]*2))
    print("'", *escapecodes, "'", sep='')

#read in PIDs list
with open('Assets/PIDS.csv', 'r') as f:
  reader = csv.reader(f)
  PIDS = list(reader)

#PID row layout:
    #row[0] = PID_LABEL, to be printed out with the rest of the block information
    #row[1] = Charblock starting address
    #row[2] = Label address, likely no program functionality
    #row[3] = Calculated pointer, likely no program functionality
    #row[4] = Hex string, deliminates beginning of charblock
    #row[5] = Block length, read this many bytes from the beginning of the block

#okay, it's time y'allmst
with open("Test-Files/FE10Data.cms.decompressed", "rb") as binary_file:
    #Go to beginning of file
    binary_file.seek(0, 0)
    #Grab charblock
    index = int(PIDS[1][1], 16)
    print(index)
    binary_file.seek(index,0)
    block = int(PIDS[1][5], 16)
    charblock = binary_file.read(block)

    #grab character data
    print(PIDS[1][0])
    growths = charblock.slice()

    print(format(charblock))
    #for b in PIDS:
