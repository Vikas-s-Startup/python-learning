import time

# def getSecondsSinceEpoch():
#     return int(time.time())
# secondsSinceEpoch = getSecondsSinceEpoch()
# minutesSinceEpoch = secondsSinceEpoch / 60
# hoursSinceEpoch = minutesSinceEpoch / 60
# daysSinceEpoch = hoursSinceEpoch / 24
# print(f"{secondsSinceEpoch} Seconds Since \n{minutesSinceEpoch} Minutes Since \n{hoursSinceEpoch} Hours Since \n{daysSinceEpoch} Days Since Epoch")
# today = (int(daysSinceEpoch) + 4) % 7
# print(days_of_week[today])

# epoch = " January 1, 1970, 00:00:00 (UTC) "


days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months_of_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]


def is_leapYear(y):
    if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
        return True
    else:
        return False

end_year = 1991

# Find first day of end_year
total_days = 0
for year in range(1970, end_year):
    if is_leapYear(year):
        total_days += 366
    else:
        total_days += 365
s = (total_days + 4) % 7
print(days_of_week[s])
