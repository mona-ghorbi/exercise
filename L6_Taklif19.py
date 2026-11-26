
#---------تمرین 19 محاسبه مجموع اعداد-----------------#


def sum_to_n_while(n):
    i = 1
    j = 0
    while i <= n :
        j = i +j
        i +=1
    return j

print(sum_to_n_while(5))
