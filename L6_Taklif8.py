
#------------------------------تمرین 8 دریافت چند عدد از کاربر----------#


count = int(input("How many: ").strip())


def collect_numbers(count):
    numbers = []
    for i in range(count):
        number = int(input("Enter a number: ").strip())
        numbers.append(number)
    return numbers    
        
        
print(collect_numbers(count))    