a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Division by zero is not allowed. Invalid input")
