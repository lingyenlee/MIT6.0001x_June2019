#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 08:27:25 2019

@author: apple
Using Bisection Search to Make the Program Faster
"""

balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0

#set tolerance to 0.01
tolerance = 0.01
#save balance to a new variable
newbalance = balance
#set low bound to One-twelfth of the original balance
lowerBound = newbalance/12
#set upper bound  good upper bound to one-twelfth of the balance, 
#after having its interest compounded monthly for an entire year.
rate = (1+monthlyInterestRate)**12
upperBound = (newbalance*rate)/12.0
#take average of low and upper bound to be the guess
monthlyPayment = (upperBound+lowerBound)/2
#initialize month to 0
month = 0

print("new balance", newbalance)
print("low",round(lowerBound,2))
print("upper", round(upperBound,2))
print("monthlyPayment", round(monthlyPayment,2))

#while the balance is not within the tolerance range
while (abs(newbalance)) > tolerance:
#    reset balance to original value
    newbalance = balance
#    iterate through the months
    for month in range(0,12):
        month += 1
        print("month", month)
    
        monthlyUnpaidBalance = newbalance - monthlyPayment
        print("monthlyUnpaidBalance", round(monthlyUnpaidBalance,2))
    
        newbalance = monthlyUnpaidBalance + monthlyUnpaidBalance*monthlyInterestRate
        print("new monthly Balance", round(newbalance,2))

#    if balance is overpaid, that is, guess is too high
    if newbalance < 0:
#        reset upperbound to guess
        upperBound = monthlyPayment
    else:
#        otherwise if balance is not paid, guess is too low
#        set low bound to guess
        lowerBound = monthlyPayment
#        get the new average or new guess
    monthlyPayment = (upperBound+lowerBound)/2
     
print("Lowest payment is", round(monthlyPayment,2))
