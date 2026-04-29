list_of_spam_word = ["make a lot of money", "buy now", "click this", "subscribe this", "free offer"]

email = input("Enter the email: ")

if(email in list_of_spam_word):
    print("This email is a spam email")

else:
    print("This email is not a spam email")