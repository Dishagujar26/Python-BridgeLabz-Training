import os

# specify the directory path (use "." for current directory)
path = '/'

# get list of files and directories
contents = os.listdir(path)

# print each item
for item in contents:
    print(item)