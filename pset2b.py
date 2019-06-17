#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 17:18:13 2019

@author: apple
"""

#pset 2b
balance = 3926
annualInterestRate = 0.2
monthlyPayment = 0
newbalance = balance

while newbalance > 0:
    monthlyPayment += 10
    print("monthly payment", monthlyPayment)
    newbalance = balance
    month = 0

    while month < 12 and newbalance > 0:
        month += 1
        print("month", month)
        
        monthlyUnpaidBal = newbalance - monthlyPayment
        print("monthly unpaid bal", round(monthlyUnpaidBal,2))
        monthlyIntRate = annualInterestRate/12.0
        newbalance =  monthlyUnpaidBal + monthlyUnpaidBal*monthlyIntRate
        print("updated balance is", round(newbalance,1))
        
    newbalance = round(newbalance,2)
        
 
print("payment is", monthlyPayment)
    
 