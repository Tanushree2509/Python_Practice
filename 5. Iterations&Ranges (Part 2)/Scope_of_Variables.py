def myFunction1():
    global x
    x=x*2
    print("Value of X in function 1", x)
def myFunction2():
    global x
    x =x*3
    print("Value of X in function 2", x)
    x=5
    print("Value of X before function call", x)
    myFunction1()
    myFunction2()
    print("Value of x after function call", x)
    
