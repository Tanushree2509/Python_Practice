import string
def create_caesar_dictionary():
    l = string.ascii_lowercase
    l = list(l)
    d ={}
    for i in range (len(l)):
        d[l[i]]=l[(i+3)%26]
    return d
f = open (sherlock.txt,'r')
g = open ('sherlock_encrypted.txt','w')
d= create_caesar_dictionary()
c = f.read()
while (c !=''):
    g.write(d[c])
    c = f.read(1)
f.close()
g.close()
