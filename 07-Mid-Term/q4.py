# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:25:53 2019

@author: Lee
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    listAB = []
    total = 0
    for i in range(0, len(listA)):
        listAB.append(listA[i]*listB[i])
    
    for i in listAB:
        total += i
    return total
print(dotProduct([1,2,3], [4,5,6]))