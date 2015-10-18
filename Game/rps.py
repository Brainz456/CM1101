import random
choices1 = ["rock", "paper", "scissors"]
choices2 = ["heads", "tails"]

def exec_rps():
    print("Lets play Rock, Paper, Scissors")
    
    user_input = str(input("Rock Paper Scissors!!"))
    compans = random.choice(choices1)
    
    if user_input == "rock":
        if compans == "paper":
            print("Paper!! Oh man, I won!")
        elif compans == "scissors":
            print("Scissors!! Noooo, I lost!")
        else:
            print("Rock!! It's a draw!")
    
    elif user_input == "paper":
        if compans == "paper":
            print("Paper!! It's a draw!")
        elif compans == "scissors":
            print("Scissors!! Oh ma, I won!")
        else:
            print("Rock!! Noooo, I lost!")
        
    elif user_input == "scissors":
        if compans == "paper":
            print("Paper!! Noooo, I lost!")
        elif compans == "scissors":
            print("Scissors!! It's a draw!")
        else:
            print("Rock!! Oh man, I won!")
    else:
        print("please enter a valid text")
    
    
    
def exec_cflip():
     user_input = str(input("Please select either HEADS or TAILS"))
     flip = random.choice(choices2)
     
     if user_input == flip:
         print("Nice choice, Guess this means I take a drink")
     else:
         print("Haha man, you lost so you drink")
         print("'You take a drink'")
    
