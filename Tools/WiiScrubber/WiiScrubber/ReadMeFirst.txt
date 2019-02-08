Wiiscrubber 1.40 - The next degeneration

*sigh* Just couldn't leave it alone version. Lots of changes, some subtle, some not so.

Whats new?

1. ticket.bin is displayed under the partition.bin breakout
2. cert.bin and tmd.bin can now be different sizes
3. Extra button for Trimming an ISO - this makes an ISO slightly larger than the indicated data size - USES TRUCHA
4. Confirmation window on Shrinking partition
5. Proper Korean key support so can open and scrub/trim/extract/replace Korean ISOs
7. Deleted the 'force Wii' option as I followed the advice of Marcan
8.Partition support corrected due to a Wii limitation on Primary partition (you can only have
   three partitions in the primary. To paraphrase Star Wars "Many verbatims died to bring you this information").
9.Can save/load/import crypted partitions making replacement much quicker
10.Full 4 partition offset support
11.Partition titles displayed in the window. 

In other words you can easily create a multipartition disc. AKA a multiboot.

Companion software:
1. Makewiikeybin. exe - makes a key.bin file for you. Does not contain the actual key but generates it from
   a simple algorithm. - Decided to remove this from the pack due to some twittering. See links for possible
   solution - I also recommend hexd.exe. Version 1.1 also generates the Korean kkey.bin.
2. PartitionBuilder - allows you to generate a partition file that can be loaded via wiiscrubber. This
   means you can now generate an entire partition from a directory of files. So rather than changing one at
   a time you can extract an entire partition, change whatever files you want and then rebuild.
3. Partition.bin changer - allows you to view/modify the ticket, tmd, certs and h3.bin in one simple editing package
   Allows trucha signing of ticket and tmd
4. HBC Multiboot file, based on SoftChip, that allows you to select which partition to boot from. i.e. A multiISO loader


If not included in the pack then check out drop.io/wiiscrubber you'll also find the source code there.

Bug Fixes:
1. You can actually load/replace partition.bin again - this was broken in the 1.30 to 1.31 update
2. Shrink partition works correctly now - incorrect size was being copied down - OOOPS.
3. Can change the bootmode of unusually defined boot mode discs
4. Partitions now start on a 0x20000 boundary as the Wii seems to like them that way
5. Partitions in the second partition table now show correctly

Bugs:
Trimming still needs some work to confirm most title work correctly. At least I can now test due to having obtained
a Flatmii.

Thanks to:
1. My wife for putting up with me while I twiddled with this
2. Lots of people who did beta testing e.g sr_corsario
3. People who suggested things or who's software I 'borrowed' e.g. Wiipower and the Softchip people


You need:
You will need a copy of the ubiquitous "key.bin" in the same directory.
For full functionality you also require the Korean "kkey.bin"
You should not need to install any extra runtime files.
A descrambled wii iso
Plenty of disc space
A fair bit of time.

How to use:
Copy the key.bin file to the same directory as the exe.
Load the software.
Load the ISO file by clicking on the 'load iso' button
What the program is doing appears in the bottom window
Disc filelist appears in the top window as a standard treelist
Name of game and size of the data on the disc appears in top right

How to extract files:
Only one at a time at present
In the treelist click on a file to select
Right click the mouse button
Select 'Save' from the popup menu
The fields on the filename shown are:
name, partition, Offset into decrypted file, Filesize, file reference in FST (-ve means system file)

How to scrub the disc:
Click on the clean and save button
Depending on the option chosen next to the clean button you will then save
either a scrubbed file, a dif file or both files. If the TRUCHA option is chosen then
you will create several new files:
1. a dummy fst.bin
2. a modified fst.bin containing links for the padding files
3. several files full of 0's that can be loaded into the modified image.
4. a modified boot.bin that is needed for the modified fst.bin to be accessed

ISO: This creates a copy of the loaded ISO with the same name but (compress)
appended to the name before the .ISO part  (so SPM.ISO would become
SPM(compress).ISO).
DIFF: This creates a Diff file of the differences between the loaded file and
what a scrubbed one would contain. The filename used is the same as the savename but with
.dif used instead of ISO
BOTH: does both ISO and DIFF - you will need a LOT of storage for this

Compressing the scrubbed image should give you a figure close to the size of data
detailed earlier. The DIFF file will not compress that well (due to it being the
random data contained in the 'empty' disk blocks.


Comments:
I've tried on quite a few files, checking the files that are then extracted and
all seems correct. But no 100% guarantees can be made that the cleaned ISO will
work. What I tend to do is extract all the files from an uncleaned image using wiitools
and then extract all the same files from a cleaned image and do a windiff on them to
check for any irregularities. There is always the potential that Nintendo will start
checking for these sort of changes in a firmware update. Just be aware.

Sources etc.:
The source code is written under Visual C 6 (what I had installed here at the time).
The source will be released when I have a fully stable build.
Some of the source is from the excellent wiifuse
Some source code from Waninkokos wiifrii
Openssl source is also included for the crypto

Limitations/Errors/Bugs/Features/Improvements:
You may notice the 'load' function on the file popup - that would be a target - FIXED
Multiple file extraction would be more than useful but I thought it was better to
test the extraction function on single files first
I've got an issue where a release version will not work correctly, thats why this release is
a debug build. (*Love* finding those errors) - FIXED - Thanks to Juster at GBATemp.net
Yes the Icon is rubbish - one of my trademarks - will be fixed soon
File size is limited to 4.5 Gig as if the software is on a DL disc it probably needs to be - Fixed
Some of the extracted Disc titles look odd - not my fault :) - Fixed

Wish list:
N/A


Comments/Suggestions/Errors:
Pop over to GBATEMP.NET and post on the boards there.
Changes from 1.31

Changes from 1.30
*17 Can cater for discs that have non-standard disc IDs by using the 'force wii' check
    box e.g. iso_template.iso.bz2
*18 Can extract/replace the sub parts of partition.bin i.e. tmd.bin, cert.bin and h3.bin
*19 Added two useful links in the about box ;)

Changes from 1.21
1. Extra options on right click menu related to partition operations
   (you can now delete them and resize the data area)
2. Increased speed of file replacement by blocking it (and progress bar)
3. Extra couple of links in the about box
4. Window is now resizable (within limits)
5. Some of the text on buttons changed
6. More accurate indication of size as headers are now included in calculation
   and dynamically considered when header button pressed
7. Extra option on right click for WIIDISC as it allows for changing between
   system boot and normal boot
8. Common key check possible to over-ride in case Korean key becomes available
9. Can now replace the partition.bin file
10. Can add data partitions/channels
11. Can 'shuffle' up the partitions to the start of the disc for where some have
    been deleted - doesn't use Trucha bug.
12. Can Shrink the partition by moving the data up in the partition (meaning all
    the free space then appears at the end - Uses Trucha Bug.
13. Can save a decoded partition
14. Can load/replace a decoded partition
15. Can import a new disc partition.
16. Can resize a partition.



Changes from 1.2
1. Bug fixes in the fst.bin size calculation for non-system files
   meant that added files were made as size / 4
2. 32/64 bug in line:
	/* Jump to the specified cluster and copy it to memory */
	offset = iso->parts[partition].offset + iso->parts[partition].data_offset + (cluster * SIZE_CLUSTER);
fixed to:
	/* Jump to the specified cluster and copy it to memory */
	offset = iso->parts[partition].offset + iso->parts[partition].data_offset + (u64)((u64)cluster * (u64)SIZE_CLUSTER);
  so that data could be read above the 2 gig point correctly. Problem possibly exists
  in Waninkokos source code too as it does an int by UL calculation for the cluster * SIZE_CLUSTER

Changes from 1.1b
1. Load file now works
2. Several more bug fixes with 32/64 issues
3. Display changed for partition info to allow VC channels to show
   correctly
4. Trucha signing of disc works automagically
5. Can possibly load files bigger than the original

Changes from 1.0a:
1. Options of creating and using the dif files
2. MoH2 now really does show correctly ;)
3. Key checking to make sure the correct one is used
4. code tidy up
5. Gamecube images work
6. TRUCHA signer padding option
7. Option of keeping crypto headers or not
8. settings are saved in the registry
9. Bug fixing - thank you Juster.

Changes from 1.0:
1. Way of scrubbing changed slightly so that the sector crypto header is left
unchanged. This makes it a bit more difficult to detect but lessens the compressability. 
2. Disc Filename display corrected so titles like MoH2 show correctly ;)
 
Changes from beta test version:
1. Key file now only needs to be in the same directory as the program
2. A progress bar with cancel option when you start scrubbing
3. appended file name changed to (compress) to avoid confusion
4. Clickable URL of gbatemp in about box.
 
Dack
February 2009

DiD
End-ex