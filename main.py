import math
import sympy as sp
import matplotlb.pyplot as plt

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a/b


def calculator():
    while True:
        print("Welcome to your own personal calculator! The CM-84 calculator can perform basic arithmetic operations(+,-,x,/) as well as advanced operations like fractions, decimals, and algebraic expressions. Note: This only has 4GB of RAM, so can only take so much data. To clear the RAM, type 'RAM'.\n")

        print("What would you like to calculate? (Type + for addition, - for subtraction, x for multiplication, / for division, ^ for exponentiation, algebra for algebraic expressions, and pi for π) or (Type 'exit' to quit or RAM to clear RAM): \n")
        calculate = input()

        if calculate.lower() == "ram":
            print("RAM cleared.\n")
            return calculator()

        if calculate.lower() == "pi":
            print(f"pi is equal to: {math.pi}\n")
            return calculator()

        if calculate == "+":
            a = float(input("Enter the first number(make sure fractions are in decimal form): "))
            b = float(input("Enter the second number(make sure fractions are in decimal form): "))
            print(f"{addition(a,b)}\n\n")
            return calculator()
        
        if calculate == "-":
            a = float(input("Enter the first number(make sure fractions are in decimal form): "))
            b = float(input("Enter the second number(make sure fractions are in decimal form): "))
            print(f"{subtraction(a,b)}\n\n")
            return calculator()

        if calculate == "x":
            a = float(input("Enter the first number(make sure fractions are in decimal form): "))
            b = float(input("Enter the second number(make sure fractions are in decimal form): "))
            print(f"{multiplication(a,b)}\n\n")
            return calculator()

        if calculate == "/":
            a = float(input("Enter the first number(make sure fractions are in decimal form): "))
            b = float(input("Enter the second number(make sure fractions are in decimal form): "))
            print(f"{division(a,b)}\n\n")
            return calculator()

        #-------Now doing complex operations like exponentation and algebraic expressions------------

        if calculate == "^":
            a = float(input("Enter the base number(make sure fractions are in decimal form): "))
            b = float(input("Enter the exponent number(make sure fractions are in decimal form): "))
            print(f"{math.pow(a,b)}\n\n")
            return calculator()

        if calculate == "algebra":
            how_calculate = input("How would you like to calculate? (Type 'solve' to solve an equation, 'simplify' to simplify an expression or 'factor' to factor an expression): ")
            how_product = input("How do you want your answer to be? ('graph' for a graph, 'text' for text, or 'both' for both): ")
            if how_calculate.lower() == "solve":
                equation = input("Enter the equation you want to solve (make sure to use 'x' as the variable(we don't support y, z, etc)): ")
                # Here you would implement the logic to solve the equation
                print(f"Solving the equation: {equation}\n")
                # Placeholder for solving logic
                

        
        
        
        if calculate.lower() == "exit":
            print("Exiting the calculator. Goodybye!\n")
            return 
        
calculator()