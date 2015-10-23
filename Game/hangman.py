from time import *
import random
answer = ["CARDIFF","UNIVERSITY","STUDENT","FRESHERS","PYTHON","COMPILER","INTERPRETER", "BREAKPOINT", "NIGHTLIFE", "TECHNOLOGY", "GUINESS", "WINDOWS"]
used_letters = []
picture = {0 : """ 
    +---+
    |   |
        |
        |
        |
        |
========= """, 1:""" 
    +---+
    |   |
    O   |
        |
        |
        |
========= """, 2:""" 
    +---+
    |   |
    O   |
    |   |
        |
        |
========= """, 3:""" 
    +---+
    |   |
    O   |
   /|   |
        |
        |
========= """, 4:""" 
    +---+
    |   |
    O   |
   /|\  |
        |
        |
========= """, 5:""" 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
========= """, 6:""" 
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
========= """}

def exec_hangman():
    selected_answer = random.choice(answer)
    shown_answer = []
    strikes = 0
    
    print("""
Let's play Hangman. The object of the game is simple, guess the word. 
But there is a catch: each time you guess wrong, you get a strike. 
At the end of the game, you drink for each strike you take. 
Sound simple enough? Then let's start.""")
    sleep(10)    
    
    
    while strikes < 6:
        
        for char in selected_answer:
                if char in used_letters:
                    shown_answer.append(char)
                else:
                    shown_answer.append("_")
            
        for char in used_letters:
                if char in selected_answer:
                    pass
                else:
                    strikes += 1  
                    
        print("")
        print(picture[strikes])
        print("")
        print("Guess the word:",shown_answer)
        print ("used letters:" , used_letters)
        print("Strikes:", strikes)
        
        if selected_answer == "".join(shown_answer):
            print("You win!!!")
            return strikes
        
        
        if strikes == 6:
            print("Hangman! You lose, time to drink!")
            print("The word was:", selected_answer)
            return strikes
        user_input = str(input("Please enter a letter to guess:"))
        shown_answer = []       
        strikes = 0
            
        if len(user_input) > 1 or user_input.isalpha() == False:
            print ("Enter a single letter please")
            sleep(3)
            
        else:
            user_input = user_input.upper()
            used_letters.append(user_input)
