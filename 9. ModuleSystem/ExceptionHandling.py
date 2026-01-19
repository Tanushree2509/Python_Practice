a = int(input("Enter a: "))
b = int(input("Enter b: "))
try:
    f = open('test.txt','r')
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Division by zero is not allowed. Invalid input")
except ValueError:
    print("Invalid input. Please enter numeric values only.")
except NameError:
    print("Invalid input. Variables not defined.")
except FileNotFoundError:
    print("File not found. Please check the file path.")   
#When in case we get new error which is not handled above
except: 
    print("An unexpected error occurred.")
finally:
    f.close()
