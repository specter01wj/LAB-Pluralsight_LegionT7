# Get the loan details with input validation
while True:
    try:
        money_owed = float(input("How much money do you owe, in dollars?\n"))
        apr = float(input("What is the annual percentage rate of the loan?\n"))
        payment = float(input("How much will you pay off each month in dollars?\n"))
        months = int(input("How many months do you want to see the results for?\n"))

        if money_owed <= 0 or apr < 0 or payment <= 0 or months <= 0:
            print("Please enter positive values for all inputs.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Convert APR to monthly interest rate
monthly_rate = apr / 100 / 12

# Check if payment is too low
if payment <= money_owed * monthly_rate:
    print("Your monthly payment is too low and will not cover the interest. The debt will increase indefinitely.")
else:
    # Simulate payments
    for i in range(1, months + 1):
        # Calculate interest for the month
        interest_paid = round(money_owed * monthly_rate, 2)
        money_owed += interest_paid

        # Check if this is the last payment
        if money_owed - payment < 0:
            print(f"The last payment is ${money_owed:.2f}")
            print(f"You paid off the loan in {i} months.")
            break

        # Deduct the payment
        money_owed -= payment

        # Print the monthly update
        print(f"Month {i}: Paid ${payment:.2f}, of which ${interest_paid:.2f} was interest. Now you owe ${money_owed:.2f}")

