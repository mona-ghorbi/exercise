

#------------------L4 Taklif4------------بررسی رمز عبور-----------------
#----------------------just if------------------------------------
#چون در مسئله گفته شده حتما هر 3 شرط باید چک شود کوتاه ترین و بهترین راه این روش است

password = input("Enter a password: ")
if len(password) < 8:
    print("The password is too short!")
if password.replace(" ","").isdigit():
    print("The password is all numbers!")
if password.find(" ") != -1:
    print("The password contains one or more spaces!")


#----------------------nested if------------------------------------

#چون لازم است تمام مسیرها چک شوند با این روش لازم است تمام شرط ها در هر شاخه به صورت تکراری چک شوند و روش مناسبی نیست
password = input("Enter a password: ")
if len(password) < 8:
    if password.replace(" ","").isdigit():
        if password.find(" ") != -1:
            print("The password is too short!")
            print("The password is all numbers!")
            print("The password contains one or more spaces!")
        else:
            print("The password is too short!")
            print("The password is all numbers!")
    else:
        if password.find(" ") != -1:
            print("The password is too short!")
            print("The password contains one or more spaces!")
        else:
            print("The password is too short!")
if len(password) > 8:
    if password.replace(" ","").isdigit():
        if password.find(" ") != -1:
            print("The password is all numbers!")
            print("The password contains one or more spaces!")
        else:
            print("The password is all numbers!")
    else:
        if password.find(" ") != -1:
            print("The password contains one or more spaces!")
        
        
#---------------------elif-------------------------------
# نسبت به روش قبل بهتر شده اما باز هم شرط تکراری نوشته شده است

password = input("Enter a password: ").strip()
if len(password) < 8:
    print("The password is too short!")
    if password.replace(" ","").isdigit():
        print("The password is all numbers!")
        if password.find(" ")!= -1:
            print("The password contains one or more spaces!")
    elif password.find(" "):
            print("The password contains one or more spaces!") 
elif password.replace(" ","").isdigit():
    print("The password is all numbers!")
elif password.find(" ")!= -1:
    print("The password contains one or more spaces!")

#-----------------------------------------------------------


        
   
