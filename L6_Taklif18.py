
#--------------تمرین 18 پیاده سازی range با حلقه while----------#



def custom_range(start, stop, step):
    range_list = []
    while start < stop :
        range_list.append(start)
        start = start + step;
    return range_list

print(custom_range(2, 15, 3))