#VERY DANGEROUS STUFF
import csv
import binascii
import os
import struct
import io
import randomizedispos
import randomizedata
import genhtml

diff = ["c", "h", "n"]
def randomizer(path, seed, args):
    character_index = randomizedata.randomizedata(path, seed, args)

    #randomize part 1
    for i in range(1,12):
        for d in diff:
            randomizedispos.r_dispos(path + "/zmap/bmap01" + str(i).zfill(2) + "/dispos_" + d + ".bin", args, character_index)
    #randomize part 2???
    for i in range(1,6):
        for d in diff:
            randomizedispos.r_dispos(path + "/zmap/bmap02" + str(i).zfill(2) + "/dispos_" + d + ".bin", args, character_index)

    #generate HTML table of character/class info
    if args["HTML"] == True:
        genhtml.gen(character_index)
