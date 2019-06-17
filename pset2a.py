#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:22:34 2019

@author: apple
"""
#
#def calBal(balance, annualInterestRate, monthlyPaymentRate, month):
#    monthlyIntRate = annualInterestRate/12.0
#    minMonthlyPayment = monthlyPaymentRate * balance
#    monthlyUnpaidBal = balance - minMonthlyPayment
#    updatedBal = monthlyUnpaidBal + monthlyUnpaidBal*monthlyIntRate
#        
#    if month >= 12:
#        print("Remaining balace:", round(updatedBal,2))
#        return round(updatedBal, 2)
#    else: 
#        
#        print("Month", month, "Remaining balance:", round(updatedBal,2))
#        month += 1
#        return calBal(round(updatedBal,2), annualInterestRate, monthlyPaymentRate, month)
#
#calBal(42, 0.2, 0.04, 1)
#monthlyIntRate = annualInterestRate/12.0
#minMonthlyPayment = monthlyPaymentRate * balance
#monthlyUnpaidBal = balance - minMonthlyPayment

#pset 2a
#balance = 42
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
#
#month = 0
#
#while month < 12:
#    month += 1
#    monthlyIntRate = annualInterestRate/12.0
#    minMonthlyPayment = monthlyPaymentRate * balance
#    monthlyUnpaidBal = balance - minMonthlyPayment
#    updatedBal =  monthlyUnpaidBal + monthlyUnpaidBal*monthlyIntRate
#    balance = updatedBal
#
#print("Remaining balance:",round(updatedBal,2) )

#pset 2b
balance = 3329
annualInterestRate = 0.2
fixedPayment = 0

while balance > 0:
    fixedPayment += 10
    monthlyIntRate = annualInterestRate/12.0
    monthlyUnpaidBal = balance - fixedPayment
    updatedBal =  monthlyUnpaidBal + monthlyUnpaidBal*monthlyIntRate
    balance = updatedBal
    print("balance is", round(balance,1))
    print("payment is", fixedPayment)
    
    
print("Lowest Payment", fixedPayment)

    









    