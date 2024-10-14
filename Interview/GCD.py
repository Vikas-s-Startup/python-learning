# a1 = int(input("Enter a number: "))
# a2 = int(input("Enter a number: "))


def get_gcd(n1, n2):
    gcd = 1
    temp = min(n1, n2)

    for i in range(1, temp+1):
        if n1 % i ==0 and n2 % i == 0:
            gcd = i
    return gcd
