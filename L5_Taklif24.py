# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 08:04:30 2026

@author: Mona Ghorbi
"""

#---------تمرین 24 بازی حدس عدد-----------------#


#-----------روش اول-----------------#

secret_number = 7

guess = int(input("Guess the number: "))

while guess != secret_number :
    if guess < secret_number:
        print("Too Low")
    else:
        print("Too High")
    guess = int(input("Guess the number: "))

print("Correct!")


#---------------------روش دوم ----------#

secret_number = 7

while True :
    guess = int(input("Guess the number: ")) 
    if guess < secret_number:
          print("Too Low")
    elif guess > secret_number:
          print("Too High")
    else:
          print("Correct!")
          break
    


