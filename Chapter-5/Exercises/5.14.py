import math
n = 1
largest=0

while math.pow(n, 3) - math.pow(n, 2) < 1000:
    largest = n
    n += 1

print(largest)