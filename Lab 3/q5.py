# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:03:55 2025

@author: Lenovo
"""
# isinstance(element, data_type)

n = ["Atulya", "Bharat", 1,2,3,4, "Jha"]

sum = 0
count = 0


for i in n:
    if (isinstance(i,int) == True ):
        sum += i
        count +=1 

mean = sum / count
print("sum : {}, mean: {} ".format(sum,mean))
