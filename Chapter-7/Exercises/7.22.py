import random

all_cards = ["D" + "-" + str(x) for x in range(1, 14)] + ["H" + "-" + str(x) for x in range(1, 14)] + [
    "S" + "-" + str(x) for x in range(1, 14)] + ["C" + "-" + str(x) for x in range(1, 14)]

random.shuffle(all_cards)

picked_cards = []
unique_cards = []
total_picks = 0

while len(unique_cards) < 4:
    picked_card = random.randint(1, len(all_cards))
    picked_cards.append(all_cards[picked_card - 1])
    total_picks += 1
    picked_deck = all_cards[picked_card - 1].split("-")[0]
    if picked_deck not in unique_cards:
        unique_cards.append(picked_deck)

print(f"Picked Cards: {picked_cards}")
print(f"Total Picks: {total_picks}, until card from each deck has been picked")
print(unique_cards)
