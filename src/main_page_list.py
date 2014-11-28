# Created by Eli Foster
# 0.1.0

import shutil
import tempfile
import sys
import os
import time
import gc

# EDIT THIS IF YOU HAVE CHANGED YOUR DIRECTORY NAMES.
directory = 'work/mainlist_input.txt'
new_dir = 'work/out/mainlist_output.txt'

def run():
    tmp = tempfile.NamedTemporaryFile(delete=False)
    with open(directory) as finput:
        with open(tmp.name, 'w') as ftmp:
            for line in finput:
                x = str(line)
                ftmp.write("[[" + x.rstrip("\r\n") + "]] {{*}} ")
    try:
        shutil.copyfile(tmp.name, new_dir)
    except:
        print "There was an issue using shutil! Trying to use os instead."
        os.rename(directory, new_dir)

time_amount = time.clock()
run()
print ("Main page list generated. It took " + str(time.clock() - time_amount) + " seconds")
print ("Program is now exiting and clearing memory.")
time.sleep(0.5)
directory = None
new_dir = None
time_amount = None
gc.collect()
print ("Memory cleared as much as possible.")
sys.exit()

'''
== Changelog ==
=== 0.1.0 ===
* Initial build.

'''
