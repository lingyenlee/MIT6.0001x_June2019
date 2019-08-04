#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 17:18:13 2019

@author: apple
write a program that calculates the minimum fixed monthly 
payment needed in order pay off a credit card balance 
within 12 months
The monthly payment must be a multiple of $10 and is 
the same for all months.
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = 
(Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

#pset 2b

balance = 1000
annualInterestRate = 0.2

#initialize monthly fixed payment to 10
monthlyPayment = 10
#store balance to a new variable
newbalance = balance
#initialize month to 0
monthlyIntRate = annualInterestRate/12.0
month = 0

#while balance is still outstanding, iterate 
while newbalance > 0:

    #iterate thru 12 months while the balance still remaining
    for month in range(0,12):
        #increment month by 1
        month += 1
        print("month", month)
        
        #calculate unpaid balance        
        monthlyUnpaidBal = newbalance - monthlyPayment
        print("monthly unpaid bal", round(monthlyUnpaidBal,2))
        
        #calculate updated balance       
        newbalance =  monthlyUnpaidBal + monthlyUnpaidBal*monthlyIntRate
        print("new balance is", round(newbalance,1))
    
    # if balance still left unpaid, increase monthly payment by 10 and repeat         
    if newbalance > 0:
         #increment fixed payment by 10
         monthlyPayment += 10
         print("monthly payment", monthlyPayment)
   
    #if negative, then payment is the lowest payment needed     
    else:
        break
    
    #reset newbalance to initial balance
    newbalance = balance
    print("newbal", newbalance)
        
 
print("payment is", monthlyPayment)
    
 