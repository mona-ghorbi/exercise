


#---------تمرین 23 محدودیت تعداد تلاش برای ورود-----------------#


def login_with_limit(correct_password, max_attempts):
    attempt = 0
    while True:
        if attempt >= max_attempts:
            return False
        else:
            user_password = input('password:')
            if user_password == correct_password:
                return True
            else:
                attempt = attempt + 1
                print('wrong password')
                print('tedade baghimonde:',3-attempt)
                
if login_with_limit("admin123", 3):
    print('login successfully')
else:
    print('account locked')
