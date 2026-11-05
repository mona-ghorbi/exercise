
#----------------L4 Taklif6----------------ماشین حساب----------------

x = float(input("Enter x: ").strip())
y = float(input("Enter y: ").strip())
operation = input("Enter an operation(+,-,*,/): ").strip()

if operation == "+":
    print(f"x+y={x+y}")
elif operation == "-":
    print(f"x-y={x-y}")
elif operation == "*":
    print(f"x*y={x*y}")
else:
    print(f"x/y={x/y}")

