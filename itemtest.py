#items time
import csv
from itertools import repeat
import binascii
import sys

#format output funct
def format(bytestring):
    hexstring = binascii.hexlify(bytestring).decode('ascii')
    escapecodes = map(''.join, zip(repeat(r' '), *[iter(hexstring)]*2))
    print("'", *escapecodes, "'", sep='')

#read in IIDs list
with open('Assets/IIDS.csv', 'r') as f:
  reader = csv.reader(f)
  IIDS = list(reader)

#Weapon ranks list
#IID row layout:
    #row[0] = IID_LABEL, to be printed out with the rest of the block information
    #row[1] = Classblock starting address
    #row[2] = Label address, likely no program functionality
    #row[3] = Calculated pointer, likely no program functionality
    #row[4] = Hex string, deliminates beginning of charblock
    #row[5] = Block length, read this many bytes from the beginning of the block
    #row[6] = Class tier, determines how bytes are read/grouped

#okay, it's time y'allmst
with open("Test-Files/FE10Data.cms.decompressed", "rb") as binary_file:
    #Go to beginning of file
    binary_file.seek(0, 0)

    '''
    #Grab classblock
    index = int(IIDS[18][1], 16)
    #print(index)
    binary_file.seek(index,0)

    length = int(IIDS[18][5], 16)
    itemblock = binary_file.read(length)
    print(format(itemblock))

    '''
    for b in IIDS:
        #Grab classblock
        index = int(b[1], 16)
        #print(index)
        binary_file.seek(index,0)

        length = int(b[5], 16)
        itemblock = binary_file.read(length)

        #grab class data
        print("\n" + b[0])
        print("-----------------------")
        #Mt and stuff starts at byte 40 of the itemblock
        print("Mt: " + str(itemblock[40]))
        print("Hit: " + str(itemblock[41]))
        print("Crit: " + str(itemblock[42]))
        print("Wt: " + str(itemblock[43]))
        print("Uses: " + str(itemblock[44]))
        print("WEXP: " + str(itemblock[45]))
        print("Min: " + str(itemblock[46]))
        print("Max: " + str(itemblock[47]))
