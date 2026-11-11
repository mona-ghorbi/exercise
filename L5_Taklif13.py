
#-----------------------تمرین 13 فیلتر دانشجویان بر اساس نمره-------------#

students = [ 
    ("Ali", 18), 
    ("Sara", 12), 
    ("Reza", 9), 
    ("Mina", 20), 
    ("Nima", 14) 
]

for student in students:
    if student[1] >= 15:
        print(student[0])

