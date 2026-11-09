# we will learn to delete a file or to check a file that exist or not >>

import os 
if os.path.exists("/Users/harshraj/python/file_handling/demoreadfiles.txt"):
    print("Your file exists in the directory!")
else:
    print("Your file do not exist int the directory!")
# to delete use os.remove() exixting file..

os.remove("/Users/harshraj/python/file_handling/demodeletefile.txt")

# To delete an entire folder, use the os.rmdir() method:
# import os
# os.rmdir("myfolder")
