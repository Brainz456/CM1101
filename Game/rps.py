import random
choices1 = ["rock", "paper", "scissors"]
choices2 = ["heads", "tails"]

def rps():
    print("Lets play Rock, Paper, Scissors!")
    
    user_input = str(input("ROCK, PAPER or SCISSORS: "))
    compans = random.choice(choices1)
    
    if user_input == "rock":
        if compans == "paper":
            print("Paper!! Oh man, I won!")
            return [True, False]
        elif compans == "scissors":
            print("Scissors!! Noooo, I lost!")
            return [False, True]
        else:
            print("Rock!! It's a draw!")
            return rps()
    
    elif user_input == "paper":
        if compans == "paper":
            print("Paper!! It's a draw!")
            return rps()
        elif compans == "scissors":
            print("Scissors!! Oh ma, I won!")
            return [True, False]
        else:
            print("Rock!! Noooo, I lost!")
            return [False, True]
        
    elif user_input == "scissors":
        if compans == "paper":
            print("Paper!! Noooo, I lost!")
            return [False, True]
        elif compans == "scissors":
            print("Scissors!! It's a draw!")
            return rps()
        else:
            print("Rock!! Oh man, I won!")
            return [True, False]
    else:
        print("please enter a valid text.")
        return rps()
    
    
    
def heads_or_tails():
     user_input = str(input("Please select either HEADS or TAILS: "))
     flip = random.choice(choices2)
     
     if user_input == flip:
         print("Nice choice! Guess this means I take a drink!")
         print("Your friend takes a drink.")
         return False
     else:
         print("Haha! Man, you lost so you drink!")
         print("You take a drink.")
         return True
    
