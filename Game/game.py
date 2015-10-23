#!/usr/bin/python3
import os
from map import rooms
from map import *
from player import current_room
from player import inventory
from player import *

from gameParser import *

from characters import *

from rps import *
from hangman import *
from mastermind import *
from number_guesser import *
from Riddles import *
from blackjack import *

import time

current_room = rooms["Home"]

alcoholCounter = 0
winCounter = 0

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    items_as_string = ""
    for item in items:
        items_as_string += str(item["name"]) + ", "

    return items_as_string[:-2]


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    if len(list_of_items(room["items"])) < 1:
        pass
    else:
        print("There is " + list_of_items(room["items"]) + " here.")
        print("")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    if len(inventory) == 0:
        print("You have nothing.")
    else:
        print("You have " + list_of_items(inventory) + ".")
    print("")
    time.sleep(1) # 3


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print("")
    print(room["name"].upper())
    print("")
    # Display room description
    print(room["description"])
    time.sleep(1) # 10
    print("")
    print_room_items(room)
    time.sleep(1) # 5
    

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for item in room_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")

    for item in inv_items:
        print("DROP " + item["id"].upper() + " to drop " + item["name"] + ".")
        
    for item in inv_items:
        if current_room == rooms["Home"]:
            continue
        else:
            print("GIVE " + item["id"].upper() + " to give " + item["name"] + " to " + current_room["character"]["id"] + ".")
    
    for item in inv_items:
        print("EXPLAIN " + item["id"].upper() + " to see the item description for " + item["name"] + ".")
    
    
    if current_room == rooms["Home"]:
        pass
    else:
        print("PLAY " + current_room["game"]["id"].upper() + " to play " + current_room["game"]["name"] + ".")
    
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    
    if is_valid_exit((current_room["exits"]), direction) == True:
        if item_id not in inventory or item_keys not in inventory:
            print("You cannot leave the house without your house keys and student ID!")
            time.sleep(1)
        else:
            current_room = move(current_room["exits"], direction)
    elif is_valid_exit((current_room["exits"]), direction) == False:
        print("This doesn't make sense.")

    return current_room


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    item_taken = False
    
    global inventory
    if len(inventory) > 3:
        print("You cannot carry more than four items.")
    elif len(inventory) <= 5:
        for ite in current_room["items"]:
            if item_id == ite["id"]:
                inventory.append(ite)
                current_room["items"].remove(ite)
                print("You have taken " + ite["name"] + ".")
                item_taken = True
    if item_taken == False:
        print("This doesn't make sense.")
    
    item_taken = False
    time.sleep(1) # 3
    

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    
    item_dropped = False
    
    global inventory
    
    for ite in inventory:
        if item_id == ite["id"]:
            current_room["items"].append(ite)
            inventory.remove(ite)
            print("You have dropped " + ite["name"] + " at " + current_room["name"] + ".")
            item_dropped = True
            time.sleep(1) # 3
            
    if item_dropped == False:
        print("This doesn't make sense.")
        
    item_taken = False
    time.sleep(1) # 3
    
            
def execute_give(item_id):
    """This function takes an item_id as an argument and transfers this item from the
    player's inventory to the character who is in the current room that the
    player is in. However, if there is no such item in the inventory, this
    function prints "You don't have that in your inventory."
    """
    
    global inventory
    for ite in inventory:
        if item_id == ite["id"]:
            current_room["character"]["items"].append(ite)
            inventory.remove(ite)
            print("You have given " + ite["name"] + " to " + current_room["character"]["id"] + ".")
            time.sleep(1) # 3


def execute_explain(item_id):
    """This function takes an item_id as an argument and prints the description
    of the item in the inventory. However, if there is no such item in the
    inventory, this function prints "This item is not in your inventory."
    """
    
    global inventory
    for ite in inventory:
        if item_id == ite["id"]:
            print(ite["description"])
            time.sleep(1) # 15
            

def execute_play(game_id):
    """This function takes the name of a mini-game and then calls it. The game
    is then played by the player, if the player loses the mini-game, the player
    must "have a drink", which is implemented by a counter. If the player wins
    the mini-game, then the player doesn't incur any "drinking" penalties, i.e.
    the counter remains the same.
    """
    
    global alcoholCounter
    global winCounter
    
    if game_id == "rps": # RPS works fine
        if current_room == rooms["Tiger Tiger"]:
            alc, win = rps()
            if alc == True and win == False:
                alcoholCounter += 1
            elif alc == False and win == True:
                winCounter += 1            
        else:
            print("You cannot play that game here.")
            
    elif game_id == "hangman": # Problem! Hangman won't seem to reset when you play it again!
        if current_room == rooms["Students Union"]:
            alcFromHangman = exec_hangman()
            if alcFromHangman < 6:
                winCounter += 1
            alcoholCounter += alcFromHangman
        else:
            print("You cannot play that game here.")
            
    elif game_id == "fetch": # Works fine.
        if current_room == rooms["Retros"]:
            fetch()
        else:
            print("You cannot play that game here.")
            
    elif game_id == "riddle": # Works fine.
        if current_room == rooms["Pryzm"]:
            riddleNumber = random.randint(1, 6)
            if (riddleNumber == 1):
                alcFromRiddle, winFromRiddle = riddle_one()
                if (alcFromRiddle == True and winFromRiddle == False):
                    alcoholCounter += 1
                else:
                    winCounter += 1
            if (riddleNumber == 2):
                alcFromRiddle, winFromRiddle = riddle_two()
                if (alcFromRiddle == True and winFromRiddle == False):
                    alcoholCounter += 1
                else:
                    winCounter += 1
            if (riddleNumber == 3):
                alcFromRiddle, winFromRiddle = riddle_three()
                if (alcFromRiddle == True and winFromRiddle == False):
                    alcoholCounter += 1
                else:
                    winCounter += 1
            if (riddleNumber == 4):
                alcFromRiddle, winFromRiddle = riddle_four()
                if (alcFromRiddle == True and winFromRiddle == False):
                    alcoholCounter += 1
                else:
                    winCounter += 1
            if (riddleNumber == 5):
                alcFromRiddle, winFromRiddle = riddle_five()
                if (alcFromRiddle == True and winFromRiddle == False):
                    alcoholCounter += 1
                else:
                    winCounter += 1
        else:
            print("You cannot play that game here.")
            
    elif game_id == "numberguesser": # Works fine.
        if current_room == rooms["Glam"]:
            pass
            alcoholCounter += number_guesser()
        else:
            print("You cannot play that game here.")
            
    elif game_id == "blackjack": # Untested
        if current_room == rooms["Live Lounge"]:
            pass
            alcoholCounter += blackjack()
        else:
            print("You cannot play that game here.")
            
    elif game_id == "mastermind": # Works fine.
        if current_room == rooms["Unse Unse Unse"]:
            alcoholCounter += mastermind()
            winCounter += 1
        else:
            print("You cannot play that game here.")
    
    else:
        print("This doesn't make sense.")
    
    print("Overall, you have consumed " + str(alcoholCounter) + " units of alcohol.")
    print("Overall, you have won the mini-games " + str(winCounter) + " times.")
    time.sleep(3)


def fetch():
    
    global winCounter
    
    if item_scarf in current_room["character"]["items"]:
        print("You found it! Oh, thank you very much!")
        print("Gigi goes back to the dance floor.")
        winCounter += 1
        
    else:
        print("Gigi walks over to you. He says he's on a pub crawl too and he's lost his rainbow scarf! He wants you to find it.")
        print("Objective: Find the rainbow scarf and bring it to Gigi.")
        print("When you find the scarf, return to Retros and type GIVE SCARF.")
        print("When that's done, type PLAY FETCH again to complete the quest.")


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
            
    elif command[0] == "explain":
        if len(command) > 1:
            execute_explain(command[1])
        else:
            print("Explain what?")
            
    elif command[0] == "give":
        if len(command) > 1:
            execute_give(command[1])
        else:
            print("Give what?")
            
    elif command[0] == "play":
        if len(command) > 1:
            execute_play(command[1])
        else:
            print("Play what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():
    os.system("color 02")
    print("WELCOME TO...")
    print(" _____________________________________________________________________________________________________________________________")
    print("|  _____   _____   _____        _____       ___  ___       ___   _____   _   _   _____   _____        _____   _____    _____  |")
    print("| /  ___| | ____| |_   _|      /  ___/     /   |/   |     /   | /  ___/ | | | | | ____| |  _  \      |  _  \ |  _  \  /  _  \ |")
    print("| | |     | |__     | |        | |___     / /|   /| |    / /| | | |___  | |_| | | |__   | | | |      | |_| | | |_| |  | | | | |") 
    print("| | |  _  |  __|    | |        \___  \   / / |__/ | |   / / | | \___  \ |  _  | |  __|  | | | |      |  _  { |  _  /  | | | | |")
    print("| | |_| | | |___    | |         ___| |  / /       | |  / /  | |  ___| | | | | | | |___  | |_| |      | |_| | | | \ \  | |_| | |")
    print("| \_____/ |_____|   |_|        /_____/ /_/        |_| /_/   |_| /_____/ |_| |_| |_____| |_____/      |_____/ |_|  \_\ \_____/ |")
    print("|_____________________________________________________________________________________________________________________________|")
    print("")
    print("Go out on a pub crawl, play some mini-games and try not to get wasted!")
    print("RULES and OBJECTIVES")
    print("1. You can only carry up to four items at any time.")
    print("2. Play some of the mini-games in each of the 7 areas.")
    print("3. Win a combination of mini-games at least 10 times.")
    print("   For example, you could win hangman 4 times and each of the other mini-games once to win the main game.")
    print("4. If you lose a mini-game, then you have to 'have a drink' and gain a penalty in units of alcohol consumed.")
    print("   Different mini-games have different penalties, so think carefully before you decide which mini-game to play.")
    print("5. Incur too many drinking penalties, and you will lose the main game.")
    
    while True:
        print("Please select the difficulty level. Type: EASY, MEDIUM or HARD.")
        print("Beware: the harder the difficulty, the less alcohol you will be able to consume before you pass out, and the more mini-games you will have to win.")
        difficulty = input("> ")
        difficulty = normalise_input(difficulty)
    
        if difficulty == "easy" or "medium" or "hard":
            break
        else:
            print("that doesn't make sense")
    
    # Main game loop
    while True:
        
        if difficulty == "easy":
            if alcoholCounter < 40 and winCounter >= 5:
                print("Congratulations! You've managed to win all of the mini-games and you're not too drunk either! Thanks for playing!")
                break
            elif alcoholCounter >= 40:
                print("Oh dear, you're feeling a bit faint, you're gonna.... you're.....")
                time.sleep(10)
                print("You've passed out. GAME OVER! Thanks for playing!")
                break
        
        if difficulty == "medium":
            if alcoholCounter < 25 and winCounter >= 6:
                print("Congratulations! You've managed to win all of the mini-games and you're not too drunk either! Thanks for playing!")
                break
            elif alcoholCounter >= 25:
                print("Oh dear, you're feeling a bit faint, you're gonna.... you're.....")
                time.sleep(10)
                print("You've passed out. GAME OVER! Thanks for playing!")
                break
                
        if difficulty == "hard":
            if alcoholCounter < 10 and winCounter >= 7:
                print("Congratulations! You've managed to win all of the mini-games and you're not too drunk either! Thanks for playing!")
                break
            elif alcoholCounter >= 10:
                print("Oh dear, you're feeling a bit faint, you're gonna.... you're.....")
                time.sleep(10)
                print("You've passed out. GAME OVER! Thanks for playing!")
                break
                
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player what to do
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

