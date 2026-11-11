
#----------------------------تمرین 9 پیدا کردن عدد مورد نظر------------#


numbers = [4, 9, 15, 23, 42, 56, 71]
user_number = int(input("Enter a number: ").strip())

for number in numbers:
    if number == user_number:
        print("Number found")
        break
   
    