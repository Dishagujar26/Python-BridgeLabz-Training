n = 3

# range(n, 0) moves forward by default (+1), but 3 → 0 needs to move backward (-1), so loop never runs.

for i in range(n+1, 0, -1):
    for j in range(i-1):
        print("* ", end="")
    print()

    
for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    print()