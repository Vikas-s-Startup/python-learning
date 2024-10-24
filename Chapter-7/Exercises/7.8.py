def indexOfSmallestElementV2(lst: list[int]) -> int:
    temp_list = [x for x in lst]
    temp_list.sort()
    return int(lst.index(temp_list[0]))


def indexOfSmallestElementV1(lst: list[int]) -> int:
    smallest_index = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[smallest_index]:
            smallest_index = i
    return smallest_index

def main():
    user_input = input("Enter a list of integers: ").strip().split(" ")
    user_input = [int(x) for x in user_input]
    smallestIndex = indexOfSmallestElementV1(user_input)
    print(f"Index of the smallest element in the list is {smallestIndex}")

main()