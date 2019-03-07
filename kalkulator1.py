import json
x = first_num = int(input("Enter the first number: "))
y = second_num = int(input("Enter the second number: "))

operation = input("Choose math operation (+, -, *, /: ")

history_file = open("history.txt", "a")

if operation == "+":
    result = x + y
    print(result)
    history_file.write(json.dumps(str(result)))
elif operation == "-":
    result = x - y
    print(x - y)
    history_file.write(json.dumps(str(result)))
elif operation == "*":
    result = x * y
    print(x * y)
    history_file.write(json.dumps(str(result)))
elif operation == "/":
    result = x / y
    print(x / y)
    history_file.write(json.dumps(str(result)))
else:
    print("You did not provide the correct math operation.")
    history_file.write("You did not provide the correct math operation.")

def get_history_list():
    with open("history.txt", "r") as history_file:
        history_list = json.loads(history_file.read())
        return history_list


history_file.close()
