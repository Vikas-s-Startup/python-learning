import random
number_of_balls = int(input("Please enter the number of balls: "))
number_of_slots = int(input("Please enter the number of slots: "))

SLOTS_WITH_BALLS = [0 for x in range(1, number_of_slots+1)]
BALL_PATHS = []

for ball in range(1, number_of_balls+1):
    BALL_PATH = ""
    for level in range(1, number_of_slots+1):
        choice = random.choice(["L", "R"])
        BALL_PATH += choice
    count_L = BALL_PATH.count('L')
    count_R = BALL_PATH.count('R')
    SLOTS_WITH_BALLS[count_R] += 1
    BALL_PATHS.append(BALL_PATH)

print(BALL_PATHS)
print(SLOTS_WITH_BALLS)
