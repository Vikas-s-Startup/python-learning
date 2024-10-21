import datetime

thisYear = datetime.date.today().year
userYear = int(input("Enter your birth year: "))

print(f"Your age is {thisYear-userYear}")