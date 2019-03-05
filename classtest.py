#okay, this one is for classes this time
import csv
from itertools import repeat
import binascii

#format output funct
def format(bytestring):
    hexstring = binascii.hexlify(bytestring).decode('ascii')
    escapecodes = map(''.join, zip(repeat(r' '), *[iter(hexstring)]*2))
    print("'", *escapecodes, "'", sep='')

#read in JIDs list
with open('Assets/JIDS.csv', 'r') as f:
  reader = csv.reader(f)
  JIDS = list(reader)

#Weapon ranks list
#JID row layout:
    #row[0] = JID_LABEL, to be printed out with the rest of the block information
    #row[1] = Classblock starting address
    #row[2] = Label address, likely no program functionality
    #row[3] = Calculated pointer, likely no program functionality
    #row[4] = Hex string, deliminates beginning of charblock
    #row[5] = Block length, read this many bytes from the beginning of the block
    #row[6] = Class tier, determines how bytes are read/grouped

#okay, it's time y'allmst
with open("Test-Files/FE10Data.cms.decompressed", "rb") as binary_file:
    '''
    #Go to beginning of file
    binary_file.seek(0, 0)

    #Grab classblock
    index = int(JIDS[0][1], 16)
    #print(index)
    binary_file.seek(index,0)

    length = int(JIDS[0][5], 16)
    charblock = binary_file.read(length)
    print(format(charblock))

    growths = bytearray(charblock[length-24:length-16])
    for i in growths:
        print(i)
    '''
    first_tier = []
    second_tier = []
    third_tier = []

    banned_classes = []
    for b in JIDS:
        #Grab classblock
        index = int(b[1], 16)
        #print(index)
        binary_file.seek(index,0)

        length = int(b[5], 16)
        charblock = binary_file.read(length)

        #grab class data
        print("\n" + b[0])

        print("\nCAPS")
        print("-------------------")
        stats = bytearray(charblock[length-32:length-24])
        for i in stats:
            print(i)
        #print(format(charblock))

        print("\nSTATS")
        print("-------------------")
        stats = bytearray(charblock[length-24:length-16])
        for i in stats:
            print(i)
        #print(format(charblock))

        print("\nGROWTHS")
        print("-------------------")
        growths = bytearray(charblock[length-16:length-8])
        for i in growths:
            print(i)

        if charblock.find(b'\x00\x03\x37\x83') != -1:
            print("3rd tier")
            third_tier.append(b[0])
        elif charblock.find(b'\x00\x03\x37\x78') != -1:
            print("2nd tier")
            second_tier.append(b[0])
        else:
            print("1st tier")
            first_tier.append(b[0])

        if charblock.find(b'\x00\x03\x38\x36') != -1:
            print("Transformed class")
            banned_classes.append(b[0])
            
    print(banned_classes)
