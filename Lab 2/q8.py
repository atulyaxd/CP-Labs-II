# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:20:39 2025

@author: Lenovo
"""

import math

print("format of eqn: ax**2 + bx + c")
a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
c = eval(input("Enter c: "))


val = {-1,2,3,4,5}

d = math.pow(b,2) / (2 *a)

for x in val:
    F = a*pow(x,2) + b * x + c
    if (x==d):
        print(f"F[{x}]  = 0")
    elif (x > d):
        print(f"F[{x}] = {F}")
    elif (x < d):
        print(f"F[{x}] = {F}")
        
