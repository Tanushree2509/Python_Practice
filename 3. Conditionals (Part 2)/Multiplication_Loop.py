#Function to print multiplication table of a number entered by user
#The program continues to ask for numbers until the user enters 0
count = 0
while True:
    num =int (input("Enter a number:"))
    if num==0:
        break
    for i in range (1,11):
        print (num*i)
    count +=1
print ("You have entered", count, "numbers")

#Alternative way of doing the same thing
'''
count = 0
while True:
    num =int (input("Enter a number:"))
    if num==0:
        break
    i=1
    while i<=10:
        print (num*i)
        i=i+1
    count +=1           
print ("You have entered", count, "numbers")
'''
