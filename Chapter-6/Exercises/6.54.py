# Non-Space Counter


user_input = "Hello World! I am Rick."

nonSpaceCharacters = 0

for char in user_input:
    if char != " ":
        nonSpaceCharacters += 1

print(nonSpaceCharacters)