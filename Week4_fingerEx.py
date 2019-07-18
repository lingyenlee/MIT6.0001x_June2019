#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 03:58:16 2019

@author: apple
"""

#class Coordinate(object):
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#
#    def getX(self):
#        # Getter method for a Coordinate object's x coordinate.
#        # Getter methods are better practice than just accessing an attribute directly
#        return self.x
#
#    def getY(self):
#        # Getter method for a Coordinate object's y coordinate
#        return self.y
#    
#    def __eq__(self, other):
#        if self.x == other.x and self.y == other.y:
#            return True
#        else:
#            return False
#    
#    def __repr__(self):  
#        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')' 
#    
#
#    def __str__(self):
#        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
#
#x = Coordinate(3, 4) 

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    
    def intersect(self, other):
        """Assumes other is a intSet and return a new set
        with integers appear in both self and other"""
        commonSet = intSet()
        for x in self.vals:
            if other.member(x):
                commonSet.insert(x)
        
        return commonSet
    
    def __len__(self):
        return len(self)

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

setA = {-17,-16,-12,-2,3,7,12,13,19}
setB = {-17,-16,-8,7,10,13,17,19}
setA.intersect(setB)