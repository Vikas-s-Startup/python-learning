import math
n = 1
largest=0

while math.pow(n, 3) < 12000:
    largest = n
    n += 1

print(largest)