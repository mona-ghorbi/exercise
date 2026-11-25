# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 08:23:59 2026

@author: Mona Ghorbi
"""

#---------تمرین 25 طراحی منوی مدیریت کاربران-----------------#

users = []

while True:
    print("==== User Management ====")
    print("1. Add User")
    print("2. Show Users")
    print("3. Search User")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 4 :
        break
    elif choice == 1:
        user = input("Enter the user: ").strip()
        users.append(user)
        print(f"{user} added to the list.")
    elif choice == 2:
        print(users)
    elif choice == 3:
        user = input("Enter the user: ").strip()
        index = 0
        while index < len(users) :
            item = users[index]
            if item.lower() == user.lower():
                print(f"User fond in index {index}")
                break
            else:
                index +=1
        if index == len(users):
            print("User not found")
    else:
         print("Invalid Choice")
            
            
    
