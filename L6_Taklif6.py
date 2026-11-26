
#-------------------------تمرین 6 محاسبه مجموع و میانگین-------------#



def calculate_scores(scores):
    sum = 0
    average = 0
    for score in scores:
        sum +=score
    average = sum / len(scores)
    return sum, average
    print("sum =", sum)
    print("average =", average)
    
    
scores = [15, 18, 12, 20, 16, 14, 19]
print(calculate_scores(scores))