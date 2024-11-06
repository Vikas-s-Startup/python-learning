from logging import currentframe


def selectionSort(lst):
    for i in range(len(lst)-1):
        currentMin = min(lst[i:])
        currentMinIndex = i + lst[i:].index(currentMin)
        if currentMinIndex != i:
            lst[currentMinIndex], lst[i] = lst[i], currentMin
    return lst


list1 = [1,3,5,5,7,9]
list2 = [2,4,6,8,10]

list3 = list1 + list2

final_sorted_list = selectionSort(list3)

print(list3)