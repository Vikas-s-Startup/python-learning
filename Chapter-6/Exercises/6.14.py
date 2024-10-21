import math

def estimatePi(n):
    pi = 0
    for i in range(n):
        # Alternate adding and subtracting terms using (-1)**i
        pi += ((-1) ** i) / (2 * i + 1)
    return 4 * pi


for j in range(1, 1001, 100):
    print(j, estimatePi(j))