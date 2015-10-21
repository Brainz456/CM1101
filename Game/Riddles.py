

def riddle_one():
    count = 0
    while (count < 3):
        ans = input("""What has roots as nobody sees,
                    is taller than trees Up, up, up it goes,
                    and yet never grows?""")
        if ans in ['Mountain', 'mountain']:
            print("Success")
            return [False, True]
            break
        else:
            print("please try again")
            count = count + 1
    if (count >= 3):
        print("You have failed miserably")
        return [True, False]


def riddle_two():
    count = 0
    while (count < 3):
        ans = input("""Voiceless it cries,
Wingless flutters,
Toothless bites,
Mouthless mutters.""")
        if ans in ['Wind', 'wind']:
            print("Success")
            return [False, True]
            break
        else:
            print("please try again")
            count = count + 1
    if (count >= 3):
        print("You have failed miserably")
        return [True, False]
            
def riddle_three():
    count = 0
    while (count < 3):
        ans = input("""It cannot be seen, cannot be felt,
Cannot be heard, cannot be smelt.
It lies behind stars and under hills,
And empty holes it fills.
It comes first and follows after,
Ends life, kills laughter.""")
        if ans in ['Dark', 'dark']:
            print("Success")
            return [False, True]
            break
        else:
            print("please try again")
            count = count + 1
    if (count >= 3):
        print("You have failed miserably")
        return [True, False]
            

def riddle_four():
    count = 0
    while (count < 3):
        ans = input("""Alive without breath,
As cold as death;
Never thirsty, ever drinking,
All in mail never clinking""")
        if ans in ['Fish', 'fish']:
            print("Success")
            return [False, True]
            break
        else:
            print("please try again")
            count = count + 1
    if (count >= 3):
        print("You have failed miserably")
        return [True, False]

def riddle_five():
    count = 0
    while (count < 3):
        ans = input("What have I got in my pocket?")
        if ans in ['Ring', 'ring']:
            print("Success")
            return [False, True]
            break
        else:
            print("please try again")
            count = count + 1
    if (count >= 3):
        print("You have failed miserably")
        return [True, False]