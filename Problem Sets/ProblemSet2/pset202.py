# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 11:23:37 2016

@author: james.hussey
"""

balance = 3329
# the outstanding balance on the credit card

annualInterestRate = 0.2
# annual interest rate as a decimal

monthlyInterestRate = annualInterestRate / 12
# monthly interest rate as a decimal

lowestPayment = 0
# lowest monthly payment necessary to pay off balance in 12 months

tempBalance = balance
# holding place for temporary balance so as not to overwrite starting balance

# Function that calculates the balance at the end of a year
def yearEnd(balance, lowestPayment, monthlyInterestRate):
    tempBalance = balance
    for m in range(0,12):
       tempBalance -= lowestPayment
       tempBalance += monthlyInterestRate * tempBalance
    check(tempBalance, lowestPayment)

# Function that checks the condition that will end our loop
def check(tempBalance, lowestPayment):    
    if tempBalance >= 0:
        lowestPayment += 10
        yearEnd(balance, lowestPayment, monthlyInterestRate)
    else:
        # Final print statement
        print("Lowest Payment: %s" % (lowestPayment))

check(tempBalance, lowestPayment)