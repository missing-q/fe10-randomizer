# fe9-randomizer
A WIP randomizer for the game Fire Emblem: Path of Radiance for the Gamecube. Warning- FE9 Randomizer is currently nonfunctional and will probably not either do anything or corrupt your ISO. I'll edit this description once it actually works.

## How to use fe9-randomizer
1. Obtain an ISO of FE9. I'd recommend making a backup copy, just in case.
2. Open up the ISO in GCTool, in the provided Tools folder, then extract it to some directory on your computer.
3. Open BatchLZ77, also in the provided Tools folder, and decrypt the **system.cmp** file in the extracted game. I'd reccomend making another backup of **system.cmp** before decrypting it as well.
4. Now open **system.cmp** in FE9 Randomizer! Wait a bit for the randomizer to apply your selected settings; a notification will pop up when it's done.
5. Once it's randomized, do everything in reverse- reencrypt **system.cmp** with BatchLZ77, then repack your ISO with GCTool. If GCTool says your file is too large, you'll have to select the option to repack the ISO *trimmed*.
6. Have fun! If there are any bugs or you're having trouble somewhere in the process, just shoot me a message on [Discord](https://discord.gg/KJVZWtn) and I'll try to help as best as I can.

If anyone knows of a way to patch FE9 without unpacking the ISO/decrypting files, please let me know!
