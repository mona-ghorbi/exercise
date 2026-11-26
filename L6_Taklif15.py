
#-----------------------------تمرین 15 جستجوی کاربر-----------------------#


users = [
    (1, "ali", "active"), 
    (2, "sara", "inactive"), 
    (3, "reza", "active"), 
    (4, "mina", "inactive"), 
    (5, "nima", "active") 
]

        

def search_user(users, username):
    for user in users:
        if user[1] == username:
            return user[0], user[2]
    return None
            
print(search_user(users, "sara"))    

