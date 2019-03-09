def r_dispos(filename, args, index):
    #REMEMBER- when appending new labels to the end of a file, be sure to update the first 4 bytes in the file header with the new file length.
    import csv
    import binascii
    import os
    import struct
    import io

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

    def appendtoend(rfile, label):
        with open(rfile, 'ab+') as l:
            l.seek(0,2)
            length = len(label.encode("utf8")) + 1
            l.write(bytes(label, "ascii") + b'\x00')
            l.seek(0,2)
            return l.tell() - length

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
    with open(filename, "rb+") as binary_file:
        #Go to beginning of file, header info
        binary_file.seek(0, 0)
        filesize = binary_file.read(4)
        d = binary_file.read(4)
        p1 = binary_file.read(4)
        p2 = binary_file.read(4)

        #convert to actual ints lmao
        filesize = struct.unpack(">i", filesize)[0]
        d = struct.unpack(">i", d)[0]
        p1 = struct.unpack(">i", p1)[0]
        p2 = struct.unpack(">i", p2)[0]

        #offset stuff
        p_dataregion = 32
        p_pr1 = d + p_dataregion
        p_pr2 = p_pr1 + (p1 * 4)
        p_endregion = p_pr2 + (p2 * 8)

        #grab file sections
        binary_file.seek(0, 0)
        header = binary_file.read(32)
        dataregion = binary_file.read(d)
        pointer_1 = binary_file.read(p1 * 4)
        pointer_2 = binary_file.read(p2 * 8) #contains pointers to faction blocks
        endregion = binary_file.read(filesize - p_endregion)

        #---------------
        # first four bytes of the faction block seem to be # of units and total number of units and then two other bytes
        factionr = io.BytesIO(pointer_2)
        for i in range(p2):
            addr = factionr.read(8)
            #jump to faction block start
            addr = struct.unpack(">i",addr[:4])[0]
            if addr != 0:
                binary_file.seek(addr + 32)
                fct_header = binary_file.read(4)
                num = fct_header[0]
                #--------------------
                for i in range(num):
                    mapblock = binary_file.read(104)
                    #print("\n" + format(mapblock))
                    charid = format(mapblock[4:8])
                    string = readuntilnull(filename, toaddress(charid))
                    print(string)

                    charext = False
                    classstr = b''
                    newjob = ""
                    for char in index:
                        if string == char[0]:
                            newjob = char[1]
                            newadd = appendtoend(filename, char[1]) - 32
                            classstr = struct.pack(">l",newadd)
                            print(classstr)
                            charext = True

                    if charext:
                        #write class
                        binary_file.seek(binary_file.tell()-104,0)
                        binary_file.read(8)
                        binary_file.write(classstr) #count as indexing 4 bytes, remember

                        #jump back
                        binary_file.seek(92,1)
                        #OKAY FINALLY
                        print(newjob)
                    else:
                        classid = format(mapblock[8:12])
                        print(readuntilnull(filename, toaddress(classid)))

                    #Weapons
                    wep1 = format(mapblock[36:40])
                    print(readuntilnull(filename, toaddress(wep1)))
                    wep2 = format(mapblock[40:44])
                    print(readuntilnull(filename, toaddress(wep2)))
                    wep3 = format(mapblock[44:48])
                    print(readuntilnull(filename, toaddress(wep3)))
                    wep4 = format(mapblock[48:52])
                    print(readuntilnull(filename, toaddress(wep4)))

                    #Items
                    wep1 = format(mapblock[52:56])
                    print(readuntilnull(filename, toaddress(wep1)))
                    wep2 = format(mapblock[56:60])
                    print(readuntilnull(filename, toaddress(wep2)))
                    wep3 = format(mapblock[60:64])
                    print(readuntilnull(filename, toaddress(wep3)))
                    wep4 = format(mapblock[68:72])
                    print(readuntilnull(filename, toaddress(wep4)))
        #write new filesize to file
        filesize = os.path.getsize(filename)

        binary_file.seek(0,0)
        binary_file.write(struct.pack(">l",filesize))
