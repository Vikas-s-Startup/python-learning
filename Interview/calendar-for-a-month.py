import time

# epoch = " January 1, 1970, 00:00:00 (UTC) "

def is_leapYear(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def getSecondsSinceEpoch():
    return int(time.time())

secondsSinceEpoch = getSecondsSinceEpoch()
minutesSinceEpoch = secondsSinceEpoch / 60
hoursSinceEpoch = minutesSinceEpoch / 60
daysSinceEpoch = hoursSinceEpoch / 24

print(f"{secondsSinceEpoch} Seconds Since \n{minutesSinceEpoch} Minutes Since \n{hoursSinceEpoch} Hours Since \n{daysSinceEpoch} Days Since Epoch")