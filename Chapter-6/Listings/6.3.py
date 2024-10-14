# print grades for the score
def printGrade(score):
    if score >=90.0:
        return 'A'
    elif 80.0 <= score < 90.0:
        return 'B'
    elif 70.0 <= score < 80.0:
        return 'C'
    elif 60.0 <= score < 70.0:
        return 'D'
    else:
        return 'F'

marks = float(input("Enter a score: "))
print("The grade is ", printGrade(marks))
