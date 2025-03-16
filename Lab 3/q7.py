# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:23:23 2025

@author: Lenovo
"""

l = [-1,2,3,-4,5,-23,10]

p = 0
n = 0
for i in l:
    if (i > 0):
        p +=1
    elif (i < 0):
        n += 1

print(f"Number of positive = {p}",f"Number of negative = {n}",sep="\n")