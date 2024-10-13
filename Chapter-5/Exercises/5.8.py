import math

print("Real Number              Cube Root")
for i in range(0, 52, 4):
    print(f"{i}          {math.pow(i, 1/3)}")