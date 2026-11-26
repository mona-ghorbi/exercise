
#-----------------------تمرین 13 فیلتر دانشجویان بر اساس نمره-------------#

students = [ 
    ("Ali", 18), 
    ("Sara", 12), 
    ("Reza", 9), 
    ("Mina", 20), 
    ("Nima", 14) 
]


def filter_students_by_grade(students, min_grade):
    higher_min_grade = []
    for student in students:
        if student[1] >= min_grade:
            higher_min_grade.append(student[0])
    return higher_min_grade

print(filter_students_by_grade(students,15))        