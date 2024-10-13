user_input = int(input("Enter a number greater than 0: "))
prime_factors = []

for i in range(1, user_input+1):
    if user_input % i == 0:
        prime_factors.append(i)

print(f"Prime Factors of {user_input} are {prime_factors}")