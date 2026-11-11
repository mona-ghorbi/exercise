
#--------------------------تمرین 14 محاسبه قیمت محصولات -------------------#

products = [ 
    ("Laptop", 50000, 2), 
    ("Mouse", 800, 3), 
    ("Keyboard", 1500, 2), 
    ("Monitor", 12000, 1) 
]

sum = 0

for product in products:
    price = product[1] * product[2]
    print(f"Total price {product[0]} is {price}")
    sum += price

print(f"Total price of all products is: {sum}")


