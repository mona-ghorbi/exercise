
#------------------------تمرین 11 توقف حلقه با عدد صفر-------------------#

numbers = []
for i in range(10):
    number = int(input("Enter a number: ").strip())
    if number != 0:
        numbers.append(number)
    else:
        break
print(numbers)    
        

