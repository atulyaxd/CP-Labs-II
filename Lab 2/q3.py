# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 09:10:37 2025

@author: Lenovo
"""

n = int(input("Enter a number: "))


#Method 1: First check if the number of factors is greater than one or not 
count = 0

for i in range(2,n+1):
    if (n % i == 0):
        count +=1
    
if (count > 1):
    print(f"-> {n} is not prime.")
else:
    print(f"-> {n} is prime.")