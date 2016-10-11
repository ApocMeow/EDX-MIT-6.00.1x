# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 23:00:32 2016

@author: james.hussey
"""

# the outstanding balance on the credit card
balance = 320000

# annual interest rate as a decimal
annualInterestRate = 0.2

# monthly interest rate as a decimal
monthlyInterestRate = annualInterestRate / 12

# lower boundary for bisection search
lowerBound = (balance / 12)

# upper boundary for bisection search
upperBound = (balance * ((1 + monthlyInterestRate) ** 12)) / 12

# lowest monthly payment necessary to pay off balance in 12 months
lowestPayment = (lowerBound + upperBound) / 2

# holding place for temporary balance so as not to overwrite starting balance
tempBalance = balance

while abs(tempBalance) > 0.01:
    tempBalance = balance
    lowestPayment = (lowerBound + upperBound) / 2
    for m in range(12):
       tempBalance -= lowestPayment
       tempBalance += monthlyInterestRate * tempBalance
   
    if tempBalance > 0:
        lowerBound = lowestPayment
    else:
        upperBound = lowestPayment       

# final print statement to 2 decimal places
print("Lowest Payment: %.2f" % (lowestPayment))