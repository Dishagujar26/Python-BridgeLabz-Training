
'''
BaseException
    ├── Exception
    │      ├── ValueError
    │      ├── TypeError
    │      ├── NameError
    │      ├── IndexError
    │      ├── KeyError
    │      ├── ZeroDivisionError
    │      └── your custom exception
    │
    ├── KeyboardInterrupt
    └── SystemExit

'''

# Custom Exception + raise + try/except in one code

# Creating our own custom exception
# Exception is parent class for all errors
class InvalidAgeError(Exception):
    pass


def check_age(age):

    # validating input type
    if not isinstance(age, int):
        # manually throwing error
        raise TypeError("Age must be integer")

    # business validation
    if age < 0:
        # raising custom exception
        raise InvalidAgeError("Age cannot be negative")

    print("Valid age:", age)


# try block = code that may throw exception
try:
    check_age("25")      # wrong type
    check_age(-5)        # custom exception
    check_age(22)        # valid

# catches built-in exception
except TypeError as e:
    print("Type Error:", e)

# catches custom exception
except InvalidAgeError as e:
    print("Custom Error:", e)

# always runs
finally:
    print("Program finished")

print ("Program finished and continue after the try block")


# try with else caluse - Run else only if no exception occurs in try.
# For code that should run only when try succeeds.

try:
    num = 10 / 2
    print(num)

except ZeroDivisionError:
    print("Cannot divide")

else:
    print("Division successful")

finally:
    print("Done")