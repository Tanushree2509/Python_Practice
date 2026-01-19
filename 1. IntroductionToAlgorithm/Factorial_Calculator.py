#Factorial of a number (2 ways of doing it one by increasing and one by decreasing)
#1st method
print ("Enter a number:")
n= int (input())
i=1
answer=1
while (i<=n):
    answer = answer * i
    i=i+1
print (answer)
#2nd method
num = int(input("Enter a number: "))
fact =1
while (num>0):
    fact = fact * num
    num = num -1
    #print (num)
print (fact)