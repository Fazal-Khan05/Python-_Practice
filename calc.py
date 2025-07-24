# Ask the user for two numbers and an operator (+, -, *, /).
# Use input() to take the values, perform the selected operation, and print the result.

print("------------------------Welcome to the simple calculator!---------------------------------------")
a = float(input("Enter first number :"))
b = float(input("Enter second number :"))

choice = input("Enter any operator + , - , * , / . :")

print("Performing operation........")

if choice == "+" :
    print("The addition of two numbers is :", a + b)
elif choice == "-" :
    print("The subtraction of two numbers is :", a - b)
elif choice == "*" :
    print("The multiplication of two numbers is :", a * b)
elif choice == "/" :
    print("The division of two numbers is :", a / b)
else:
    print("Incorrect operator selected. Please select correct operator")


