import time

total_seconds = int(time.time())

print(total_seconds)

current_seconds = total_seconds % 60
print(f"Seconds: {current_seconds}")

total_minutes = total_seconds / 60
current_minute = total_minutes % 60

print(f"Minutes: {current_minute}")
print(current_minute)

total_hours = total_minutes / 60
current_hour = total_hours % 24

print(f"Current Hour: {current_hour}")

#
# minutes = current_time // 60
# hours = minutes // 60
#
# print(f"{hours}:{minutes}:{remaining_seconds}")