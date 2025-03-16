# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:09:39 2025

@author: Lenovo
"""
import math

def series(m):
    sum = 0 
    for i in range(1,m+1):
        sum += i / math.factorial(i)
    print(sum)
              

m = eval(input("Enter a number: "))
series(m)