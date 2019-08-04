#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:27:10 2019

@author: apple
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    odd = ()
    for t in range(0, len(aTup)):
        if t % 2 == 0:
            odd =  odd + (aTup[t],)

    return odd     
         
oddTuples(('I', 'am', 'a', 'test', 'tuple'))

def findRoot(x, power, epsilon):
    
    """
    Assumes x and epsilon int or float, power an int,
    epsilon > 0 & power >= 1
    Returns float y such that y**power is within epsilon of x.
    If such a float does not exist, it returns None
    """ 
    if x < 0 and power%2 == 0:
        return None
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**power - x) >= epsilon:
        if ans**power < x: 
            low = ans
        else:
            high = ans
    ans = (high + low)/2.0 
    return ans


#def applyEachTo(L, x):
#    result = []
#    for i in range(len(L)):
#        result.append(L[i](x))
#    return result
#
#def square(a):
#    return a*a
#
#def halve(a):
#    return a/2
#
#def inc(a):
#    return a+1
#
#applyEachTo([inc, max, int], -3)

#animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
#
#animals['d'] = 'donkey'
#
#print(animals)
#print(animals['c'])
#print(len(animals["a"]))
#for element in animals:
#       print( element )
#print('baboon' in animals)
#del animals['b']
#print(animals.values())

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


#def how_many(aDict):
#    '''
#    aDict: A dictionary, where all the values are lists.
#
#    returns: int, how many values are in the dictionary.
#    '''
#    count = []
##    return sum(len(animal) for animal in aDict.values())
#    for animal in aDict.values():    
#        count += animal
#        
#    return(len(count))
#print(how_many(animals))


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    animalList = {}
    for animal in aDict:
        animalList[animal] = len(aDict[animal])
    return max(animalList.keys())

#        animalList[value_animal] = len(value_animal)
#    return animalList
     

print(biggest(animals))