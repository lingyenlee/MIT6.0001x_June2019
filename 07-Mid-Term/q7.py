# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:15:28 2019

@author: Lee
"""

def satisfiesF(L):
    
    for i in range(0, len(L)-1):
       
        if f(L[i]) == False:
            L.remove(L[i])
   
    return len(L)
        
def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)