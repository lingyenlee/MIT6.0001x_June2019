# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    
    int_exp = 0
    if base == num:
        int_exp = 1
    elif base > num:
        int_exp = 0
    else:
        for i in range(1, int(num)):
           if abs(num - base**i) <= abs(num - base**(i+1)):
               int_exp = i
               break
    return int_exp
print(closest_power(4, 160.0))      
print(4**3)
print(4**4)
print(160 - 4**3)
print(160 - 4 ** 4)