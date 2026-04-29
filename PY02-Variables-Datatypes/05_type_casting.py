a = 31.2
b = int(a) # Convert a to an integer
print ("Integer value of a:", b)

a = "harry"
b = int(a) # This will raise a ValueError because "harry" cannot be converted to an integer
b = float(a) # This will raise a ValueError because "harry" cannot be converted to a float
b = type(a) # This will return <class 'str'> because a is a string
print ("Type of a:", b)

a = "123"
b = int(a) # This will convert the string "123" to the integer 123
b = float(a) # This will convert the string "123" to the float 123.0
print ("Integer value of a:", b)

a = 123
b = str(a) # Convert the integer 123 to the string "123"
print ("String value of a:", b)

