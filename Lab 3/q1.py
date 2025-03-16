# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:32:20 2025

@author: Lenovo
"""

colours = ["Red", "Blue", "Green", "Pink"]

#accessing elements

#for i in range(len(colours)):
#    print(colours[i],end=",")
#
#print("\n")
print(colours[1])
print(colours[1:])
print(colours[0:2])
#changing element

colours[3] = "Black"

#replacing the element

temp = "Black"
colours[3] = colours[1]
colours[1] = temp

#appending the value
new_color = input("Enter a new colour: ")
colours.append(new_color)

#inserting an element

new_color = input("Enter a new colour: ")
colours.insert(2, new_color)

#extend item

new_color_list = ["Purple", "Golden", "Silver"]
colours.extend(new_color_list)

#remove item
colours.remove("Golden")
colours.pop()

print(colours)
#clear 
colours.clear()

