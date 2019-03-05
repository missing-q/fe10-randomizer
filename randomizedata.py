def randomizedata(file, seed):

    #here we go boys
    import csv
    from itertools import repeat
    import binascii
    import random
    import io

    #autogenned class tiers
    first_tier = ['JID_BLADE', 'JID_SOLDIER', 'JID_FIGHTER', 'JID_ARCHER', 'JID_LANCEARMOR', 'JID_AXARMOR', 'JID_SWORDARMOR', 'JID_SWORDARMOR_F', 'JID_THIEF', 'JID_BANDIT', 'JID_FIREMAGE', 'JID_THUNDERMAGE', 'JID_THUNDERMAGE_F', 'JID_WINDMAGE', 'JID_LIGHTMAGE', 'JID_PRIEST', 'JID_PRIEST_F', 'JID_SWORDKNIGHT', 'JID_LANCEKNIGHT', 'JID_LANCEKNIGHT_F', 'JID_AXEKNIGHT', 'JID_BOWKNIGHT', 'JID_PEGASUSKNIGHT', 'JID_DRAGONKNIGHT', 'JID_DRAGONKNIGHT_F', 'JID_BEASTTRIBE_L', 'JID_LION', 'JID_KINGLION_GI','JID_LION_GI', 'JID_KINGLION', 'JID_LION_CA', 'JID_BEASTTRIBE_T', 'JID_TIGER', 'JID_BEASTTRIBE_C', 'JID_CAT', 'JID_BEASTTRIBE_C/F', 'JID_CAT_F', 'JID_BEASTTRIBE_W', 'JID_WOLF', 'JID_QUEENWOLF', 'JID_WOLF_F', 'JID_BIRDTRIBE_H', 'JID_HAWK', 'JID_KINGHAWK', 'JID_HAWK_TI', 'JID_BIRDTRIBE_C', 'JID_CROW', 'JID_BIRDTRIBE_C/F', 'JID_CROW_F', 'JID_KINGCROW', 'JID_CROW_NA', 'JID_PRINCEEGRET', 'JID_EGRET', 'JID_PRINCEEGRET_RA', 'JID_EGRET_RA', 'JID_PRINCESSEGRET', 'JID_EGRET_LE', 'JID_DRAGONTRIBE_R', 'JID_REDDRAGON', 'JID_DRAGONTRIBE_R/F', 'JID_REDDRAGON_F', 'JID_DRAGONTRIBE_W', 'JID_WHITEDRAGON', 'JID_DRAGONKING', 'JID_BLACKDRAGON', 'JID_DRAGONPRINCE', 'JID_BLACKDRAGON_KU', 'JID_PILGRIM', 'JID_VENDOR_GOODS', 'JID_OLDMAN', 'JID_CITIZEN', 'JID_CITIZEN_F', 'JID_CHILD', 'JID_CHILD_F', 'JID_HORSE']

    second_tier = ['JID_BRAVE', 'JID_SWORDMASTER', 'JID_SWORDMASTER_F', 'JID_HALBERDIER', 'JID_HALBERDIER_F', 'JID_WARRIOR', 'JID_SNIPER', 'JID_GLORYDUX', 'JID_GREATDUX', 'JID_BLADEDUX', 'JID_BLADEDUX_F', 'JID_ROGUE', 'JID_ROGUE_F', 'JID_FIRESAGE', 'JID_FIRESAGE_F', 'JID_THUNDERSAGE', 'JID_THUNDERSAGE_F', 'JID_WINDSAGE', 'JID_LIGHTSAGE', 'JID_DARKSAGE', 'JID_DRUID', 'JID_BISHOP', 'JID_BISHOP_F', 'JID_CLERIC', 'JID_BLADEKNIGHT', 'JID_GLORYKNIGHT', 'JID_GLORYKNIGHT_F', 'JID_GREATKNIGHT', 'JID_GREATKNIGHT_F', 'JID_ARROWKNIGHT', 'JID_ARROWKNIGHT_F', 'JID_FALCONKNIGHT', 'JID_DRAGONMASTER', 'JID_DRAGONMASTER_F']

    third_tier = ['JID_VANGUARD', 'JID_SWORDMASTER_SP', 'JID_SWORDESCHATOS', 'JID_SWORDESCHATOS_F', 'JID_HALBERDIER_SP', 'JID_HOLYLANCER', 'JID_HOLYLANCER_F', 'JID_WARRIOR_SP', 'JID_AXBRAVE', 'JID_SNIPER_SP', 'JID_SAGITTARY', 'JID_GLORYDUX_SP', 'JID_GREATDUX_SP', 'JID_BLADEDUX_SP', 'JID_MARSHAL_L', 'JID_MARSHAL_A', 'JID_MARSHAL_S/F', 'JID_MARSHAL_Z', 'JID_DARKKNIGHT', 'JID_ESPION', 'JID_ESPION_F', 'JID_ASSASSIN', 'JID_FIRESAGE_SP', 'JID_THUNDERSAGE_SP', 'JID_WINDSAGE_SP', 'JID_ARCHSAGE_F', 'JID_ARCHSAGE_F/F', 'JID_ARCHSAGE_T', 'JID_ARCHSAGE_T/F', 'JID_ARCHSAGE_W', 'JID_SHAMAN', 'JID_CAESER', 'JID_CHANCELLOR', 'JID_DRUID_SP', 'JID_SUMMONER', 'JID_BISHOP_SP', 'JID_SAINT', 'JID_SAINT_F', 'JID_SAINT_SP', 'JID_VALKYRIA', 'JID_BLADEKNIGHT_SP', 'JID_GLORYKNIGHT_SP', 'JID_GREATKNIGHT_SP', 'JID_ARROWKNIGHT_SP', 'JID_GOLDKNIGHT_S', 'JID_GOLDKNIGHT_A', 'JID_GOLDKNIGHT_A/F', 'JID_SILVERKNIGHT_L', 'JID_SILVERKNIGHT_L/F', 'JID_SILVERKNIGHT_B', 'JID_FALCONKNIGHT_SP', 'JID_ENLILKNIGHT', 'JID_QUEEN', 'JID_DRAGONMASTER_SP', 'JID_RLINDWURM', 'JID_RLINDWURM_F', 'JID_SPIRIT_F', 'JID_SPIRIT_S', 'JID_SPIRIT_W', 'JID_GODDESS_AURA', 'JID_GODDESS', 'JID_DEBUG']

    banned_classes = ['JID_LION', 'JID_LION_GI', 'JID_LION_CA', 'JID_TIGER', 'JID_CAT', 'JID_CAT_F', 'JID_WOLF', 'JID_WOLF_F', 'JID_HAWK', 'JID_HAWK_TI', 'JID_CROW', 'JID_CROW_F', 'JID_CROW_NA', 'JID_EGRET', 'JID_EGRET_RA', 'JID_EGRET_LE', 'JID_REDDRAGON', 'JID_REDDRAGON_F', 'JID_WHITEDRAGON', 'JID_BLACKDRAGON', 'JID_BLACKDRAGON_KU', 'JID_SPIRIT_F', 'JID_SPIRIT_S', 'JID_SPIRIT_W', 'JID_GODDESS_AURA', 'JID_GODDESS']

    #format output funct
    def format(bytestring):
        hex = str(binascii.hexlify(bytestring), 'ascii')
        formatted_hex = ' '.join(hex[i:i+2] for i in range(0, len(hex), 2))
        formatted_hex = formatted_hex.upper()
        return(formatted_hex)

    #read in PIDs list
    with open('Assets/PIDS.csv', 'r') as f:
        reader = csv.reader(f)
        PIDS = list(reader)

    #import in JIDS list
    with open('Assets/JIDS.csv', 'r') as f:
        reader = csv.reader(f)
        JIDS = list(reader)

    random.seed(seed)
    #PID row layout:
        #row[0] = PID_LABEL, to be printed out with the rest of the block information
        #row[1] = Charblock starting address
        #row[2] = Label address, likely no program functionality
        #row[3] = Calculated pointer, likely no program functionality
        #row[4] = Hex string, deliminates beginning of charblock
        #row[5] = Block length, read this many bytes from the beginning of the block

    #IT'S TIME
    with open(file + "/FE10Data.cms.decompressed", "rb") as binary_file:
        #Go to beginning of file
        binary_file.seek(0, 0)
        for b in PIDS:
            #Grab charblock
            index = int(b[1], 16)
            #print(index)
            binary_file.seek(index,0)

            length = int(b[5], 16)

            print("\n" + b[0])

            charblock = io.BytesIO(binary_file.read(length))
            charblock.read(16)
            job = random.choice(PIDS)

            for i in banned_classes:
                while job[0] == i:
                    job = random.choice(PIDS)

            print(job)

            #print(job)


            print("\nGROWTHS")
            print("-------------------")
            growths = bytearray(charblock[length-13:length-5])
            for i in growths:
                if i > 127:
                    print(i-256)
                else:
                    print(i)

            print("\nSTATS")
            print("-------------------")
            stats = bytearray(charblock[length-23:length-13])
            for i in stats:
                if i > 127:
                    print(i-256)
                else:
                    print(i)

            #print(format(charblock))
