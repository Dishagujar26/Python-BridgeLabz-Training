
hindi_dic = {
    "नमस्ते": "Hello",
    "कैसे": "How",
    "हो": "are",
    "आप": "you"
}

word = input("Enter a Hindi word to get the meaning: ")
print(hindi_dic.get(word, "Word not found in the dictionary"))  