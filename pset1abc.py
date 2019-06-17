#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:45:08 2019

@author: apple
"""

s = 'azcbobobegghakl'

#pset1 problem 1
#count = 0
#for i in s:
#    if i == "a" or i == "e" or i =="i" or i == "o" or i == "u":
#        count += 1
#        
#print(count)

#pset1 problem 2
#match = 0
#for i in range(len(s)):
#   if s[i:i+3] == "bob":
#       match =+ 1
#
#print(match)


prevChar = ""
currentString = ""
longestString = ""

for char in s:
  
   if prevChar <= char:
       currentString += char
       if len(currentString) > len(longestString):
           longestString = currentString
          
   else:
       currentString = char
   
   prevChar = char
   
print(longestString)  

#for letter in s:
#    if letter is 
#    if s[i] > s[i+1]:
#        temp = 
#    else:
#        temp += s[i]
#        print(temp)


    



        
        
    


       
        
       

