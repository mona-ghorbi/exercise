



#---------تمرین 25 طراحی منوی مدیریت کاربران-----------------#


def user_management_menu(users):
    while True:
        print("==== User Management ====")
        print("1. Add User")
        print("2. Show Users")
        print("3. Search User")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 4 :
            return users
        elif choice == 1:
            user = input("Enter the user: ").strip()
            users.append(user)
            print(f"{user} added to the list.")
        elif choice == 2:
            print(users)
        elif choice == 3:
            user = input("Enter the user: ").strip()
            index = 0
            while index < len(users) :
                item = users[index]
                if item.lower() == user.lower():
                    print(f"User fond in index {index}")
                    break
                else:
                    index +=1
            if index == len(users):
                print("User not found")
        else:
             print("Invalid Choice")
                

print(user_management_menu([]))