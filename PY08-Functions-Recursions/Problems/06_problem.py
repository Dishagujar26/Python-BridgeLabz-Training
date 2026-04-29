# Write a python function to remove a given word from a list and strip it at the same time.

def remove_word(word, list):
   return [item for item in list if item != word] # the job of this line is to remove the word from the list it works by checking each item in the list and if it is not equal to the word then it returns the item
   
   ''' for item in list:
      if word == item:
        list.remove(word)
   return list ''' # The same logic in depth


print(remove_word("apple", ["apple", "banana", "cherry"]))

