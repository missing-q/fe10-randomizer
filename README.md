# fe10-randomizer
A WIP randomizer for the game Fire Emblem: Radiant Dawn for the Wii. Warning- FE10 Randomizer is currently nonfunctional and will probably not either do anything or corrupt your ISO. I'll edit this description once it actually works.

## How to use fe10-randomizer
1. Obtain an ISO of FE10. I'd recommend making a backup copy, just in case.
2. Open up the ISO in WiiTool or WiiScrubber, in the provided Tools folder, then extract it to some directory on your computer.
3. Open BatchLZ77, also in the provided Tools folder, and decrypt the **FE10Data.bin** file in the extracted game. I'd reccomend making another backup of **FE10Data.bin** before decrypting it as well.
4. Now open **FE10Data.bin** in FE10 Randomizer! Wait a bit for the randomizer to apply your selected settings; a notification will pop up when it's done.
5. Once it's randomized, do everything in reverse- reencrypt **FE10Data.bin** with BatchLZ77, then repack your ISO with WiiTools/WiiScrubber.
6. Have fun! If there are any bugs or you're having trouble somewhere in the process, just shoot me a message on [Discord](https://discord.gg/KJVZWtn) and I'll try to help as best as I can.

## Research Notes
During the process of making this randomizer, I've compiled several research notes on the internal structure of Radiant Dawn, including character block locations/lengths. They can be found [here](https://docs.google.com/spreadsheets/d/1SB0EZSW0u7tHKTgQv-fEJFDxgORcouMdmTTc9lZ0DHk/edit#gid=0).
