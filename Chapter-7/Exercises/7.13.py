# input_integers = [int(x) for x in input("Enter a list of numbers: ").strip().split()]

input_integers = [25, 10]
gcd = 1

for i in range(1, min(input_integers)+1):
    if input_integers[0] % i == 0 and input_integers[1] % i == 0:
        gcd = i

print(gcd)