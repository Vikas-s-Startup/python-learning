def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1

    while high >= low:
        mid = (high + low) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid  # return the index of the found element
        else:
            low = mid + 1

    return -1  # return -1 if the element is not found

def main():
    lst = [-3, 1, 2, 4, 9, 23]
    print(binarySearch(lst, 2))  # This will now print the index of 2, which is 2.

main()