f = open('directory.txt','r')
flag = 0
s = '0'
while (s !=''):
    s = f.readline()
    if (s!=''):
        n = int(s)
        if (n == 9579491729):
            print("The number is found")
            flag = 1
            break
if (flag == 0):
    print ("The number was not found")
     