
#---------تمرین 20 دریافت عدد معتبر-----------------#


def get_valid_number():
    while True:
        user_number = int(input("Enter a number between 0 to 100: "))
        if 0 < user_number < 100:
            return user_number
    
print(f"The number is : {get_valid_number()}")