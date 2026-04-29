letter = '''
Dear <|NAME|>,
You are selected!
<|POSITION|> is the position you have been selected for.
<|SALARY|> is the salary you will be receiving.
<|Date|> is the date you will be joining the company.
Have a great day ahead!'''

name = input("Enter your name: ")
position = input("Enter your position: ")
salary = input("Enter your salary: ")
date = input("Enter your joining date: ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|POSITION|>", position)
letter = letter.replace("<|SALARY|>", salary)
letter = letter.replace("<|Date|>", date)

# By chaining 
# letter = letter.replace("<|NAME|>", name).replace("<|POSITION|>", position).replace("<|SALARY|>", salary).replace("<|Date|>", date)
print(letter)
