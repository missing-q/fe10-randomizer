#here we go boys
import csv
from itertools import repeat
import binascii
from staticrand import beast_classes

#format output funct
def format(bytestring):
    hex = str(binascii.hexlify(bytestring), 'ascii')
    formatted_hex = ' '.join(hex[i:i+2] for i in range(0, len(hex), 2))
    formatted_hex = formatted_hex.upper()
    return(formatted_hex)

def sign_int(int):
    if int > 127:
        return int-256
    else:
        return int

#read in PIDs list
with open('Assets/PIDS.csv', 'r') as f:
    reader = csv.reader(f)
    PIDS = list(reader)

 #import in JIDS list
with open('Assets/JIDS.csv', 'r') as f:
     reader = csv.reader(f)
     JIDS = list(reader)

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
    for b in PIDS:
        #Grab charblock
        index = int(b[1], 16)
        #print(index)
        binary_file.seek(index,0)

        length = int(b[5], 16)
        charblock = binary_file.read(length)

        #grab character data
        print("\n" + b[0])
        job = format(charblock[16:20])
        #print(job)

        for j in JIDS:
            if job == j[4]:
                print("\nClass: " + j[0])
                break #just so it doesn't iterate over the entire JIDS file lol

        print("\nGROWTHS")
        print("-------------------")
        growths = bytearray(charblock[length-13:length-5])
        for i in growths:
            print(sign_int(i))

        print("\nSTATS")
        print("-------------------")
        stats = bytearray(charblock[length-23:length-13])
        for i in stats:
            print(sign_int(i))

        #transformation gauge nonsense
        un_turn = charblock[length-27]
        un_battle = charblock[length-26]
        tr_turn = charblock[length-25]
        tr_battle = charblock[length-24]

        print("\nTRANSFORMATION GAUGE")
        print("-------------------")
        print(format(charblock[length-27:length-23]))
        #print(format(charblock))
