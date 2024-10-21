from random import randint

sumOfDiceFaces = 0

while sumOfDiceFaces != 7:
    diceOne = randint(1, 6)
    diceTwo = randint(1, 6)

    sumOfDiceFaces = diceOne + diceTwo
    print(f"User Rolled {diceOne} + {diceTwo} = {sumOfDiceFaces}")
    point = 0
    if sumOfDiceFaces in [2,3,12]:
        print("User Looses")
    elif sumOfDiceFaces in [7, 11]:
        print("User Wins")
    elif sumOfDiceFaces in [4, 5, 6, 8, 9, 10]:
        point += 1