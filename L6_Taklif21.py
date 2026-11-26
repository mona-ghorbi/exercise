

#---------تمرین 21 محاسبه مجموع اعداد تا ورود صفر-----------------#
  
    
def sum_until_zero_conditional():
    number = int(input("Enter a number: "))
    sum = 0
    while number != 0:
        sum += number
        number = int(input("Enter a number: "))
    return sum

print(sum_until_zero_conditional())

#----------------------------

def sum_until_zero_break():
    sum = 0
    while True :
        number = int(input("Enter a number: "))
        if number != 0:
            sum += number
        else:
            break
    return sum

print(sum_until_zero_break())