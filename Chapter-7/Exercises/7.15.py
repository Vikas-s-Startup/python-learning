input_integers = [int(x) for x in input("Enter a list of numbers: ").strip().split()]

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

list_is_even = True
for num in input_integers:
    if not is_even(num):
        list_is_even = False
        break

print(f"input list {input_integers} is {"odd" if not list_is_even else "even"}")