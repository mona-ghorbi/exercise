
#--------------تمرین 17 تبدیل حلقه for به while----------#


def count_with_while(start, end):
    count_list = []
    i = start
    while i< end+1:
        count_list.append(i)
        i +=1
    return count_list


print(count_with_while(1, 20))