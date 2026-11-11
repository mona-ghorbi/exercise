
#----------------تمرین 16 سیستم مدیریت نمرات دانشجویان -------------------#


students = [ 
    ("Ali", 22, 18), 
    ("Sara", 20, 15), 
    ("Reza", 23, 9), 
    ("Mina", 21, 20), 
    ("Nima", 19, 12), 
    ("Amir", 24, 7) 
]

under10_students = []
above_average = []
max_number = students[0]
sum = 0

for student in students:
    print("Name: {student[0], Age: {student[1]}, Grade: {student[2]}")
    if student[2] <10:
        under10_students.append(student[0])
    sum += student[2] 
    if student[2] > max_number[2]:
        max_number = student

average = sum/len(students)
for student in students:
    if student[2] > average:
        above_average.append(student[0])
        
        
print(f"Average of all students grades is: {average}")
print(f"Students with grade under 10 are: {under10_students}")
print(f"Maximum grade is for {max_number[0]}")
print(f"Students with grade above avarage are: {above_average}")








