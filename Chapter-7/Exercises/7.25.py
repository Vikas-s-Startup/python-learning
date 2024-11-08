import time
from turtledemo.penrose import start

deckOne = [x for x in range(1, 14)]
deckTwo = [x for x in range(1, 14)]
deckThree = [x for x in range(1, 14)]
deckFour = [x for x in range(1, 14)]

combinations = []
start_time = time.time()
for deckOneCard in deckOne:
    for deckTwoCard in deckTwo:
        for deckThreeCard in deckThree:
            for deckFourCard in deckFour:
                if deckOneCard + deckTwoCard + deckThreeCard + deckFourCard == 24:
                    combinations.append([deckOneCard,deckTwoCard,deckThreeCard,deckFourCard])
end_time = time.time() - start_time

print("Total Time taken is ", end_time)
for combination in combinations:
    print(combination)