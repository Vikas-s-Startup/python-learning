# Predicting Future Tuition Fee

year = 0
tuition_fee = 10000
increase_every_year = 1.07
double_fee = 20000

while tuition_fee < 20000:
    year += 1
    tuition_fee = tuition_fee * 1.07
print(year)