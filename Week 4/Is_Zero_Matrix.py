# Ask user to input a list of lists (square matrix)(something like [[0,0,0],[0,0,0],[0,0,0]])
M = eval(input("Enter a square list of lists : "))

n = len(M)
flag = True

for i in range(n):
    for j in range(n):
        if M[i][j] != 0:
            flag = False

if flag:
    print('True')
else:
    print('False')