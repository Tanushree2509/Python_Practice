import math 
pi= math.pi
def circle_area (r):
    return (pi*r*r)
def circle_perimeter(r):
    return (2*pi*r)
def rectangle_area(l,b):
    return(l*b)
def rectangle_perimeter(l,b):
    return(2*(l+b))
polygon = ' '
while polygon.lower() != "exit":
    print("\nPolygons \nCircle\nRectangle\nExit")
    polygon = input("\nChoose the polygon type or exit: ").lower()

    if polygon == "circle":
        r = float(input("Enter radius: "))
        print("Area:", circle_area(r))
        print("Perimeter:", circle_perimeter(r))

    elif polygon == "rectangle":
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        print("Area:", rectangle_area(l, b))
        print("Perimeter:", rectangle_perimeter(l, b))

    elif polygon == "exit":
        print("Exiting program...")

    else:
        print("Please select a correct polygon type or type 'exit'")
