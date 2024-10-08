n1 = int(10)
n2 = int(20)


# Greatest Common Divisor version 1
gcd = int(1)
k = int(2)

while k <= n1 and k <= n2:
    if n1 % k == 0 and n2 % k == 0:
        gcd = k
    k += 1
print(gcd)



# Greatest Common Divisor version 2
import math
gcd_new = 1
i = 1
for i in range(1, min(n1, n2) + 1):
    if n1 % i == 0 and n2 % i == 0:
        gcd_new = i

print(gcd_new)