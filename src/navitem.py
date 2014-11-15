# Created by Eli Foster
# 0.1.6

import shutil
import tempfile
import sys
import os
import time

# EDIT THIS IF YOU HAVE CHANGED YOUR DIRECTORY NAMES.
directory = 'work/navitem_input.txt'
new_dir = 'work/navitem_output.txt'

def run():
    #These can be found on Template:G/Mods.
    #If you are running Python 3, change raw_input to input for it to work. You may still get errors though.
    modname = raw_input("What is the mod abbreviation?\nIf you are unsure, or it is not on the list, please contact Santa. If you are Santa, do it.\n")

    tmp = tempfile.NamedTemporaryFile(delete=False)
    with open(directory) as finput:
        with open(tmp.name, 'w') as ftmp:
            for line in finput:
                x = str(line)
                ftmp.write('\t-->{{NI|' + x.rstrip("\r\n") + "|mod=" + modname + "}}{{,}}<!--\n")
    try:
        shutil.copyfile(tmp.name, new_dir)
    except:
        print "There was an issue using shutil! Trying to use os instead."
        os.rename(directory, new_dir)

time_amount = time.clock()
run()
print ("Navitem list generated. It took " + str(time.clock() - time_amount) + " seconds")

time.sleep(1)
print ("Program is now exiting.")
time.sleep(0.5)
sys.exit()

'''
== Changelog ==
=== 0.2.0 ===
* NEW: Now tells you that it has finished, and how long it took.
* NEW: Things aren't instant, because that bothers me (+ some console messages to tell you things)
* FIX: Program exits properly.

=== 0.1.6 ===
* FIX: Shoved everything in run() method

=== 0.1.5 ===
* FIX: Changed directories AGAIN.

=== 0.1.4 ===
* FIX: Changed directories to work/navitem/input-output.txt, for when I add more programs to this repo.

=== 0.1.3 ===
* FIX: Fixed tab spacing; it's no longer 4 spaces.

=== 0.1.2 ===
* FIX: No longer overwrites input; instead it makes output.txt.
* FIX: It should now work, though be weird, on non-UNIX-based systems. (thanks wolfman)
* FIX: Program exits properly with sys.exit

=== 0.1.1 ===
* FIX: Made the text that gets written actually correct.
* TWEAK: Changed modname raw_input text.

=== 0.1.0 ===
* Initial build.

'''
