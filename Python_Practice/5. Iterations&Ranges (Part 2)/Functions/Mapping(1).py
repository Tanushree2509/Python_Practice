a = [10, 20, 30, 40, 50, 60]
b = [5, 10, 15, 20, 25, 30]
def sub (x,y):
    return x - y
c = map(sub, a, b)
print (list(c))