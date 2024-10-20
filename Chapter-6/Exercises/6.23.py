# milliseconds = int(input("Enter time in milliseconds"))
milliseconds = 1123241637

seconds = milliseconds/1000
remaining_seconds = seconds % 60
minutes = seconds/60
hours = minutes/60

print(f"{hours}:{minutes}:{remaining_seconds}")