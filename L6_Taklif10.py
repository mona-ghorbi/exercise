 
#--------------------------------------تمرین 10 ------------------------#



def skip_multiplies_of_three(start, end):
    not_multiplies_of_three = []
    for i in range(start,end+1):
        if i % 3 != 0 :
            not_multiplies_of_three.append(i)
    return not_multiplies_of_three

print(skip_multiplies_of_three(1, 30))