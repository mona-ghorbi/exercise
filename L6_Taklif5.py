

#---------------------تمرین 5 بررسی اعداد داخل لیست-----------------#


        
def analyze_even_numbers(numbers):
    even__numbers =[]
    for number in numbers:
        if number%2 == 0 : 
            even__numbers.append(number)
    return even__numbers
    
numbers = [12, 7, 25, 18, 3, 40, 11, 8]

print((len(analyze_even_numbers(numbers)),analyze_even_numbers(numbers)))