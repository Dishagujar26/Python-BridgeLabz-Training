# file IO in python what is it and how to use it?
# In python we can use the open() function to open a file and read it.

# open function take two arguments filename and mode and return a file object
# mode is a string that specifies how the file should be opened and readed
# mode can be "r" for read, "w" for write, "a" for append
# by default the mode is "r"

# operations that we can perform on a file object are read(), write(), close(), seek(), tell()

# open a file
f = open("filename.txt", "r")

# read a file
f = open("filename.txt", "r")
print(f.read())

# read and then write
f = open("filename.txt", "r+")
print(f.read())
f.write("Hello world!")
f.close()

# close a file
f = open("filename.txt", "r")
print(f.read())
f.close()

# write to a file
f = open("filename.txt", "w")
f.write("Hello world!")
f.close()

# write and then read
f = open("filename.txt", "w+")
print(f.read())
f.write("Hello world!")
f.close()

# differnce between r+ and w+ mode in python
# r+ mode will read and write to a file
# w+ mode will write to a file and read from a file

# what's the difference between write and append?
# write will overwrite the file example if the file already exists it will be overwritten and if the file doesn't exist it will be created and the file will be empty
# append will append the file example if the file already exists it will be appended and if the file doesn't exist it will be created


# append to a file
f = open("filename.txt", "a")
f.write("Hello world!")
f.close()

# append and then read - a+ mode will append to a file and read from a file
f = open("filename.txt", "a+")
print(f.read())
f.write("Hello world!")
f.close()

# read plus append
f = open("filename.txt", "r+")
print(f.read())
f.write("Hello world!")
f.close()

# update a file - modify existing content 
f = open("filename.txt", "r+")
content = f.read()

f.seek(0) # this will set the cursor to the beginning of the file
f.write("Updated: " + content)

f.close()

# delete a file
import os
os.remove("filename.txt")

# rename a file
import os
os.rename("filename.txt", "newfilename.txt")

# copy a file
import shutil
shutil.copy("filename.txt", "newfilename.txt")

# move a file
import shutil
shutil.move("filename.txt", "newfilename.txt")

# read a file line by line
f = open("filename.txt", "r")
for x in f:
    print(x)
f.close() 

# another way to read a file line by line
line  = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()

# read a file character by character
f = open("filename.txt", "r")
for x in f:
    for y in x:
        print(y)
f.close()

# read a file byte by byte
f = open("filename.txt", "rb")
for x in f:
    print(x)
f.close()

# with satetement in python - it both reads and writes to a file at the same time without having to close the file manually 
with open("filename.txt", "r") as f:
    print(f.read())

with open("filename.txt", "a") as f:
    f.write("\nNew line added")