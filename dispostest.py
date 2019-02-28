#REMEMBER- when appending new labels to the end of a file, be sure to update the first 4 bytes in the file header with the new file length.
import csv
from itertools import repeat
import binascii
import os

#format output funct
def format(bytestring):
    hex = str(binascii.hexlify(bytestring), 'ascii')
    formatted_hex = ' '.join(hex[i:i+2] for i in range(0, len(hex), 2))
    formatted_hex = formatted_hex.upper()
    return(formatted_hex)

#converts hex strings into an address the reader can check
def toaddress(str):
    val = int("0x" + str.replace(" ", ""),16) + 32 #adding offset nonsense
    return val

#reads until the next x00 byte, helpful for grabbing stuff from addresses
def readuntilnull(file, addr):
    with open(file,'rb') as label:
        label.seek(addr,0)
        byte = label.read(1)
        while byte != b"/x00":
            byte = f.read(1)
        return byte

#import in PIDS
with open('Assets/PIDS.csv', 'r') as f:
    reader = csv.reader(f)
    PIDS = list(reader)

 #import in JIDS
with open('Assets/JIDS.csv', 'r') as f:
     reader = csv.reader(f)
     JIDS = list(reader)

#IIDS
with open('Assets/IIDS.csv', 'r') as f:
  reader = csv.reader(f)
  IIDS = list(reader)

#here we go boys
with open("Test-Files/zmap/bmap0101/dispos_n.bin", "rb") as binary_file:
    #Go to beginning of file
    binary_file.seek(0, 0)
    index = int("0x28", 16) # character data starts around 0x28, I believe, & takes up 104 bytes
    binary_file.seek(index)
    length = 104
    for i in range(0,5):
        mapblock = binary_file.read(length)
        print(format(mapblock))
        charid = format(mapblock[4:8])
        print(charid)
        print(toaddress(charid))
        if (toaddress(charid) < os.path.getsize("Test-Files/zmap/bmap0101/dispos_n.bin")):
            string = readuntilnull("Test-Files/zmap/bmap0101/dispos_n.bin", toaddress(charid))
            print(string)
