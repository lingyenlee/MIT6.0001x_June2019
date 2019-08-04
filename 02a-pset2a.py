#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:22:34 2019

@author: apple
"""

"""
Write a program to calculate the credit card balance after one year 
if a person only pays the minimum monthly payment required by the 
credit card company each month.
"""

balance = 42; 
annualInterestRate = 0.2; 
monthlyPaymentRate = 0.04

month = 0

#iterate through each month while less than 12
while month < 12:
#increment each month
    month += 1
#calculate monthly interest rate
    monthlyIntRate = annualInterestRate/12.0
#calculate monthly payment by monthly payment rate
    minMonthlyPayment = monthlyPaymentRate * balance
#calculate unpaid balance by substracting balance from monthly payment
    monthlyUnpaidBal = balance - minMonthlyPayment
#calculate updated balance by adding in interest to unpaid balance
    updatedBal =  monthlyUnpaidBal + monthlyUnpaidBal*monthlyIntRate
#store the updated balance to balance for recurring loops 
    balance = updatedBal

#print the balance at the end of the iteration
print("Remaining balance:",round(updatedBal,2) )
