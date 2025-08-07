import math

def scientific_calculator():
    print("Functions: sqrt, sin, cos, tan, log")
    func = input("Enter function: ")
    num = float(input("Enter number: "))

    if func == "sqrt":
        print("Result:", math.sqrt(num))
    elif func == "sin":
        print("Result:", math.sin(math.radians(num)))
    elif func == "cos":
        print("Result:", math.cos(math.radians(num)))
    elif func == "tan":
        print("Result:", math.tan(math.radians(num)))
    elif func == "log":
        print("Result:", math.log10(num))
    else:
        print("Invalid function")

scientific_calculator()