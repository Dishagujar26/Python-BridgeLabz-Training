# wipping out the content of the file 

with open("log.txt", "w") as f:
    f.write("")

# another way of doing this problem 

import os
os.remove("log.txt") # this will remove the file not the content if we want to remove the content we can use os.truncate

os.truncate("log.txt", 0)