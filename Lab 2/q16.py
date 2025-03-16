# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:39:51 2025

@author: Lenovo
"""
set_pwd = "atulya"

run = True
while run:
    pwd = input("Enter password: ")
    if pwd == set_pwd: 
        run = False 
        print("Access granted!!")
        break 
    