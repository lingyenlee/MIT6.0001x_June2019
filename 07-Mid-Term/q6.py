# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:08:07 2019

@author: Lee
"""

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(20,12))
print(gcd(23, 290))