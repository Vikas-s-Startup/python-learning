import random

def generate_random_list():
    random_list = []
    total = 0
    while total < 500:
        n = random.randint(1, 999)
        if n not in random_list:
            random_list.append(n)
            total += 1
    return random_list

unsorted_list = generate_random_list()

print(f" Unsorted List: {unsorted_list}")

def bubble_sort(sorted_list):
    for x in range(len(sorted_list), 0, -1):
        for y in range(0, x-1):
            if sorted_list[y] > sorted_list[y+1]:
                sorted_list[y] , sorted_list[y+1] = sorted_list[y+1], sorted_list[y]
    return sorted_list

sorted_output = bubble_sort(unsorted_list)

print(f" Sorted List: {sorted_output}")
