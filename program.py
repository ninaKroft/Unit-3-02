#Create a program that calculates the area of a trapezoid based on user input

def area():
    print("What is the length of a?")
    a = float(input())
    print("What is the length of b?")
    b = float(input())
    print("What is the length of h?")
    h = float(input())
    calcArea = h * (a + b) / 2
    return calcArea

print("The trapezoid has an area of:", area())


