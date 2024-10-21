def sqrt(n):
    lastGuess = 1
    nextGuess = (lastGuess + (n / lastGuess)) / 2
    while abs(nextGuess - lastGuess) >= 0.0001:
        lastGuess = nextGuess
        nextGuess = (lastGuess + (n / lastGuess)) / 2
    return nextGuess

print(f"Square root of 9 is {sqrt(9)}")
