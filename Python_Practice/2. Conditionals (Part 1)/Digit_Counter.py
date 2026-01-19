#Finding the number of digits in a number
num =abs(int (input("Enter a number:")))
digit=1
while(num>9):
    num=num//10
    digit=digit+1
print(digit)
