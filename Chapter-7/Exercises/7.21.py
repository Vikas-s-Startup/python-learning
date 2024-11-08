students = 100
number_of_lockers = 100
lock_status = [False for _ in range(number_of_lockers)]
print(len(lock_status))

for student in range(1, students+1):
    for locker in range(student-1,number_of_lockers, student):
        if lock_status[locker]:
            lock_status[locker] = False
        else:
            lock_status[locker] = True
        # lock_status[locker] = not lock_status[locker]

print(lock_status)
print("Opened Locks are: ",lock_status.count(True))
print("Closed Locks are: ",lock_status.count(False))