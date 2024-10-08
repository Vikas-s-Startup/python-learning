import math
print("Degree Cos Tan")

for degree in range(0, 380, 20):
    print(f"{degree}     {math.cos(degree)}     {math.tan(degree)}")