# Write a program to find out whether a file is identical & matches the content of another file.

with open("file1.txt", "r") as f1:
    content1 = f1.read()

with open("file2.txt", "r") as f2:
    content2 = f2.read()

if content1 == content2:
    print("Files are identical")
else:
    print("Files are not identical")

# another way of doing this problem 

with open("file1.txt", "r") as f1:
    with open("file2.txt", "r") as f2:
        if f1.read() == f2.read():
            print("Files are identical")
        else:
            print("Files are not identical")