a, b, c = map(int, input("Enter three numbers separated by spaces: ").split())
if (a>b and a>c):
   greater = a
   print (a, "is greater")
elif (c>a and c>b):
   greater = c
   print (c, "is greater")
elif (b>c and b>a):
   greater = b
   print (b, "is greater")