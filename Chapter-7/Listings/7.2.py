import random

deck = list(range(0, 52))

random.shuffle(deck)

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks  = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

for i in range(4):
    suit = suits[deck[i] // 13]
    rank = ranks[deck[i] % 13]
    print("Card number", deck[i], "is", rank, "of", suit)