#VERY DANGEROUS STUFF
import csv
import binascii
import os
import struct
import io
import randomizedispos
import randomizedata

diff = ["c", "h", "n"]
def randomizer(path, seed, args):
    character_index = randomizedata.randomizedata(path, seed, args)
    randomizedispos.r_dispos(path + "/zmap/bmap0101/dispos_n.bin", args, character_index)
    
    '''
    #randomize part 1
    for i in range(1,12):
        for d in diff:
            randomizedispos.r_dispos(path + "/zmap/bmap01" + str(i).zfill(2) + "/dispos_" + d + ".bin", args, character_index)
    '''

    #walk through every dispos file in dir
    '''
    for subdir, dirs, files in os.walk(path):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file
            if filepath.endswith(".bin"):
                print(filepath)
                #randomizedispos.r_dispos(filepath, args, character_index)

    '''
