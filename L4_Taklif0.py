

#--------L4 Taklif0------تشخیص عدد------------------
#---- تشخیص مثبت یا منفی بودن عدد-------- 

number = int(input("Enter a number: ").strip())
if number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is positive")    


#----------تشخیص زوج یا فرد بودن عدد--------------

number = int(input("Enter a number: ").strip())
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")