def computeValue(x0,y0, x1, y1, x2, y2):
    return ((x1-x0) * (y2-y0)) - ((x2-x0) * (y1-y0))

def leftOfTheLine(x0,y0, x1, y1, x2, y2):
    return True if computeValue(x0,y0, x1, y1, x2, y2) > 0 else False

def RightOfTheLine(x0, y0, x1, y1, x2, y2):
    return True if computeValue(x0,y0, x1, y1, x2, y2) < 0 else False

def OnTheLine(x0, y0, x1, y1, x2, y2):
    return True if computeValue(x0,y0, x1, y1, x2, y2) == 0 else False

X0  = float(input("Enter the x-coordinate of point 0: "))
Y0  = float(input("Enter the x-coordinate of point 0: "))
X1  = float(input("Enter the x-coordinate of point 1: "))
Y1  = float(input("Enter the x-coordinate of point 1: "))
X2  = float(input("Enter the x-coordinate of point 2: "))
Y2  = float(input("Enter the x-coordinate of point 2: "))



if leftOfTheLine(X0, Y0, X1, Y1, X2, Y2):
    print(f"({X2},{Y2}) is on the left side of the line from ({X0},{Y0}) to ({X1},{Y1})")

if RightOfTheLine(X0, Y0, X1, Y1, X2, Y2):
    print(f"({X2},{Y2}) is on the right side of the line from ({X0},{Y0}) to ({X1},{Y1})")

if OnTheLine(X0, Y0, X1, Y1, X2, Y2):
    print(f"({X2},{Y2}) is on the line from ({X0},{Y0}) to ({X1},{Y1})")