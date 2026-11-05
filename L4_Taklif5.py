
#-----------L4 Taklif5---------------ورود به کلاس-------------------


users = ["mona", "nima", "ali"]

username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

if username not in users:
    print("User not found")
elif password == "python123":
    print("Welcome")
else:
    print("Wrong password!")
    




