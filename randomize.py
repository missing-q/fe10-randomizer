#VERY DANGEROUS STUFF
import csv
import binascii
import os
import struct
import io
import randomizedispos
import randomizedata

def randomizer(path, seed, args):
    character_index = randomizedata.randomizedata(args)
    randomizetest.r_dispos(path + "/zmap/bmap0101/dispos_n.bin", args, character_index)
    
    #walk through every dispos file in dir
    '''
    for subdir, dirs, files in os.walk(path):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file
            if filepath.endswith(".bin"):
                print(filepath)
                #randomizetest.r_dispos(filepath, args, character_index)

    '''
