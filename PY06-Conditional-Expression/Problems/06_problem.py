math = int(intput("Enter marks for math: "))
chemistry = int(input("Enter marks for chemistry: "))
physics = int(input("Enter marks for physics: "))

list_of_marks = [math, chemistry, physics]
total_marks = sum(list_of_marks) % 100

if(total_marks >= 90 and total_marks <= 100):
    print("Excellent! You have scored an A+ grade")
elif(total_marks >= 80 and total_marks < 90):
    print("Great! You have scored an A grade")
elif(total_marks >= 70 and total_marks < 80):
    print("Good! You have scored a B grade")            
elif(total_marks >= 60 and total_marks < 70):
    print("You have scored a C grade")          
elif(total_marks >= 50 and total_marks < 60):
    print("You have scored a D grade")          
elif(total_marks >= 40 and total_marks < 50):
    print("You have scored an E grade") 
elif(total_marks >= 0 and total_marks < 40):
    print("Sorry! You have failed the exam")





