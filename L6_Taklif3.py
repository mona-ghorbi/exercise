
#-----------------------تمرین 3 محموع اعداد--------------------#

def sum_range(start,end):
    sum =0
    for i in range(start,end+1):
        sum += i
    return sum

print(sum_range(1,100))