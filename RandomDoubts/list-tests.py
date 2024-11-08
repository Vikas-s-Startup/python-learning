import time

list1 = [1, 1, 2, 2, 4, 5, 6, 7, 7, 4, 3, 2, 3, 4, 6, 5, 4, 3, 6, 7, 7, 7, 8, 9, 7, 5, 4, 2, 6, 4, 4, 3, 2, 3, 2, 2]

start_time = time.perf_counter()

# Counting occurrences of 7 in list1
# count = 0
# for i in list1:
#     if i == 7:
#         count += 1
# print("Count of 7:", count)

print("Count of 7:", list1.count(7))

# Output the result and time taken
end_time = time.perf_counter()
print(f"Total Time Taken is: {(end_time - start_time) * 1000:.6f} milliseconds")


list1.sort()
print(list1)