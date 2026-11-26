
#--------------------------تمرین 14 محاسبه قیمت محصولات -------------------#

products = [ 
    ("Laptop", 50000, 2), 
    ("Mouse", 800, 3), 
    ("Keyboard", 1500, 2), 
    ("Monitor", 12000, 1) 
]


def calculate_card(products):
    sum = 0
    product_list =[]
    for product in products:
        price = product[1] * product[2]
        product_list.append((product[0],price))
        sum += price
    return product_list, sum

print(calculate_card(products))
    
    
    
    
    
