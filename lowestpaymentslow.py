balance = 500
annualInterestRate = 0.5

Monthly = 0
balance2 = balance
monthlyInterestRate = annualInterestRate/12

while balance > 0:
    for i in range(12):
        balance = balance - Monthly + ((balance - Monthly) * monthlyInterestRate)
    if balance > 0:
        Monthly += 10
        balance = balance2
    elif balance <= 0:
        break
print('Lowest Payment:', Monthly)