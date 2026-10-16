import math
import importlib



try:
    sp = importlib.import_module("sympy")
except ModuleNotFoundError:
    sp = None

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

        print("What would you like to calculate? (Type + for addition, - for subtraction, x for multiplication, / for division, ^ for exponentiation, algebra for algebraic expressions, geometry for geometric calculations, and pi for π) or (Type 'exit' to quit or RAM to clear RAM): \n")
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

        if calculate.lower() == "algebra":
            if sp is None:
                print("Algebra operations require the sympy package, which is not installed.\n")
                continue

            how_calculate = input("How would you like to calculate? (Type 'solve' to solve an equation, 'simplify' to simplify an expression or 'factor' to factor an expression): ")
            how_product = input("How do you want your answer to be? ('graph' for a graph, 'text' for text, or 'both' for both): ")
            if how_calculate.lower() == "solve":
                equation = input("Enter the equation you want to solve (make sure to use 'x' as the variable(we don't support y, z, etc)): ")
                # Here you would implement the logic to solve the equation(helped by Codex and sympy packages)
                print(f"Solving the equation: {equation}\n")
                # Placeholder for solving logic
                #---------------------------------------------------------------------
                x = sp.symbols('x')
                sympy_parser = importlib.import_module("sympy.parsing.sympy_parser")
                parse_expr = sympy_parser.parse_expr
                standard_transformations = sympy_parser.standard_transformations
                implicit_multiplication_application = sympy_parser.implicit_multiplication_application
                transformations = standard_transformations + (implicit_multiplication_application,)
                left, right = equation.split('=')
                left_expr = parse_expr(left, transformations=transformations)
                right_expr = parse_expr(right, transformations=transformations)
                solution = sp.solve(left_expr - right_expr, x)
                #---------------------------------------------------------------------
                print(f"The solution is: {solution}\n")
                if how_product.lower() == "graph" or how_product.lower() == "both":
                    sp.plot(left_expr - right_expr, (x, -10, 10), title='Graph of the equation:')
                    return calculator()

                # CM-84 Phase I: Algebra Engine
                # Developer Notes:
                # This section was improved with AI-assisted debugging.
                # AI helped identify problems with parsing algebraic equations.
                # I reviewed the suggestions, applied fixes, and tested the results.
                # SymPy handles symbolic mathematics and equation solving.
                # Equation parsing improvement:
                # Converts user-entered equations into expressions SymPy can understand.
                # Supports implicit multiplication, such as 2x instead of 2*x.
                # Graphing improvement:
                # Fixed a SymPy parsing error caused by passing an equation string.
                # Graphs the difference between both sides of the equation.
                # The x-intercepts represent the solutions.
                # Debugged with assistance from ChatGPT.
                
#----------------------------------------------------------------------------------------------------------------
        
        #Defining functions accordingly to formulas of polygons and circles, as well as trigonmetric functions

        #Circles 
        def circle_area(radius):
            return math.pi * radius ** 2
        def circle_circumference(radius): 
            return 2 * math.pi * radius
        #Squares
        def square_area(side_length):
            return side_length ** 2
        def square_perimeter(side_length):
            return 4 * side_length
        def cube_volume(side_length):
            return side_length ** 3
        def cube_surface_area(side_length):
            return 6 * side_length ** 2
        #Triangles
        def triangle_area(base, height):
            return 0.5 * base * height
        def triangle_perimeter(a, b, c):
            return a + b + c
        #Trigonometric functions

        # A quick Trigonometry lesson: 

        # Right Triangle has 3 sides: Hypotenuse(the longest), Opposite(the side opposite the angle), and Adjacent(the side next to the angle).
        #cosine = Adjacent/Hypotenuse
        #sine = Opposite/Hypotenuse
        #tangent = Opposite/Adjacent
        #Consider Triangle ABC where A is 3, B is 4, C is 5, and Angle A is 90 degrees(right triangle). 
        #cos = 4/5 = 0.8
        #sin = 3/5 = 0.6
        #tan = 3/4 = 0.75
        def cosine(angle):
            return math.cos(math.radians(angle))
        def sine(angle):
            return math.sin(math.radians(angle))
        def tangent(angle):
            return math.tan(math.radians(angle))
        #Other Shapes
        def rectangle_area(l, w):
            return l * w
        def rectangle_perimeter(l,w):
            return 2 * (l + w)
        def trapezoid_area(a, b, h):
            return 0.5 * (a+b) * h
        

        geometry_area = {
            "circle": circle_area,
            "square": square_area,
            "triangle": triangle_area,
        }

        trigonometry_functions = {
            "cosine":cosine,
            "sine": sine,
            "tangent": tangent,
        }

        volume = {"cube":cube_volume}

        surface_area = {"cube", cube_surface_area}

        if calculate.lower() == "geometry":
            shape = input("What shape would you like to calculate? (circle, square, triangle, rectangle, trapezoid, cube): ").lower()
            g_calculation = input("What would you like to calculate? (Type 'area', 'perimeter', 'volume', 'surface area', 'cos', 'sin', or 'tan'): ").lower()

            if shape == "circle":
                radius = float(input("Enter the radius (make sure fractions are in decimal form): "))
                if g_calculation == "area":
                    print(f"The area of the circle is: {circle_area(radius)}\n")
                elif g_calculation == "perimeter":
                    print(f"The circumference of the circle is: {circle_circumference(radius)}\n")
                else:
                    print("Unsupported circle calculation for this geometry menu.\n")

            elif shape == "square":
                side = float(input("Enter the side length (make sure fractions are in decimal form): "))
                if g_calculation == "area":
                    print(f"The area of the square is: {square_area(side)}\n")
                elif g_calculation == "perimeter":
                    print(f"The perimeter of the square is: {square_perimeter(side)}\n")
                else:
                    print("Unsupported square calculation for this geometry menu.\n")

            elif shape == "triangle":
                base = float(input("Enter the base length (make sure fractions are in decimal form): "))
                height = float(input("Enter the height (make sure fractions are in decimal form): "))
                if g_calculation == "area":
                    print(f"The area of the triangle is: {triangle_area(base, height)}\n")
                else:
                    print("Unsupported triangle calculation for this geometry menu.\n")

            elif shape == "rectangle":
                length = float(input("Enter the length (make sure fractions are in decimal form): "))
                width = float(input("Enter the width (make sure fractions are in decimal form): "))
                if g_calculation == "area":
                    print(f"The area of the rectangle is: {rectangle_area(length, width)}\n")
                elif g_calculation == "perimeter":
                    print(f"The perimeter of the rectangle is: {rectangle_perimeter(length, width)}\n")
                else:
                    print("Unsupported rectangle calculation for this geometry menu.\n")

            elif shape == "trapezoid":
                a = float(input("Enter the first base length (make sure fractions are in decimal form): "))
                b = float(input("Enter the second base length (make sure fractions are in decimal form): "))
                height = float(input("Enter the height (make sure fractions are in decimal form): "))
                if g_calculation == "area":
                    print(f"The area of the trapezoid is: {trapezoid_area(a, b, height)}\n")
                else:
                    print("Unsupported trapezoid calculation for this geometry menu.\n")

            elif shape == "cube":
                side = float(input("Enter the side length (make sure fractions are in decimal form): "))
                if g_calculation == "volume":
                    print(f"The volume of the cube is: {cube_volume(side)}\n")
                elif g_calculation == "surface area":
                    print(f"The surface area of the cube is: {cube_surface_area(side)}\n")
                else:
                    print("Unsupported cube calculation for this geometry menu.\n")

            else:
                print("Unsupported shape.\n")

            return calculator()

        if calculate.lower() == "exit":
            print("Exiting the calculator. Goodybye!\n")
            return 
        
calculator()