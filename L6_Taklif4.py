
#---------------------------تمرین 4 جدول ضرب---------------------#


number = int(input("Enter a number: ").strip())


def multiplication_table(number):
    multiplication_list =[]
    for i in range(1,11):
        multiplication_list.append(f"{number}*{i}={number*i}")
    return multiplication_list

print(multiplication_table(number))
