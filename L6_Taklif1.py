# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:52:52 2026

@author: Mona Ghorbi
"""


#--------------تمرین 1 نمایش اعداد فرد--------------#

def odd_numbers(start,end):
    odd_numbers =[]
    for i in range(start,end,2):
        odd_numbers.append(i+1)
    return odd_numbers

print(odd_numbers(10,50))
    

