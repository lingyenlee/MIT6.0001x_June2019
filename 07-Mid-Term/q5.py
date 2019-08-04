# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:46:18 2019

@author: Lee
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    result = {}
    uniq_key = []
    
    for value in aDict.values():
        
        if value in result:
            
            result[value] += 1
        else: 
            result[value] = 1
    
    for key, value in aDict.items():
        if result[value] == 1:
            uniq_key.append(key) 

    return uniq_key

print(uniqueValues({4: 2, 5: 3, 6: 4}))
print(uniqueValues({1: 1, 2: 1, 3: 3}))

    