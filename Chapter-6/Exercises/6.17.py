def isValid(side1, side2, side3):
    return True if ((side1 + side2) > side3) else False

def area(side1, side2, side3):
    return side1 * side2 * side3


s1 = float(input("enter edge 1: "))
s2 = float(input("enter edge 2: "))
s3 = float(input("enter edge 3: "))

if isValid(s1, s2, s3):
    print(f"The provided sides {s1}, {s2}, {s3} are valid ")
    print(f"Area of sides {s1}, {s2}, {s3} is {area(s1, s2, s3)}")
else:
    print(f"The provided sides {s1}, {s2}, {s3} are NOT valid ")