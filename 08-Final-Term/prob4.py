#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 09:21:49 2019

@author: apple
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    result = {}
    for i in L:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    print(result)
    result2 = []
    for key, value in result.items():
        if value % 2 != 0:
           result2.append(key)
    
    if len(result2) > 0:
        return max(result2)
    else:
        return None
      
            
    
print(largest_odd_times([2,2,4,4]))
print(largest_odd_times([3,9,5,3,5,3]))
print(largest_odd_times([3, 3, 2, 0]))