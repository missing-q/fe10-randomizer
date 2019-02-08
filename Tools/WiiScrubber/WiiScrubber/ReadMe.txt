WiiPartitionBinChanger version 1.0

Written by Dack 2008/2009

Whats it do?

It allows you to view and edit some of the parameters in the partition.bin that
is created by the Wiiscrubber application.

The partition.bin is what I called the amalgamation of ticket, tmd, certificates and H3 table
at the start of a Wii partition. It also includes the various pointers relating to each of these
sub-sections.

It has the Trucha signing bits built in so allows you to change, and sign, tickets and TMDs.

And this means?

You can now create your own TMDs for things like Guitar Hero that will then have their own save slot.

Whats needed to run it?

The usual key.bin file is required AS WELL AS a copy of the Korean common key as a file called
"kkey.bin" in the same directory. These can be found in the usual places or created using the application
"MakeWiiKeyBin.exe" Version 1.1.

The reason for the Korean Key is that the application can change the necessary byte in the ticket and allow
Korean discs to be transfered to use the usual common key very easily. (click button, sign, save, insert)

Most of the data in the ticket and tmd can be altered, the certs and H3 are view only.

EXCEPT

Each of the tabs in the display has a load button - this can be used to insert different a sub-file e.g cert,
h3, ticket or TMD. The companion SAVE button in the panel allows you to save the sub-file.

If different sized certs or TMD are loaded then it shouldn't matter as the necessary pointers are updated in
the complete partition.bin.

Needless to say - if you sign anything they don't work on Wiis where the firmware has the bug fixed.

Bugs/Features:
I'm sure there are more than a few, post on Gbatemp.net when you find some
Ones I know of:
  It will still work if you don't have the Korean key - you just may get some 'interesting' results
  As ticket and TMD are seperate entities changes in title ID are not echoed to the other
  No prompt to save on exit
  Very lax error checking on field entry

Tips:
1. If you are changing the TMD for an existing game, remember to change the boot.bin bytes as well
2. Use Wiiscrubber 1.30 for the partition.bin extraction/replacement as a bug was introduced in 1.31 that
   disabled that function - DOH!

Thanks:
Everyone who Beta tested
Team Twiizers for the release of the Keys

Dack

BftD

History:
08/01/09 - Initial release of version 1.0

Source code will be available after the usual tidy up period over on drop.io/wiiscrubber
Uses the OpenSSL library
