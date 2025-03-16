# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:51:07 2025

@author: Lenovo
"""

users = {"atulya":"123456789", "anshul" : "qwerty"}

"""
run = True
while run:

    usr_id = input("Enter user id: ")
    usr_pwd = input("Enter user pwd: ")

    if(users[usr_id] == usr_pwd):
        print("Access granted")
        run = False
        break
        
    
    else:
        count = 1
        usr_id = input("Enter user id: ")
        usr_pwd = input("Enter user pwd: ")
        while usr_id in users and count < 3:
            
            if(users[usr_id] == usr_pwd):
                print("Access granted")
                run = False
                break
            else:
                count += 1
                print("reverify")
        
        if(count == 3):
            print("\n*Limit Reached* \nAccount blocked")
            c = input("Proceed to update password Y,N: ")
            if (c == "Y"):
                usr_id = input("Enter user id: ")
                new_pwd = input("New password: ")
                users[usr_id] = new_pwd

                print("Updated!!")
                run = False
                break
                

"""            
        
#Updated

def inputs():
    usr_id = input("Enter user id: ")
    usr_pwd = input("Enter user pwd: ")

    if usr_id in users:
        if (users[usr_id] == usr_pwd):
            return 1    
        else:
            return 0
count = 3

def update(usr_id):
    usr_pwd = input("Enter new user pwd: ")
    users[usr_id] = usr_pwd
    print("Updated !!")


while count > 0:
    run = inputs()
    if run == 1:
        print("Access granted!!")
        break

    elif run == 0:
        count -= 1
        print(f"Please reverify, {count} chances remaining")
        if count == 0:
            u_yn = input("Want to change pwd : ")
            if u_yn == "Y":
                update(usr_id=input("enter user id: "))
            else:
                break 


         

