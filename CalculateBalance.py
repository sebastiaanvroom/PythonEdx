balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for x in range(12):
    balance = balance - (balance * monthlyPaymentRate) + ((balance - (balance * monthlyPaymentRate)) * (annualInterestRate/12))
    print('Remaining balance: ',  balance) 