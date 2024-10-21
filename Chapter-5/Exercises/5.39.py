base_salary = 5000
target_commission = 30000 - base_salary
sales = 0
temp_commission = 0


if sales <=5000:
    sales += 5000
    temp_commission = 5000 * 0.08
    target_commission -= temp_commission
if sales <=10000:
    sales += 5000
    temp_commission = 5000 * 0.1
    target_commission -= temp_commission
remainder_sales = target_commission / 0.12

total_sales = remainder_sales + sales

print(total_sales)

# Initialize variables
# base_salary = 5000
# total_income_goal = 30000
# sales = 0
# commission = 0
#
# # Loop until the total income reaches or exceeds the goal
# while (base_salary + commission) < total_income_goal:
#     sales += 1  # Increment sales by 1 unit
#
#     # Calculate commission based on sales amount
#     if sales <= 5000:
#         commission = sales * 0.08  # 8% for sales up to $5,000
#     elif sales <= 10000:
#         # 8% for the first $5,000, 10% for the remaining up to $10,000
#         commission = (5000 * 0.08) + (sales - 5000) * 0.10
#     else:
#         # 8% for the first $5,000, 10% for the next $5,000, 12% for the rest
#         commission = (5000 * 0.08) + (5000 * 0.10) + (sales - 10000) * 0.12
#
# # Output the minimum sales needed
# print(f"The minimum sales required to earn $30,000 is: ${sales:.2f}")


