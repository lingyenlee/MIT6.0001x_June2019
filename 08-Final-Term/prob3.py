#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 08:37:19 2019

@author: apple
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    
    while True:
        try:
            num_list = list(s)
            total = 0
            num_list = []
            for i in s:
                if i.isdigit():
                    num_list.append(int(i))
            
            return sum(num_list)
            
        except ValueError:
            return False 
    
    
#    num_list = list(s)
#    total = 0
#    num_list = []
#    for i in s:
#        if i.isdigit():
#            num_list.append(int(i))
#    return sum(num_list)
    
              
    
#    return  sum([int(i) for i in s if type(i)== int or i.isdigit()]) 
    
        
    
print(sum_digits("a;35d4"))
print(sum_digits("ssdfm"))