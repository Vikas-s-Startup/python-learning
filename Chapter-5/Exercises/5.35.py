# Perfect number
import math
import time

start_time = time.time()
perfect_numbers = []

for i in range(1, 10001):
    # print(f"Checking {i}")
    divisors = []
    divisor_sum = 0
    for j in range(1, int(math.sqrt(i)) +1):
        if i % j == 0:
            divisor_sum += j

    if i == divisor_sum:
        perfect_numbers.append(i)

total_time = time.time() - start_time
print(f"Perfect numbers between 1 and 10,000 are {set(perfect_numbers)} and time taken to calculate is {total_time}")


# import time, math
# start_time = time.time()
#
# perfect_numbers = []
#
# for i in range(2, 10001):  # Start from 2, as 1 can't be a perfect number
#     divisor_sum = 1  # 1 is a divisor for all numbers, start the sum with 1
#     for j in range(2, int(math.sqrt(i)) + 1):  # Check divisors up to sqrt(i)
#         if i % j == 0:
#             divisor_sum += j
#             if j != i // j:  # Add the complementary divisor only if it's different
#                 divisor_sum += i // j
#     if i == divisor_sum:
#         perfect_numbers.append(i)
# total_time = time.time() - start_time
# print(f"Perfect numbers between 1 and 10,000 are {perfect_numbers} and time taken is {total_time}")
