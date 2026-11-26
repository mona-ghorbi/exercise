
#------------------------تمرین 12 اطلاعات دانشجویان -----------------------#

students = [ 
    ("Ali", 22), 
    ("Sara", 19), 
    ("Reza", 25), 
    ("Nima", 20), 
    ("Mina", 23) 
]


def format_students(students):
    format_students_list = []
    for student in students:
        format_students_list.append(f"name: {student[0]}, Age: {student[1]}")
    return format_students_list
        
print(format_students(students))  
