import os
def clear():
    os.system('cls')
    
word = input("What is the word your friends are going to guess? ")
clear()
newWord = ""
for x in range(0, len(word)):
    newWord += "_"
print(newWord)
