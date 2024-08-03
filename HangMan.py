import random
import json
from Hangmanart import hangmanart1,logo,stages,you_win,you_lose
from wordlist import words_list






print(f'{logo}')



computer_selected=random.choice(words_list)

computer_selected=list(computer_selected)



word_guess=[]
for i in range(len(computer_selected)):
    word_guess+="_"



counter=0
computer_selected_copy=computer_selected.copy()

while counter<len(stages):
    if word_guess==computer_selected:
        break
    else:
        print(''.join(word_guess))
        guess_letter=(input("Guess a letter:\n"))
        #####Sonrasinda tahmin edilen harfin var olup olmadigi ve word_guess e o harfin eklenmesini yapicam
        if guess_letter in computer_selected:
            while guess_letter in computer_selected_copy:
                word_guess[computer_selected_copy.index(guess_letter)]=guess_letter
                computer_selected_copy[computer_selected_copy.index(guess_letter)]="_"
        else:
            print(stages[counter])
            counter+=1
            
        
if word_guess==computer_selected:
    print(f'{you_win}\nThe word is:{"".join(word_guess)}')
else:
    print(f'{you_lose}\nThe word was:{"".join(computer_selected)}')            