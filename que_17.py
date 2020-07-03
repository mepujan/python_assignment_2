# Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.


def calculator(num1, num2,operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return 'Cannot be divided by zero'

num1=int(input('Number1: '))
num2=int(input('Number2: '))
operator=input('Enter the operator (+,-,*,/): ')

print("Result = ",calculator(num1,num2,operator))