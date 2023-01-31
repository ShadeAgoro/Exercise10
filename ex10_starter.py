import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames

import os.path
import glob
# glob patterns expand a wildcard pattern to retrieve a list of filenames
# asterick means all
files = glob.glob('*')
# built-in function to stream output with filenames in terminal
print(files)

# TODO: use os.path.getsize to find each file's size
import os.path
# assign file size to wildcard pattern
filesize = os.path.getsize(hdir)

# initially wrote print((filesize) + "bytes") as a command
# this came back with an error message
# 'unsupported operand types(s) for +: 'int' and 'str'
# added 'str' as file size is a string
# built-in function then printed a string of output in bytes
print(str(filesize) + "bytes")

# TODO: Add a test to only display files that are not zero length
import os.path
# import os.path again as this is how file names were initially retrieved

# ran a conditional test to pass the directory and display file sizes more than zero
for file in files:
    size = os.path.getsize(hdir)
if size == 1:
    print(str(filesize) + "bytes")

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()





