
n = 3
for i in range(0,n):
    for j in range (0, i+1):
        print("* ", end="")
    print()


""" Write a program to print the following star pattern.
* * *
*   * for n = 3
* * *
"""

print()
for i in range(n):
    for j in range(n):
        if i == 1 and j == 1:
            print("  ", end="")
        else:
            print("* ", end="")
    print()


