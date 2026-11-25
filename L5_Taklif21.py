# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 07:38:56 2026

@author: Mona Ghorbi
"""

#---------تمرین 21 محاسبه مجموع اعداد تا ورود صفر-----------------#

#--------------روش اول-----------#


number = int(input("Enter a number: "))
sum = 0

while number != 0:
    sum = sum + number
    number = int(input("Enter a number: "))
    
print(sum)


#-------------روش دوم------------#

sum = 0
while True :
    number = int(input("Enter a number: "))
    if number != 0:
        sum = sum + number
    else:
        break
print (sum)    
    