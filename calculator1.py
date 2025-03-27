num1 = float(input('enter first number:'))
num2= float(input('enter second number:'))

print ('choose an operation :+,-,/,*')
operation = input ('Enter operation')

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"
