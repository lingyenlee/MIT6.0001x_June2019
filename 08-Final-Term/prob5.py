#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 10:23:13 2019

@author: apple
"""
def f(a,b): 
    return a+b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    intersect = {}
    difference = {}
    for key in d1:
        if key in d2:
            intersect[key] = f(d1[key], d2[key])
        else:
            difference[key] = (d1[key])
            
    for key in d2:
        if key not in d1:
            difference[key] = d2[key]
   
    return(intersect, difference)
        
        
        
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
print(dict_interdiff(d1, d2))