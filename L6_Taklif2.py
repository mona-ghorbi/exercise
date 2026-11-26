
#---------------------تمرین 2 شمارش معکوس------------------#


def revers_count(start,end):
    revers_list =[]
    for i in range(start,end-1,-1):
        revers_list.append(i)
    return revers_list

print(revers_count(20,1))

