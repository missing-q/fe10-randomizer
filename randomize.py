#VERY DANGEROUS STUFF
import csv
import binascii
import os
import struct
import io
import randomizedispos

def randomizer(path):
    #walk through every dispos file in dir
    for subdir, dirs, files in os.walk(path):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file
            if filepath.endswith(".bin"):
                #print(filepath)
                #randomizetest.r_dispos(filepath)
