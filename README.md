# fe10-randomizer
A WIP randomizer for the game Fire Emblem: Radiant Dawn for the Wii. FE10 Randomizer is currently **semifunctional** and randomizes your ROM up to the end of Part 1. I've only tested FE10-Randomizer on NTSC v1.01 ROMs of Radiant Dawn, and can't guarantee it'll work on any other region/version type.

## How to use fe10-randomizer
*Requirements: Python 3.6+, PyQt5. If you don't have PyQt5, you can easily install it from pip.*

1. Obtain an ISO of FE10. I'd recommend making a backup copy, just in case.
2. Extract the ISO to some folder on your computer. I recommend personally recommend using [WiBaFu](https://sourceforge.net/projects/wiibafu/) for all of the ISO management (unpacking/repacking) stuff you'll need to do, but you can also extract your ISO using other programs, such as Dolphin. Just to be safe, make a backup of this folder.
3. Open BatchLZ77, also in the provided Tools folder, and decrypt the **FE10Data.cms** file, found in the "DATA/files/" directory, from the ISO's root folder. This will save as **FE10Data.cms.decompressed** - leave it as is for now.
4. Now run FE10 Randomizer from the command line with `python main.py` from the root folder of the repository (depending on your Python installation, you may have to run `python3 main.py`. I've found this to be the case on several Linux distros by default). It should immediately bring up a folder selection menu; select the *folder* containing **FE10Data** ("DATA/files", from the ISO's root folder), and hit OK.
5. This will bring up the main screen of the randomizer! Enter in your parameters, including the randomization seed & % variance, then hit randomize and wait for the program to finish running. A notification will pop up once it's done.
6. Once it's randomized, do everything in reverse- reencrypt **FE10Data.cmp** with BatchLZ77 (it'll save as **FE10Data.cms.decompressed.recompressed**- make sure to rename it to **FE10Data.cms**, overwriting the old one), then repack your ISO with either WiBaFu's Transfer to Image function or inserting each file one at a time with WiiScrubber like a madman.
7. Have fun! If there are any bugs or you're having trouble somewhere in the process, just shoot me a message on [Discord](https://discord.gg/KJVZWtn) or open up an issue and I'll try to help as best as I can.

## Research Notes
During the process of making this randomizer, I've compiled several research notes on the internal structure of Radiant Dawn, including character block locations/lengths. They can be found [here](https://docs.google.com/spreadsheets/d/1SB0EZSW0u7tHKTgQv-fEJFDxgORcouMdmTTc9lZ0DHk/edit#gid=0).
The vast majority of the research done on Radiant Dawn, including the basis for my own research, can be found in [this Serenes Forest thread](https://serenesforest.net/forums/index.php?/topic/18280-fe10-radiant-dawn-hacking-notes/). Thanks to VincentASM and everyone else who has contributed to the research done on Radiant Dawn!
