def calc (num1,num2,operation):
    
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operation +, - , * , /: ")
result = calc(num1, num2, operator)
print(f"The result of {num1} {operator} {num2} is: {result}")