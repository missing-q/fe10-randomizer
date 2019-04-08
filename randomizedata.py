def randomizedata(file, seed, args):

    #here we go boys
    import csv
    from itertools import repeat
    import binascii
    import random
    #python won't let you import all outside of the module level, so this is what you get
    from staticrand import first_tier, second_tier, third_tier, beast_classes, transformations, format, sign_int, parse_wepstring, toaddress, readuntilnull, appendtoend, wepslist, wep_binlist

    #read in PIDs list
    with open('Assets/PIDS.csv', 'r') as f:
        reader = csv.reader(f)
        PIDS = list(reader)

    #import in JIDS list
    with open('Assets/JIDS.csv', 'r') as f:
        reader = csv.reader(f)
        JIDS = list(reader)

    #import in IIDS list
    with open('Assets/IIDS.csv', 'r') as f:
        reader = csv.reader(f)
        IIDS = list(reader)

    #
    with open('Assets/SIDS.csv', 'r') as f:
         reader = csv.reader(f)
         SIDS = list(reader)

    with open('Assets/Weapons.csv', 'r') as f:
        reader = csv.reader(f)
        Weps = list(reader)

    random.seed(seed)
    print(args)
    var = int(args["Variance"]) / 100
    print(var)
    returnval = []
    #PID row layout:
        #row[0] = PID_LABEL, to be printed out with the rest of the block information
        #row[1] = Charblock starting address
        #row[2] = Label address, likely no program functionality
        #row[3] = Calculated pointer, likely no program functionality
        #row[4] = Hex string, deliminates beginning of charblock
        #row[5] = Block length, read this many bytes from the beginning of the block

    #okay, it's time y'allmst
    with open(file + "/FE10Data.cms.decompressed", "rb+") as binary_file:
        #CHARACTER STUFF
        #Go to beginning of file
        binary_file.seek(0, 0)
        print("CHARACTER RANDOMIZATIONS")
        print("##################################################")
        print("##################################################")
        for b in PIDS:
            #Grab charblock
            index = int(b[1], 16)
            #print(index)
            binary_file.seek(index,0)

            length = int(b[5], 16)
            charblock = binary_file.read(length)
            #grab character data
            print("\n" + b[0])
            job = charblock[16:20]
            newjob = ""
            #print(job)
            chararray = [b[0]]
            for j in JIDS:
                if format(job) == j[4]:
                    print("\nClass: " + j[0])

                    for q in first_tier:
                        if j[0] == q:
                            newjob = random.choice(first_tier)
                            print(newjob)
                            chararray.append(newjob)

                    for q in second_tier:
                        if j[0] == q:
                            newjob = random.choice(second_tier)
                            print(newjob)
                            chararray.append(newjob)

                    for q in third_tier:
                        if j[0] == q:
                            newjob = random.choice(third_tier)
                            print(newjob)
                            chararray.append(newjob)
                    break #just so it doesn't iterate over the entire JIDS file lol

            jobstr = b''
            #iterate over JIDS again just to get the proper address for newjob
            for j in JIDS:
                if j[0] == newjob:
                    jobstr = bytes.fromhex(j[4])
                    nindex = JIDS.index(j)
                    print(nindex)
                    print(Weps[nindex])
                    if Weps[nindex] == []:
                        chararray.append("")
                    else:
                        chararray.append(Weps[nindex][0])

            binary_file.seek(index + 16)
            binary_file.write(jobstr)

            print("\nGROWTHS")
            print("-------------------")
            growths = bytearray(charblock[length-13:length-5])
            gtemp = []
            for i in growths:
                mod = round(i * var) #grab percentage
                #print(mod)
                temp = i + random.randint(-1 * mod, mod)
                if temp < 0:
                    temp = 0
                if temp > 255:
                    temp = 0
                print(temp)
                gtemp.append(temp)
            print(gtemp)
            chararray.append(gtemp)
            binary_file.seek(index + (length-13), 0)
            binary_file.write(bytearray(gtemp))

            print("\nSTATS")
            print("-------------------")
            stats = bytearray(charblock[length-23:length-13])
            stemp = []
            for i in stats:
                mod = round(i * var) #grab percentage
                #print(mod)
                temp = i + random.randint(-1 * mod, mod)
                if temp < 0:
                    temp = 0
                if temp > 127:
                    temp = 0
                print(temp)
                stemp.append(temp)
            print(stemp)
            chararray.append(stemp)
            binary_file.seek(index + (length-23), 0)
            binary_file.write(bytearray(stemp))
            #print(format(charblock))

            #Transformation gauge stuff
            for i in beast_classes:
                if newjob == i:
                    tr_ind = beast_classes.index(newjob)
                    binary_file.seek(index + (length-27))
                    binary_file.write(transformations[tr_ind])
                    print("Character assigned proper transformation gauge")
            if not newjob in beast_classes:
                binary_file.seek(index + (length-27))
                binary_file.write(b'\x00\x00\x00\x00')

            returnval.append(chararray)

        #CLASS STUFF
        binary_file.seek(0, 0)
        print("CLASS RANDOMIZATIONS")
        print("##################################################")
        print("##################################################")
        #NICE
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
            caps = bytearray(charblock[length-32:length-24])
            ctemp = []
            for i in caps:
                mod = round(i * var) #grab percentage
                #print(mod)
                temp = i + random.randint(-1 * mod, mod)
                if temp < 0:
                    temp = 0
                if temp > 255:
                    temp = 255
                print(temp)
                ctemp.append(temp)
            binary_file.seek(index + (length-32), 0)
            binary_file.write(bytearray(ctemp))
            #print(format(charblock))

            print("\nSTATS")
            print("-------------------")
            stats = bytearray(charblock[length-24:length-16])
            stemp = []
            for i in stats:
                mod = round(i * var) #grab percentage
                #print(mod)
                temp = i + random.randint(-1 * mod, mod)
                if temp < 0:
                    temp = 0
                if temp > 255:
                    temp = 0
                print(temp)
                stemp.append(temp)
            print(stemp)
            binary_file.seek(index + (length-24), 0)
            binary_file.write(bytearray(stemp))
            #print(format(charblock))

            print("\nGROWTHS")
            print("-------------------")
            growths = bytearray(charblock[length-16:length-8])
            gtemp = []
            for i in growths:
                mod = round(i * var) #grab percentage
                #print(mod)
                temp = i + random.randint(-1 * mod, mod)
                if temp < 0:
                    temp = 0
                print(temp)
                gtemp.append(temp)
            print(gtemp)
            binary_file.seek(index + (length-16), 0)
            binary_file.write(bytearray(gtemp))

            #skills time bb
            #gonna do character skills for now, idk about class skills
            '''
            skillnum = int((length - 80)/4)
            binary_file.seek(index + 28)
            for i in range(skillnum):
                poin = i * 4
                ind_skill = skills[poin:poin+4]

                for q in SIDS:
                    if toaddress_n(format(ind_skill)) == int(q[3],16):
                        newskill = random.choice(list(SIDS))
            '''

        #Item stuff
        binary_file.seek(0, 0)
        print("WEAPON RANDOMIZATIONS")
        print("##################################################")
        print("##################################################")

        wepdelimiter = False #i'm iterating over the actual objects so this is what i get
        if args["Stats"] == True:
            for b in IIDS:
                #Grab classblock
                index = int(b[1], 16)
                #print(index)
                binary_file.seek(index,0)

                length = int(b[5], 16)
                itemblock = binary_file.read(length)

                #grab item data
                print("\n" + b[0])
                print("-----------------------")
                #Mt and stuff starts at byte 40 of the itemblock
                #mt, hit, crit, wt, uses, wexp, min range, max range
                stats = [int(itemblock[40]), int(itemblock[41]), int(itemblock[42]), int(itemblock[43]), int(itemblock[44]), int(itemblock[45]), int(itemblock[46]), int(itemblock[47])]
                temp = []
                #delimiter setter, I have no idea what this actually is but it's right before staves so
                if b[0] == "IID_SPRT_HEAL_SP":
                    wepdelimiter = True

                #randomizer time
                if wepdelimiter != True:
                    for i in stats:
                        mod = i + random.randint(-1 * round(i * var), round(i * var))
                        if mod <= 0:
                            mod = 1
                        if mod > 255: #somewhat more reasonably, weapon stats are unsigned
                            mod = 255
                        temp.append(mod)
                    stats = temp
                    if stats[6] > stats[7]:
                        stats[7] = stats[6]

                    print(stats)
                    binary_file.seek(index + 40)
                    binary_file.write(bytearray(stats))

        #WTA stuff
        binary_file.seek(0, 0)
        print("WTA RANDOMIZATIONS")
        print("##################################################")
        print("##################################################")
        if args['WTA'] == True:
            #why would you do this

            #WTA is laid out in the format first_type, second_type, mt+, hit+
            #                              [4 bytes, 4 bytes, 2 bytes, 2 bytes]
            binary_file.seek(160804, 0)
            mod = round(i * var)

            for i in range(13):
                index = i * 12

                binary_file.write(random.choice(wep_binlist)) #write first wep
                binary_file.write(random.choice(wep_binlist)) #write second
                mt_add = abs(sign_int(binary_file.read(2)) + random.randint(-1 * mod, mod))
                hit_add = abs(sign_int(binary_file.read(2)) + random.randint(-1 * mod, mod))

                binary_file.seek(160804 + index + 8, 0)
                binary_file.write(mt_add)
                binary_file.write(hit_add)



        #Misc: Zero out all instances of "EVENT-CC"
        binary_file.seek(0,0)
        if args["Lords"] == True:
            binary_file.seek(37552, 0)
            binary_file.write(b'\x00\x00\x00\x00')

            binary_file.seek(41964, 0)
            binary_file.write(b'\x00\x00\x00\x00')

            binary_file.seek(43108, 0)
            binary_file.write(b'\x00\x00\x00\x00')

            binary_file.seek(43808, 0)
            binary_file.write(b'\x00\x00\x00\x00')

            binary_file.seek(57108, 0)
            binary_file.write(b'\x00\x00\x00\x00')


    #return character array for use in dispos
    return returnval
