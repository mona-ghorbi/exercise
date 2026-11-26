


#---------تمرین 22 بررسی رمز عبور-----------------#




def login_conditional(correct_password):
    user_password =input("Enter the password: ")
    while user_password != correct_password:
        user_password =input("Wrong password, Enter the password again: ")
    return True
    
if login_conditional("python123"):
    print("Login Successful")

#---------------

def login_break(correct_password):
    while True:
        user_password =input("Enter the password: ")
        if user_password == correct_password:
            return True
        else:
            print("Wrong password")
    
if login_break("python123"):
    print("Login Successful")    