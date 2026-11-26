
#----------------------------تمرین 7 ایجاد لیست جدید---------------------#


def square_numbers(numbers):
    square_numbers = []
    for number in numbers:
        square_numbers.append(pow(number,2))
    return square_numbers
    
numbers = [2, 4, 6, 8, 10]    
print(square_numbers(numbers))    