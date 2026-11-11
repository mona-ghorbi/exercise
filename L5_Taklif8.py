

#------------------------------تمرین 8 دریافت چند عدد از کاربر----------#

numbers = []
quantity = int(input("How many: ").strip())
for i in range(quantity):
    number = int(input("Enter a number: ").strip())
    numbers.append(number)
print(numbers)    

