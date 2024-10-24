input_marks = input("Enter a list of scores, separated by spaces: ")
input_marks = input_marks.split(" ")

A_count = B_count = C_count = D_count = F_count = 0

for marks in input_marks:
    if int(marks) >= 90:
        A_count +=1
    elif 80 <= int(marks) < 90:
        B_count +=1
    elif 70 <= int(marks) < 80:
        C_count +=1
    elif 60 <= int(marks) < 70:
        D_count +=1
    else:
        F_count += 1

print("Grade Frequencies:")
print(f"A: {A_count}")
print(f"B: {B_count}")
print(f"C: {C_count}")
print(f"D: {D_count}")
print(f"F: {F_count}")
