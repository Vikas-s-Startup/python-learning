import math

i = 1
total_sum = 0
while i < 625:
    total_sum =+ (1/(math.pow(i, 0.5) + math.pow((i+1), 0.5)))
    i += 1

print(f"Total Sum is {total_sum}")