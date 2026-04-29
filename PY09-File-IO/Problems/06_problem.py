
with open("log.txt","r") as f:
    content  = f.read()

# find is python is written or not in the file and in which line it is written 

if "python" in content:
    print("python is present")
else:
    print("python is not present")

# find the line number where python is written in the file

with open("log.txt","r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"Python is present in line number {lineno}")
        break # if we break else won't be executed
    lineno += 1
    
else:
    print("python is not present")
  