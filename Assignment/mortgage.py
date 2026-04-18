'''
START

We are to calculate between principl amount, anual and payment duration

END

'''

principal_amount = float(input("Enter a principal amount: "))
anual_interest = float(input("Enter the annual interest rate: "))
payment_duration = int(input("Enter the duration in years: "))

monthly_rate = anual_interest / 100 / 12
total_months = payment_duration * 12

if monthly_rate == 0:
    monthly_payment = principal_amount / total_months
else:
    monthly_payment = principal_amount * monthly_rate * (1 + monthly_rate) ** total_months / ((1 + monthly_rate) ** total_months - 1)

print("Monthly payment:", round(monthly_payment, 2))
