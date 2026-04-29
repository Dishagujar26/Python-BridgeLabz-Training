# Repeat program 4 for a list of such words to be censored

word_to_censor = ["angry", "rude", "stupid", "nonsense", "foolish", "idiot", "dumb", "ugly", "pathetic", "hateful", "offensive", "insulting"]

for i in word_to_censor:
    with open("censored.txt", "r") as f:
        content = f.read()
        content = content.replace(i, "*" * len(i))
    
    with open("censored.txt", "w") as f:
            f.write(content)