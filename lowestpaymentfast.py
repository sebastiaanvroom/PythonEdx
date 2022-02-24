init_balance = balance
monthlyInterestRate = annualInterestRate/12
lower = init_balance/12
upper = (init_balance * (1 + monthlyInterestRate)**12)/12.0
increment = 0.03

while abs(balance) > increment:
    monthlyPaymentRate = (upper + lower)/2
    balance = init_balance
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > increment:
        lower = monthlyPaymentRate
    elif balance < -increment:
        upper = monthlyPaymentRate
    else:
        break
print('Lowest Payment:', round(monthlyPaymentRate, 2))