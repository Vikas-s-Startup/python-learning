input_integers = [int(x) for x in input("Enter a list of numbers: ").strip().split()]

gcd = 1

for gcd in range(min(input_integers), 0, -1):
    if input_integers[0] % gcd == 0 and input_integers[1] % gcd == 0:
        print(f"GCD: {gcd}")
        break