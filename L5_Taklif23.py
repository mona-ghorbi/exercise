# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 07:50:56 2026

@author: Mona Ghorbi
"""

#---------تمرین 23 محدودیت تعداد تلاش برای ورود-----------------#

admin_password ='admin123'
attempt = 0 
while True:
    if attempt>=3:
        print('account locked')
        break
        
    else:
        user_password = input('password:')
        if user_password==admin_password:
            print('login successfully')
            break
        else:
            attempt = attempt + 1
            print('wrong password')
            print('tedade baghimonde:',3-attempt)



#-------روش دیگر --------#

password = "admin123"
attempt = 3
while attempt>0:
    user_password = input("Enter the password: ")
    attempt = attempt -1
    if user_password == password:
        print("Access Granted")
        break
    else:
        print(f"{attempt} attempt is left")
if attempt == 0:
    print("Account is locked") 