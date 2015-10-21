#!/usr/bin/python3

import random

code = []
guess = []
guessCounter = 0

def mastermind():
    
    global code
    global guess
    global guessCounter
    
    code.append(random.randint(1, 4))
    code.append(random.randint(1, 4))
    code.append(random.randint(1, 4))
    code.append(random.randint(1, 4))
    
    print("Lets play mastermind!")
    print("The aim of this game is to guess the 4 digit code correctly.")
    
    correctCount = 0
    
    while correctCount < 4:
        print("Input 4 values from 1 - 4  to guess the 4 digit code:")
        print("To do this, input the 1st value, then press the enter key. Enter the 2nd value, then press the enter key etc.")
        guess.append(int(input("> ")))
        guess.append(int(input("> ")))
        guess.append(int(input("> ")))
        guess.append(int(input("> ")))
        
        for i in range(0, len(code)):
            if guess[i] == code[i]:
                correctCount = correctCount + 1
        
        if correctCount < 4:
            guess = []
            print("Incorrect. You have guessed " + str(correctCount) + " out of 4 digits correctly.")
            guessCounter = guessCounter + 1
            correctCount = 0
    
    print("Correct! You guessed incorrectly " + str(guessCounter) + " times. So you must incur " + str(guessCounter) + " units of alcohol.")
    return guessCounter