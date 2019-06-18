#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:45:08 2019

@author: apple

Write a program that counts up the number of vowels contained 
in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:
"""

s = 'azcbobobegghakl'

#pset1 problem 1
#count = 0
#for i in s:
#    if i == "a" or i == "e" or i =="i" or i == "o" or i == "u":
#        count += 1
#        
#print(count)

"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""

#pset1 problem 2
#match = 0
#for i in range(len(s)):
#   if s[i:i+3] == "bob":
#       match =+ 1
#
#print(match)

#pset problem 3
"""
Write a program that prints the longest substring of s in which the 
letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', 
then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print
Longest substring in alphabetical order is: abc
"""
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


    



        
        
    


       
        
       

