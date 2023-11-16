annual_rate = 0.12
monthly_rate = annual_rate / 12

purchase_price = float(input("Enter the purchase price: "))

monthly_payment = 0.05 * (purchase_price - (0.10 * purchase_price))
month = 1
balance = purchase_price

print("Month   Starting Balance   Interest to Pay   Principal to Pay   Payment   Ending Balance")

while balance > 0:
    if monthly_payment > balance:
        monthly_payment = balance
        interest = 0
    else:
        interest = balance * monthly_rate
        principal = monthly_payment - interest
        remaining = balance - monthly_payment
        print(f"{month:<7}{balance:<20.2f}{interest:<20.2f}{principal:<20.2f}{monthly_payment:<20.2f}{remaining:<20.2f}")
        balance = remaining
        month += 1

