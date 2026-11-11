
#-------------------------تمرین 6 محاسبه مجموع و میانگین-------------#

scores = [15, 18, 12, 20, 16, 14, 19]
sum = 0
average = 0

for score in scores:
    sum +=score
average = sum / len(scores)
print("sum =", sum)
print("average =", average)


