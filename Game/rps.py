import random
choices = ["rock", "paper", "scissors"]


def exec_rps():
    print("Lets play Rock, Paper, Scissors")
    
    user_input = str(input("Rock Paper Scissors!!"))
    compans = random.choice(choices)
    
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
    
    
    
    
    
    
exec_rps()