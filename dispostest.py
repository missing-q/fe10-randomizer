#REMEMBER- when appending new labels to the end of a file, be sure to update the first 4 bytes in the file header with the new file length.
import csv
from itertools import repeat
import binascii
import os
import struct

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
def readuntilnull(rfile, addr):
    with open(rfile, 'rb') as l:
        l.seek(addr,0)
        s = l.read()
        index = int(s.find(b'\x00'))
        return s[0:index].decode("ascii")

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
    #Go to beginning of file, header info
    binary_file.seek(0, 0)
    filesize = binary_file.read(4)
    data_rsize = binary_file.read(4)
    p1 = binary_file.read(4)
    p2 = binary_file.read(4)

    #convert to actual ints lmao
    filesize = struct.unpack(">i", filesize)[0]
    data_rsize = struct.unpack(">i", data_rsize)[0]
    p1 = struct.unpack(">i", p1)[0]
    p2 = struct.unpack(">i", p2)[0]

    #offset stuff
    dataregion = int("0x20",16)
    pr1 = data_rsize + dataregion
    pr2 = pr1 + (p1 * 4)
    endregion = pr2 + (p2 * 8)

    print(pr1)
    print(pr2)
    print(endregion)

    #---------------
    index = int("0x28", 16) # character data starts around 0x28, I believe, & takes up 104 bytes
    binary_file.seek(index)
    length = 104
    for i in range(5):
        mapblock = binary_file.read(length)
        print(format(mapblock))
        charid = format(mapblock[4:8])
        print(charid)
        print(toaddress(charid))
        if (toaddress(charid) < os.path.getsize("Test-Files/zmap/bmap0101/dispos_n.bin")):
            string = readuntilnull("Test-Files/zmap/bmap0101/dispos_n.bin", toaddress(charid))
            print(string)
