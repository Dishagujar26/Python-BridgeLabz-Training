# loops in python 

# for loop 
for i in range(5): # by deafult it is range(0,5) 
    print(i)     

# while loop
i = 0   
while i < 5:
    print(i)
    i += 1

# nested loop
for i in range(3):
    for j in range(2):
        print(i, j)

# loop with else
for i in range(5):
    print(i)                    
else:
    print("Loop is finished")

# break statement
for i in range(5):
    if i == 3:
        break
    print(i)

# continue statement
for i in range(5):
    if i == 3:
        continue
    print(i)

# pass statement
for i in range(5):
    if i == 3:
        pass # working of pass statement is to do nothing and it is used as a placeholder for future code
    print(i)

# loop with else and break
for i in range(5): 
    if i == 3:
        break
    print(i)
else:
    print("Loop is finished")

    
# Print even numbers from 0 to 10 using while loop

i = 0 
while i < 10:
    if i%2 == 0:
        print(i)
    i += 1
print("Loop finished")

# Print 1 to 50 using for loop 

i = 1
for j in range(50):
    print(j)
print("loop finished")

list_of_numbers = [1, 2, 3, 4, 5]

for num in list_of_numbers:
    print(num)


# range function is used to generate a sequence of numbers. 
# It takes three arguments: start, stop, and step. 
# The start argument is the number from which the sequence starts, the stop argument is the number at which the sequence ends (exclusive), and the step argument is the difference between each number in the sequence. 
# If the start argument is not provided, it defaults to 0. If the step argument is not provided, it defaults to 1.

# Example of range function in python

for k in range(1,20,5):
    print(k) # output will be 1, 6, 11, 16 because the step is 5 and it starts from 1 and ends at 20 (exclusive)

# exclusive means that the end value is not included in the range of values, 
# while inclusive means that the end value is included in the range of values.




