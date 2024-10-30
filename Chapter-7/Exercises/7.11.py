import random

# Get input from the user
user_input_string = "Hello world how are you doing"

# Convert the string into a list (since strings are immutable)
char_list = list(user_input_string)

# Implement Fisher-Yates shuffle
for i in range(len(char_list) - 1, 0, -1):
    # Pick a random index from 0 to i
    j = random.randint(0, i)
    # Swap characters at index i and j
    char_list[i], char_list[j] = char_list[j], char_list[i]

# Convert the list back into a string
shuffled_string = ''.join(char_list)

# Output the shuffled string
print("Shuffled string:", shuffled_string)
