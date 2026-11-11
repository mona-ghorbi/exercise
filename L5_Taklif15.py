

#-----------------------------تمرین 15 جستجوی کاربر-----------------------#


users = [
    (1, "ali", "active"), 
    (2, "sara", "inactive"), 
    (3, "reza", "active"), 
    (4, "mina", "inactive"), 
    (5, "nima", "active") 
]

i=0

username = input("Enter a username: ").strip()
for user in users:
    if user[1] == username:
        print(f"user_id: {user[0]}, state: {user[2]}")
        break
    else:
        i+=1
        
if i == len(users):
    print("User not found")


