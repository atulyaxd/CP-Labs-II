# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:27:21 2025

@author: Lenovo
"""

str = input("Enter a string = ")
uppercase = 0
lowercase = 0
num = 0
sym = 0

for i in str:
    if i >= 'A' and i <= 'Z':
        uppercase += 1
    elif i >= 'a' and i <= 'z':
        lowercase += 1
    elif i >= '0' and i <= '9':
        num +=1
    else: 
        sym+=1
        
print(f"No of alphabets = {uppercase+ lowercase}, No of numbers = {num}, No of symbol = {sym}")