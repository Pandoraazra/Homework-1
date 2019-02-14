x = first_num = int(input("Enter the first number: "))
y = second_num = int(input("Enter the second number: "))

operation = input("Choose math operation (+, -, *, /: ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("You did not provide the correct math operation.")