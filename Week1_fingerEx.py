#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 12:03:03 2019

@author: apple
"""
#def a(x, y, z):
#     if x:
#         return y
#     else:
#         return z
#
#def b(q, r):
#    return a(q>r, q, r)
#
#a(3>2, a, b)

#def iterPower(base, exp):
#    '''
#    base: int or float.
#    exp: int >= 0
# 
#    returns: int or float, base^exp
#    '''
#    # Your code here
#    result = 1
#    while exp > 0:
#        result = base * result
#        exp -= 1
#    return result
#
#print(iterPower(2, 3))

#def gcdIter(a, b):
#    '''
#    a, b: positive integers
#    
#    returns: a positive integer, the greatest common divisor of a & b.
#    '''
#    # Your code here
#    test = min(a, b)
#    while a % test != 0 or b % test != 0:
#        test -= 1
#    return test
#
#print(gcdIter(92, 36))


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
    
    
    
    
    
    
    
    
    
    
    
    