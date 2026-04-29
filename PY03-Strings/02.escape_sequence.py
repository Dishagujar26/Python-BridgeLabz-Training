# Escape Sequence in string manipulation is a way to represent special characters in a string that cannot be directly included in the string.
# An escape sequence is a combination of a backslash (\) followed by a character that has a special meaning. 
# The backslash is used to indicate that the following character should be treated differently than it normally would be.

# \n : New Line - it is used to insert a new line in the string. When the string is printed, the text after the \n will be displayed on a new line.
print("Hello\nWorld")
print("Hello\n\nWorld") # It will insert two new lines between "Hello" and "World"

# \t : Tabculation - it is used to insert a tab space in the string. When the string is printed, the text after the \t will be displayed with a tab space before it.    
print("Hello\tWorld")
print("Hello\t\tWorld") # It will insert two tab spaces before "World"
print("Hello\t\t\tWorld") # It will insert three tab spaces before "World" 

# \\ : Backslash - it is used to insert a backslash in the string. When the string is printed, the backslash will be displayed as a normal character.
print("Hello\\World") # output: Hello\World
print("Hello\\\\World") # output: Hello\\World

# \' : Single Quote - it is used to insert a single quote in the string. When the string is printed, the single quote will be displayed as a normal character.
print('Hello\'s World') # output: Hello's World
print('Hello\\\'s World') # output: Hello\'s World

# \" : Double Quote - it is used to insert a double quote in the string. When the string is printed, the double quote will be displayed as a normal character.
print("Hello\"s World") # output: Hello"s World

# \r : Carriage Return - it is used to move the cursor to the beginning of the line. When the string is printed, the text after the \r will overwrite the text before it.
print("Hello\rWorld") # OUTPUT: World
print("Hello\r\nWorld") # OUTPUT: World (the \n moves the cursor to the next line, so "Hello" is printed on the first line and "World" is printed on the second line)
print("Hello\r\n\rWorld") # OUTPUT: World (the first \r moves the cursor to the beginning of the line, the \n moves the cursor to the next line, and the second \r moves the cursor back to the beginning of the line, so "Hello" is printed on the first line and "World" is printed on the second line)

# \b : Backspace - it is used to move the cursor one position back. When the string is printed, the text after the \b will overwrite the text before it.
print("Hello\bWorld") # output: HellWorld 
print("Hello\b\bWorld") # output: HelWorld 

# \f : Form Feed - it is used to move the cursor to the next page. When the string is printed, the text after the \f will be displayed on the next line.
print("Hello\fWorld") # output: Hello
print("Hello\f\fWorld") # output: Hello (the first \f moves the cursor to the next page, and the second \f moves the cursor to the next page again, so "Hello" is printed on the first page and "World" is printed on the second page)

# \v : Vertical Tab - it is used to move the cursor down to the next line. When the string is printed, the text after the \v will be displayed on the next line.
print("Hello\vWorld") # output: Hello
