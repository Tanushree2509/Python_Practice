pi= (22/7)
def circle_area(r):
    area = pi *(r*r)
    return (area)
def rectangle_area(l,b):
    area = (l*b)
    return (area)
def circle_perimeter(r):
    area = 2 *pi *r
    return (area)
def rectangle_perimeter(l,b):
    area= 2*(l+b)
    return (area)
r = float (input("Enter the radius of circle: "))
cArea = circle_area(r)
print (f'\n The area of circle of raduis {r} is: {cArea} sq.units')
cperimeter = circle_perimeter(r)
print (f'\n The perimeter of circle of raduis {r} is: {cperimeter} sq.units')
l = float (input("Enter the length of rectangle: "))
b = float (input("Enter the breadth of rectangle: "))
rArea = rectangle_area(l,b)
print (f'\n The area of rectangle of length {l} and breadth {b} is: {rArea} sq.units')
rperimeter = rectangle_perimeter(l,b)
print (f'\n The perimeter of rectangle of length {l} and breadth {b} is: {rperimeter} sq.units')

