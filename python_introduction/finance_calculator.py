monthly_income = int(input("Enter your monthly income: " ))
monthly_expenses = int(input("Enter your monthly expenses: " ))
monthly_savings = monthly_income - monthly_expenses

Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(monthly_savings)
print("projected savings after one year, with interest, is:", Projected_Savings)