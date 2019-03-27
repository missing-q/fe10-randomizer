#this reads the flags from an item and dumps them to output.
import csv
from itertools import repeat, groupby
import binascii
import sys
from staticrand import toaddress, format, readuntilnull_jis

#format output funct

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
    flaglist = []
    addrlist = []
    flaglist_n = []
    addrlist_n = []

    for b in IIDS:
        #Grab classblock
        index = int(b[1], 16)
        #print(index)
        binary_file.seek(index,0)

        length = int(b[5], 16)
        itemblock = binary_file.read(length)

        flagnum = int((length - 56)/4)
        flags = itemblock[length - (flagnum * 4):]

        print("\n---------------------------------------")

        for i in range(flagnum):

            poin = i * 4
            ind_flag = format(flags[poin:poin+4])

            if ind_flag[:5] == "00 03":
                flaglist.append(readuntilnull_jis("Test-Files/FE10Data.cms.decompressed", toaddress(ind_flag)))
                addrlist.append("0x" + ind_flag.replace(" ", ""))

                print(ind_flag)
            #newflag = toaddress_n(format(ind_flag))
for i in flaglist:
    if i not in flaglist_n:
        flaglist_n.append(i)

for i in addrlist:
    if i not in addrlist_n:
        addrlist_n.append(i)

print(flaglist_n)
print(addrlist_n)
