expenses = [10.50, 8, 5, 15, 20, 5, 3]

sum1 = 0

for expense in expenses:
    sum1 += expense

print('sum = $', sum1, sep = '')

total = sum(expenses)

print('You spent $', total, sep = '')

