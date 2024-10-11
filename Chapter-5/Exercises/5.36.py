# Rock Paper Scissors
import random



system_wins = 0
player_wins = 0

while system_wins != 2 or player_wins !=0:
    system_choice = random.randint(0,2)

    print("Debug System Choice: ", system_choice)

    user_choice = int(input("Enter Scissor (0) or Rock(1) or Paper (2): "))
    default_statement = f", because Computer is {system_choice} and User is {user_choice}"

    if system_choice == 0 and user_choice == 0:
        print(f"It's a Draw {default_statement}")
    elif system_choice == 0 and user_choice == 1:
        print(f"User Wins {default_statement}")
        player_wins +=1
    elif system_choice == 0 and user_choice == 2:
        print(f"System Wins {default_statement}")
        system_wins += 1
    elif system_choice == 1 and user_choice == 0:
        print(f"System Wins {default_statement}")
    elif system_choice == 1 and user_choice == 1:
        print(f"It's a Draw {default_statement}")
    elif system_choice == 1 and user_choice == 2:
        print(f"User Wins {default_statement}")
        player_wins += 1
    elif system_choice == 2 and user_choice == 0:
        print(f"System Wins {default_statement}")
        system_wins += 1
    elif system_choice == 2 and user_choice == 1:
        print(f"User Wins {default_statement}")
        player_wins += 1
    elif system_choice == 2 and user_choice == 2:
        print(f"It's a Draw {default_statement}")
    else:
        print("Nothing")

print(f"Game Ends because System won {system_wins} and User Won {player_wins}")