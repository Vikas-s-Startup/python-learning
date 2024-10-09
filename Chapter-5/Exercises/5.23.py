import math

principal = 10000.65
annual_interest_rate = 0.05
loan_years = 1
loan_period = loan_years * 12
monthly_interest_rate = annual_interest_rate / 12  # Correct monthly interest rate
per_month_payment = (principal * monthly_interest_rate) / (1 - math.pow((1 + monthly_interest_rate), -loan_period))
total_payment_over_years = loan_period * per_month_payment
print(f"per_month_payment = {per_month_payment}")
print(f"total_payment_over_years = {total_payment_over_years}")

print("Non-sense")