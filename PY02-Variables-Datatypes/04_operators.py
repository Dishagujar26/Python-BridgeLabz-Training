# Arithmetic Operators

a = 34
b = 5
c = a + b # Addition
print ("Addition:", c)

# Assignment Operators

a = 4-2 
b = 6
b += 3 # Increment the value of b by 3 anf then assign the result to b
print ("Subtraction:", b)

# Comparison Operators

d = 5>4
print ("Greater than:", d)

d = 5==5
print ("Equal to:", d)

d = 5!=5
print ("Not equal to:", d)

d = 5<=5
print ("Less than or equal to:", d)

d = 5>=4
print ("Greater than or equal to:", d)

# Logical Operators

x = 4
y = 5
z = (x > 3) and (y < 6) # Logical AND
print ("Logical AND:", z)

z = True or False # Logical OR
print ("Logical OR:", z)

z = not (x > 3) # Logical NOT
print ("Logical NOT:", z)

z = (x > 3) and not (y < 6) # Logical AND with NOT
print ("Logical AND with NOT:", z)

z = (x > 3) or not (y < 6) # Logical OR with NOT
print ("Logical OR with NOT:", z)

z = (x > 3) and (y < 6) or not (x == y) # Logical AND and OR with NOT
print ("Logical AND and OR with NOT:", z)

# Truth Table for OR operators

print ("Truth Table for OR operators:")
print ("A\tB\tA OR B")
print ("True\tTrue\t", True or True)
print ("True\tFalse\t", True or False)
print ("False\tTrue\t", False or True)
print ("False\tFalse\t", False or False)

# Truth Table for AND operators

print ("Truth Table for AND operators:")
print ("A\tB\tA AND B")
print ("True\tTrue\t", True and True)
print ("True\tFalse\t", True and False)
print ("False\tTrue\t", False and True)
print ("False\tFalse\t", False and False)

# Truth Table for NOT operators

print ("Truth Table for NOT operators:")
print ("A\tNOT A")
print ("True\t", not True)
print ("False\t", not False)





