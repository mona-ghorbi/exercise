

#-------------L4 Taklif3-------------هزینه ارسال--------------------

purchase_amount = int(input("Enter the purchase amount(in Toman): ").strip())
if purchase_amount >= 1000000:
    shipping_cost = 0
elif purchase_amount >= 500000:
    shipping_cost = 30000
else:
    shipping_cost = 60000

print(f"Shipping cost is: {shipping_cost} Toman")


