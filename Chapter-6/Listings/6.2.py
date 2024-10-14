# print grades for the score
def printGrade(score):
    if score >=90.0:
        print('A')
        return
    elif 80.0 <= score < 90.0:
        print('B')
    elif 70.0 <= score < 80.0:
        print('C')
    elif 60.0 <= score < 70.0:
        print('D')
    else:
        print('F')

marks = float(input("Enter a score: "))
print("The grade is ", end = "")
printGrade(marks)