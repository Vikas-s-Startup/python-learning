from random import randint


def printMatrix(n):
    for i in range(1, n+1):
        for j in range(1, n + 1):
            print(chr(randint(97, 124)), end = " ")
        print()

printMatrix(10)