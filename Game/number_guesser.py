import random
number = int(random.randrange(1, 11))
penaltyCounter = 0

def number_guesser():
    
    global penaltyCounter
    
    while True:
        guess = int(input("Your guess: "))
        if guess == number:
            print("Correct.")
            return penaltyCounter
            break
        elif guess > number:
            print("Your guess is too big!")
        else:
            print("Your guess is too small!")
        
        penaltyCounter += 1