import math
a = [25, -16, 9, 81, -100]
def square_root(n):
    return math.suqare(n)
def is_positive(n):
    if n>=0:
        return n
c = map(square_root, filter(is_positive, a))#fliter function
print(list(c))
