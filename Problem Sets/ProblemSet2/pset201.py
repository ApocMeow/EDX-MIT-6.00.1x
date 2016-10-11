# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 09:59:59 2016

@author: james.hussey
"""

balance = 42
# balance - the outstanding balance on the credit card

annualInterestRate = 0.2
# annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate = 0.04
# monthlyPaymentRate - minimum monthly payment rate as a decimal

#def monthEnd(balance, annualInterestRate, monthlyPaymentRate):

for m in range(0,12):
        balance -= (balance * monthlyPaymentRate)
        balance += (annualInterestRate / 12) * balance
print(round(balance, 2))



























