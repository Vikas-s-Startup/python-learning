import random

def generate_random_list():
    random_list = []
    total = 0
    while total < 10:
        n = random.randint(1, 1000)
        if n not in random_list:
            random_list.append(n)
            total += 1
    return random_list

def selection_sort(input_list):
    for e in range(0, len(input_list)):
        smallest_now = min(input_list[e:])
        smallest_now_index = input_list.index(smallest_now)
        input_list[e], input_list[smallest_now_index] = input_list[smallest_now_index], input_list[e]
    return input_list

list_to_sort = generate_random_list()

print(f"Original List is {list_to_sort}")

sorted_list = selection_sort(list_to_sort)

print(f"Sorted List using Selection Sort is {sorted_list}")