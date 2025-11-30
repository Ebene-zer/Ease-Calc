"""
functions
add_func
subtract_func
multiply_func
divide_func
"""

# Welcome Message
print("Hi, may I know your name?")
user_name = input(str("Call me: "))
print (f"Welcome {user_name}.\n"
       "Have fun with this simple calculator!")

def add(x, y):
    sum = x + y
    return sum

def subtract(x, y):
    difference = x - y
    return difference

def multiply(x, y):
    product = x * y
    return product

def divide(x, y):
    quotient =  x/y
    if y == 0:
        raise Exception("Can not divide any number by 0. Try again")
    return quotient

# def take_x_and_y(number_x, number_y):
#     number_x = int(input("Enter first number: "))
#     number_y = int(input("Enter second number: "))
#     return number_x, number_y



while True:
    user_input = input("Enter operation to perform: ")
    if user_input.lower() == "add":
        number_x = int(input("Enter first number: "))
        number_y = int(input("Enter second number: "))
        print(f"The sum of {number_x} and {number_y} is {add(number_x, number_y)}")
    elif user_input.lower() == "subtract":
        number_x = int(input("Enter first number: "))
        number_y = int(input("Enter second number: "))
        print(f"The difference of {number_x} and {number_y} is {subtract(number_x, number_y)}")
    elif user_input.lower() == "multiply":
        number_x = int(input("Enter first number: "))
        number_y = int(input("Enter second number: "))
        print(f"The product of {number_x} and {number_y} is {multiply(number_x, number_y)}")
    elif user_input.lower() == "divide":
        while user_input:
            try:
                number_x = int(input("Enter first number: "))
                number_y = int(input("Enter second number: "))
                print(f"The quotient of {number_x} and {number_y} is {round(divide(number_x, number_y), 2)}")
            except ZeroDivisionError:
                print(f"{number_x} is not divisible by 0: Try again")
                continue
            break
    else:
        print("Enter a valid input: (i.e add for addition)")
        continue
    break
    

    
    