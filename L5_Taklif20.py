# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 07:35:20 2026

@author: Mona Ghorbi
"""

#---------تمرین 20 دریافت عدد معتبر-----------------#

while True:
    user_number = int(input("Enter a number between 0 to 100: "))
    if 0 < user_number < 100:
        break
print("number is:", user_number)


#or
'''
number = int(input("number:"))
while number<1 or number>100:
    number = int(input("number:"))
print(number)

'''