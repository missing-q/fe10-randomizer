#Exists solely for static variables (such as class lists) from the randomizer modules to import
#autogenned class tiers
import binascii

first_tier = ['JID_BLADE', 'JID_SOLDIER', 'JID_FIGHTER', 'JID_ARCHER', 'JID_LANCEARMOR', 'JID_AXARMOR', 'JID_SWORDARMOR', 'JID_SWORDARMOR_F', 'JID_THIEF', 'JID_BANDIT', 'JID_FIREMAGE', 'JID_THUNDERMAGE', 'JID_THUNDERMAGE_F', 'JID_WINDMAGE', 'JID_LIGHTMAGE', 'JID_PRIEST', 'JID_PRIEST_F', 'JID_SWORDKNIGHT', 'JID_LANCEKNIGHT', 'JID_LANCEKNIGHT_F', 'JID_AXEKNIGHT', 'JID_BOWKNIGHT', 'JID_PEGASUSKNIGHT', 'JID_DRAGONKNIGHT', 'JID_DRAGONKNIGHT_F', 'JID_BEASTTRIBE_L', 'JID_KINGLION_GI', 'JID_KINGLION', 'JID_BEASTTRIBE_T', 'JID_BEASTTRIBE_C', 'JID_BEASTTRIBE_C/F', 'JID_BEASTTRIBE_W', 'JID_BIRDTRIBE_H', 'JID_BIRDTRIBE_C', 'JID_BIRDTRIBE_C/F', 'JID_PRINCEEGRET', 'JID_PRINCEEGRET_RA', 'JID_PRINCESSEGRET', 'JID_DRAGONTRIBE_R', 'JID_DRAGONTRIBE_R/F', 'JID_DRAGONTRIBE_W', 'JID_PILGRIM', 'JID_VENDOR_GOODS', 'JID_OLDMAN', 'JID_CITIZEN', 'JID_CITIZEN_F', 'JID_CHILD', 'JID_CHILD_F', 'JID_HORSE']

second_tier = ['JID_BRAVE', 'JID_SWORDMASTER', 'JID_SWORDMASTER_F', 'JID_HALBERDIER', 'JID_HALBERDIER_F', 'JID_WARRIOR', 'JID_SNIPER', 'JID_GLORYDUX', 'JID_GREATDUX', 'JID_BLADEDUX', 'JID_BLADEDUX_F', 'JID_ROGUE', 'JID_ROGUE_F', 'JID_FIRESAGE', 'JID_FIRESAGE_F', 'JID_THUNDERSAGE', 'JID_THUNDERSAGE_F', 'JID_WINDSAGE', 'JID_LIGHTSAGE', 'JID_DARKSAGE', 'JID_DRUID', 'JID_BISHOP', 'JID_BISHOP_F', 'JID_CLERIC', 'JID_BLADEKNIGHT', 'JID_GLORYKNIGHT', 'JID_GLORYKNIGHT_F', 'JID_GREATKNIGHT', 'JID_GREATKNIGHT_F', 'JID_ARROWKNIGHT', 'JID_ARROWKNIGHT_F', 'JID_FALCONKNIGHT', 'JID_DRAGONMASTER', 'JID_DRAGONMASTER_F', 'JID_QUEENWOLF', 'JID_KINGHAWK', 'JID_KINGCROW', 'JID_DRAGONKING', 'JID_DRAGONPRINCE']

third_tier = ['JID_VANGUARD', 'JID_SWORDMASTER_SP', 'JID_SWORDESCHATOS', 'JID_SWORDESCHATOS_F', 'JID_HALBERDIER_SP', 'JID_HOLYLANCER', 'JID_HOLYLANCER_F', 'JID_WARRIOR_SP', 'JID_AXBRAVE', 'JID_SNIPER_SP', 'JID_SAGITTARY', 'JID_GLORYDUX_SP', 'JID_GREATDUX_SP', 'JID_BLADEDUX_SP', 'JID_MARSHAL_L', 'JID_MARSHAL_A', 'JID_MARSHAL_S/F', 'JID_MARSHAL_Z', 'JID_DARKKNIGHT', 'JID_ESPION', 'JID_ESPION_F', 'JID_ASSASSIN', 'JID_FIRESAGE_SP', 'JID_THUNDERSAGE_SP', 'JID_WINDSAGE_SP', 'JID_ARCHSAGE_F', 'JID_ARCHSAGE_F/F', 'JID_ARCHSAGE_T', 'JID_ARCHSAGE_T/F', 'JID_ARCHSAGE_W', 'JID_SHAMAN', 'JID_CAESER', 'JID_CHANCELLOR', 'JID_DRUID_SP', 'JID_SUMMONER', 'JID_BISHOP_SP', 'JID_SAINT', 'JID_SAINT_F', 'JID_SAINT_SP', 'JID_VALKYRIA', 'JID_BLADEKNIGHT_SP', 'JID_GLORYKNIGHT_SP', 'JID_GREATKNIGHT_SP', 'JID_ARROWKNIGHT_SP', 'JID_GOLDKNIGHT_S', 'JID_GOLDKNIGHT_A', 'JID_GOLDKNIGHT_A/F', 'JID_SILVERKNIGHT_L', 'JID_SILVERKNIGHT_L/F', 'JID_SILVERKNIGHT_B', 'JID_FALCONKNIGHT_SP', 'JID_ENLILKNIGHT', 'JID_QUEEN', 'JID_DRAGONMASTER_SP', 'JID_RLINDWURM', 'JID_RLINDWURM_F', 'JID_DEBUG']

banned_classes = ['JID_LION', 'JID_LION_GI', 'JID_LION_CA', 'JID_TIGER', 'JID_CAT', 'JID_CAT_F', 'JID_WOLF', 'JID_WOLF_F', 'JID_HAWK', 'JID_HAWK_TI', 'JID_CROW', 'JID_CROW_F', 'JID_CROW_NA', 'JID_EGRET', 'JID_EGRET_RA', 'JID_EGRET_LE', 'JID_REDDRAGON', 'JID_REDDRAGON_F', 'JID_WHITEDRAGON', 'JID_BLACKDRAGON', 'JID_BLACKDRAGON_KU', 'JID_SPIRIT_F', 'JID_SPIRIT_S', 'JID_SPIRIT_W', 'JID_GODDESS_AURA', 'JID_GODDESS']

#beast classes & corresponding transformation values, converted to hex strings for my and everyone's sanity
beast_classes = ['JID_BEASTTRIBE_T','JID_BEASTTRIBE_C','JID_BEASTTRIBE_C/F', 'JID_BEASTTRIBE_W', 'JID_QUEENWOLF','JID_BIRDTRIBE_H', 'JID_KINGHAWK','JID_BIRDTRIBE_C','JID_BIRDTRIBE_C/F', 'JID_KINGCROW','JID_PRINCEEGRET','JID_PRINCEEGRET_RA','JID_PRINCESSEGRET','JID_DRAGONTRIBE_R','JID_DRAGONTRIBE_R/F','JID_DRAGONTRIBE_W','JID_DRAGONKING','JID_DRAGONPRINCE']
transformations = [b'\x08\x0F\xFC\xFD', b'\x0A\x0F\xFB\xFC', b'\x0A\x0F\xFB\xFC', b'\x06\x0A\xFC\xFD', b'\x06\x0A\xFC\xFD',b'\x08\x0F\xFC\xFD', b'\x08\x0F\xFC\xFD',b'\x06\x0A\xFC\xFD',b'\x06\x0A\xFC\xFD', b'\x06\x0A\xFC\xFD',b'\x04\x0A\xFB\xFA',b'\x03\x06\xFB\xF8',b'\x03\x08\xFB\xF8', b'\x05\x06\xFE\xFF', b'\x05\x06\xFE\xFF', b'\x04\x05\xFE\xFF', b'\x05\x06\xFE\xFF', b'\x05\x06\xFE\xFF']

#Because Radiant Dawn is whack with how it handles weapon ranks
def parse_wepstring(string):
    weplist = ["Sword", "Lance", "Axe" , "Bow", "Knife", "Strike", "Fire", "Thunder", "Wind", "Light", "Dark", "Staff"]
    temp = []
    if "IID" in string:
        return ["Strike D"]
    for i, c in enumerate(string):
        if c != "-":
            temp.append(weplist[i] + " " + c)
    return temp

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

#weapon lists are inclusive of all the weapons "below" it
wepslist = {
    'Sword E' : ["IID_DELICATESWORD", "IID_BRONZESWORD"],
    'Sword D' : ["IID_DELICATESWORD", "IID_BRONZESWORD", "IID_IRONSWORD", "IID_POISONSWORD", "IID_WINDSWORD"],
    'Sword C' : ["IID_DELICATESWORD", "IID_BRONZESWORD", "IID_IRONSWORD", "IID_POISONSWORD", "IID_WINDSWORD", "IID_BRAVESWORD", "IID_STEELSWORD", "IID_IRONBLADE"],
    'Sword B' : ["IID_DELICATESWORD", "IID_BRONZESWORD", "IID_IRONSWORD", "IID_POISONSWORD", "IID_WINDSWORD", "IID_BRAVESWORD", "IID_STEELSWORD", "IID_IRONBLADE", "IID_WATOU", "IID_KILLSWORD", "IID_DRAGONKILLER", "IID_STEELBLADE", "IID_STORMSWORD"],
    'Sword A' : ["IID_DELICATESWORD", "IID_BRONZESWORD", "IID_IRONSWORD", "IID_POISONSWORD", "IID_WINDSWORD", "IID_BRAVESWORD", "IID_STEELSWORD", "IID_IRONBLADE", "IID_WATOU", "IID_KILLSWORD", "IID_DRAGONKILLER", "IID_STEELBLADE", "IID_STORMSWORD", "IID_SILVERSWORD", "IID_SILVERBLADE"],
    'Sword S' : ["IID_DELICATESWORD", "IID_BRONZESWORD", "IID_IRONSWORD", "IID_POISONSWORD", "IID_WINDSWORD", "IID_BRAVESWORD", "IID_STEELSWORD", "IID_IRONBLADE", "IID_WATOU", "IID_KILLSWORD", "IID_DRAGONKILLER", "IID_STEELBLADE", "IID_STORMSWORD", "IID_SILVERSWORD", "IID_SILVERBLADE", "IID_ENLILSWORD"],
    'Sword *' : ["IID_DELICATESWORD", "IID_BRONZESWORD", "IID_IRONSWORD", "IID_POISONSWORD", "IID_WINDSWORD", "IID_BRAVESWORD", "IID_STEELSWORD", "IID_IRONBLADE", "IID_WATOU", "IID_KILLSWORD", "IID_DRAGONKILLER", "IID_STEELBLADE", "IID_STORMSWORD", "IID_SILVERSWORD", "IID_SILVERBLADE", "IID_ENLILSWORD", "IID_VAGUEKATTI", "IID_ETTARD"],
    'Lance E' : ["IID_DELICATELANCE", "IID_BRONZELANCE"],
}
