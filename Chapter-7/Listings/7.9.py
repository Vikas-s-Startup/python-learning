# Selection Sort

def selectionSort(lst):
    for index in range(len(lst) - 1):
        # Find the minimum in the remaining list
        currentMinIndex = index + lst[index:].index(min(lst[index:]))
        # Swap only if the minimum is not already at the current position
        if currentMinIndex != index:
            lst[currentMinIndex], lst[index] = lst[index], lst[currentMinIndex]
    print(lst)

def main():
    lst = [-2, 4.5, 5, 1, 2, -3.3]
    selectionSort(lst)

main()
