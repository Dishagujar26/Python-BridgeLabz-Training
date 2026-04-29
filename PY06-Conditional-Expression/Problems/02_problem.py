math = float(input("Enter a marks for math: "))
chemistry = float(input("Enter a marks for chemistry: "))
physics = float(input("Enter a marks for physics: "))

list_of_marks = [math, chemistry, physics]
sum = sum(list_of_marks) % 100

if(sum > 40):
    if(math > 33 and chemistry > 33 and physics > 33):
        print("Congratulations! You have passed the exam")
else:
    print("Sorry! You have failed the exam")

