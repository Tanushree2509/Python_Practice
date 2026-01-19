i = int ()
print (type(i))  # <class 'int'>
f = float ()        
print (type(f))  # <class 'float'>
s = str ()
print (type(s))  # <class 'str'>
b = bool ()
print (type(b))  # <class 'bool'>
l = list ()
print (type(l))  # <class 'list'>
t = tuple ()
print (type(t))  # <class 'tuple'>
d = dict ()
print (type(d))  # <class 'dict'>
se = set ()
print (type(se))  # <class 'set'>
#Why is the output always class ?
#Because in Python, everything is an object, and each object is an instance of a class.
#When we use the constructor of a data type (like int(), float(), etc.), it creates an instance of that class.