

#------------------------تمرین 11 توقف حلقه با عدد صفر-------------------#



def sum_until_zero(max_count):
    sum = 0
    for i in range(max_count):
        number = int(input("Enter a number: ").strip())
        if number != 0:
            sum += number
        else:
            break
    return sum    
    
print(sum_until_zero(10))