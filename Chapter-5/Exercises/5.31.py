days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months_of_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def is_leap_year(year):
    year = int(year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# y = input("Enter a year: ")
# first_day = input("Enter the first day of the year: ")

y = 2005
first_day = 6

current_day = first_day

if is_leap_year(y):
    days_in_months[1] = 29

for month in range(12):
    print("\n",months_of_year[month], " ", y)
    print(f"First day of month {month + 1} is {days_of_week[int(current_day)]}")
    print("--------------------------")
    print("Sun Mon Tue Wed Thu Fri Sat")
    for space in range(current_day):
        print("    ", end="")
    for day in range(1, days_in_months[month]+1):
        print(f"{day:3}", end=" ")
        if (current_day + day) % 7 == 0:
            print()
    current_day = (current_day + days_in_months[month]) % 7
    print()
