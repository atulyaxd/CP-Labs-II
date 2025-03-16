# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 09:20:37 2025

@author: Lenovo
"""
#Redo

import math
print("format of eqn: ax**2 + bx + c")
a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
c = eval(input("Enter c: "))

D = pow(b,2) - 4*a*c

if (D > 0):
    print("Real and Disticnt roots exists.")
    t1 = -b/(2*a)
    t2 = math.sqrt(D)/(2*a)

    print(f"root 1 = {t1 + t2}")
    print(f"root 2 - {t1 - t2}")

elif (D == 0):
    
    print("Real and Equal roots exists.")
    t1 = -b/(2*a)
    t2 = math.sqrt(D)/(2*a)

    print(f"root 1 = {t1 + t2}")
    
elif (D < 0):
    print("Complex roots exists.")
    
    real_part = -b/(2*a)
    imag_part = pow(D,0.5)/(2*a)

    r1 = complex(real_part,imag_part)
    r2 = complex(real_part,-imag_part)

    print("Imaginary roots = {}, {}.".format(r1,r2))