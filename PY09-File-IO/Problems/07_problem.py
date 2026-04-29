# Write a program to make a copy of a text file “this. txt”

with open("source.txt", "r") as f:
    content = f.read()

with open("destination.txt", "w") as f:
    f.write(content)


# another way to fo this problem using copy function

# import shutil
# shutil.copyfile("source.txt", "destination.txt")
