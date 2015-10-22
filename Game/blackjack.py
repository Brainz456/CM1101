import random
import time
deck_drawn = []
removed_cards = []
#suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

value = {"Ace" : 11,
         "2": 2,
         "3" : 3, 
         "4" : 4, 
         "5" : 5, 
         "6" : 6, 
         "7" : 7, 
         "8" : 8, 
         "9" : 9, 
         "10" : 10,
         "Jack" : 10, 
         "Queen" : 10, 
         "King" : 10 
         }
players_hand = []
dealers_hand = []

def blackjack():
    counter = 0
    strikes = 0
    while counter < 3:         
        while len(players_hand) < 2:
            card = random.choice(numbers)
            players_hand.append(card)
            deck_drawn.append(card)
            
            while len(dealers_hand) < 2:
                card = random.choice(numbers)
                dealers_hand.append(card)
                deck_drawn.append(card)
                
                while True:
                    player_score = 0
                    for number in deck_drawn:
                        if deck_drawn.count(number) > 3:
                            if number in removed_cards:
                                pass
                            else:
                                numbers.remove(number)
                
                for card in players_hand:
                    points = value.get(card)
                    player_score += int(points)
                    
                    if player_score > 21:
                        if "Ace" in players_hand:
                            value["Ace"] = 1
                        else:
                            print("You are bust! You lose.")
                            strikes += 1
                            counter += 1
                        n = len(dealers_hand)
                        print("Your hand:", players_hand)
                        time.sleep(1)
                        print("Your score is:", player_score)
                        time.sleep(1)
                        print("The dealer's shown card is:", dealers_hand[0:(n-1)])
                        time.sleep(1)
                        print("You may:")
                        print("1) Stick")
                        print("2) Hit")
                        time.sleep(1)
                        user_input = str(input("Enter choice number:"))
                        if user_input == "1":
                            while True:
                                for number in deck_drawn:
                                    if deck_drawn.count(number) > 3:
                                        if number in removed_cards:
                                            pass
                                        else:
                                            numbers.remove(number)
                                print("The dealer's shown card is:", dealers_hand[0:n])
                                time.sleep(1)
                                dealers_score = 0
                                for card in dealers_hand:
                                    points = value.get(card)
                                    dealers_score += int(points)
                                                
                                print("The Dealer's score is:", dealers_score)
                                if dealers_score > 21:
                                    print("The Dealer went bust. You Win!")
                                    counter += 1
                                if dealers_score < 15:
                                    print("The dealer Hits...")             
                                    card = random.choice(numbers)
                                    dealers_hand.append(card)
                                    deck_drawn.append(card)
                                                
                                if dealers_score >15:
                                    dealer_diff = 21 - dealers_score
                                    player_diff = 21 - player_score
                                    print("Your score is:", player_score)
                                    print("The Dealer's score is:", dealers_score)
                                    if player_diff < dealer_diff:
                                        print("You have won, Congratulations!")
                                        counter += 1
                                    else:
                                        print("You have lost, unlucky.")
                                        counter += 1
                                        strikes += 1
                                                                        
                                                                        
                        elif user_input == "2":
                            card = random.choice(numbers)
                            players_hand.append(card)
                            deck_drawn.append(card)
                            print ("You drew a", card)
                            time.sleep(2)
                        else:
                            print("You must either stick or twist.")
                            time.sleep(3)
    return strikes
                                                    
#blackjack()