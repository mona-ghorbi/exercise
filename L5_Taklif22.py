# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 07:48:25 2026

@author: Mona Ghorbi
"""

#---------تمرین 22 بررسی رمز عبور-----------------#

password = "python123"

while True:
    user_password =input("Enter the password: ")
    if user_password == password:
        print("Login successfull")
        break
    else:
        print("wrong password")
        
#or------

password = "python123"
user_password =input("Enter the password: ")

while user_password != password:
    print("wrong password")
    user_password =input("Enter the password: ")

print("Login successfull")