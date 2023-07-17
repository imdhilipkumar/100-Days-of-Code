#Simple calculator
from art import logo
# Addition
def add(num1,num2):
    return num1 + num2

#Substraction
def subtraction(num1,num2):
    return num1 - num2

#multiplication
def multipulication(num1,num2):
    return num1 * num2

# Division
def Division(num1,num2):
    return num1 / num2

# creation the dictionary to add the keys as symbol and value as function call it as the operation

operation={
    "+":add,
    "-":subtraction,
    "*":multipulication,
    "/":Division
    }

# get the value from the user


def calculator():
    print(logo)   
    num1=float(input("What's the first number?: "))
    for symbols in operation:
        print(symbols)
    should_continue=True
    while should_continue:       
        operation_symbol=input("Pick the operation: ")
        num2=float(input("whats's the next number?: "))
        calculation=operation[operation_symbol]
        result=calculation(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")
        new_operation=input(f"Type 'y'  continue with {result}, or type 'n'end the calculation orType 'new' to start the new program .:")
        if new_operation=="y":
            num1=result
        elif new_operation=="new":
            should_continue=False
            calculator()
        else:
            should_continue=False
            print("Good Bye")
            
calculator()

