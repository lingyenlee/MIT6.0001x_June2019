#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:00:59 2019

@author: apple

The program works as follows: you (the user) thinks of an integer between 
0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you 
give it input - is its guess too high or too low? Using bisection search, 
the computer will guess the user's secret number!
"""

low = 0
high = 100
ans = int((low+high)/2)

#print("Please think of a number between 0 and 100!")
#
#while True:
#    print("Is your secret number " + str(ans) + "?")
#    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess if too low. Enter 'c' to indicate I guessed correctly.")
#    
#    if guess == "h":
#        high = ans
#    elif guess == "l":
#        low = ans
#    elif guess == "c":
#        print("Game over. Your secret number was " + str(ans) + ".")
#        break
#    else:
#        print("Sorry, I did not understand your input.")
#    
#    ans = int((low+high)/2)
#    
    
"""
Write an iterative function iterPower(base, exp) that calculates 
the exponential  baseexp  by simply using successive multiplication. 
For example, iterPower(base, exp) should compute  baseexp  by multiplying 
base times itself exp times. Write such a function below.
"""
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    while exp > 0:
        result = base * result
        exp -= 1
    return result

print(iterPower(1.02, 0))
print(iterPower(9.48, 10))


"""
Write a function recurPower(base, exp) which computes  baseexp  
by recursively calling itself to solve a smaller version of the 
same problem, and then multiplying the result by base to solve 
the initial problem.
"""
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)

print(recurPower(-3.23, 0))
print(recurPower(-2.78, 8))

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    test = min(a, b)
    while a % test != 0 or b % test != 0:
        test -= 1
    return test

print(gcdIter(92, 36))

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

print(gcdRecur(432, 342))

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
#    high = aStr[round((len(aStr)-1)/2)]
#    print(high)
#   
#    low = aStr[0]
    if len(aStr) == 0:
        return False
    
    if len(aStr) == 1:
        return aStr == char
    
    testCharIndex = len(aStr)//2
    testChar = aStr[testCharIndex]
    if testChar == char:
        return True
    elif testChar > char:
        return isIn(char, aStr[:testCharIndex])
    else:
        return isIn(char, aStr[testCharIndex+1: ])
print(isIn('a', ''))
print(isIn('e', 'abdehikmoooqrquyzz'))
print(isIn('e', 'e'))   