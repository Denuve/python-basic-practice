import operator

operator_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def get_valid_operator(op):
    while True:
        print("You need to provide a valid operator!\n")
        op = input("enter the operation you need to perform(+,-,*,%):")
        if op in operator_dict:
            operatorinput = op
            break


print("This is a basic calculator!\n")

firstnumber = int(input("enter first number: "))
secondnumber = int(input("enter second number: "))
operatorinput =  input("enter the operation you need to perform(+,-,*,/):")



if operatorinput not in operator_dict.keys():
    get_valid_operator(operatorinput)

try:
    result = operator_dict[operatorinput](firstnumber, secondnumber)
    print(f"Result: {result}")
except ZeroDivisionError:
    print("You can't divide by 0")
