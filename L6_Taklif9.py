
#----------------------------تمرین 9 پیدا کردن عدد مورد نظر------------#


numbers = [4, 9, 15, 23, 42, 56, 71]
target = int(input("Enter a number: ").strip())

   
def find_number(numbers, target):
    for number in numbers:
        if number == target:
            return True
            break
    return False
    
if find_number(numbers, target):
    print("Number Found")
else:
    print("Number Not Found")