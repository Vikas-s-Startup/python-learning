


savings_per_month = int(input("Enter the amount to be saved for each month: "))
months_in_year = int(input("Enter the number of months: "))
interest_rate_per_year = int(input("Enter the rate of interest: "))
interest_rate_per_year = interest_rate_per_year/ 100
interest_per_month = 0.05/12



total_amount = 0

for month in range(1, months_in_year+1):
    total_amount = (total_amount + savings_per_month) * ( 1 + interest_per_month)

print(f"After the {months_in_year}th month, the account value is {total_amount}")
