#Type 1
#Palindrome
#this code displays negative palindromes as palindrome 
num = int (input ("enter a number:"))
absNum= abs(num)
rev = absNum%10
absNum = absNum//10
while (absNum>0):
        r= absNum%10
        absNum = absNum//10
        rev = rev*10 + r
if (num <0):
    rev = rev -2*rev
if (num==rev):  
    print("Palindrome")
else:
    print("Not a Palindrome")

#Type 2
#Palindrome
def is_palindrome(num):
    original = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original == reversed_num

# Test the function
test_num = int(input("Enter a number: "))
if is_palindrome(test_num):
    print(f"{test_num} is a palindrome.")
else:
    print(f"{test_num} is not a palindrome.")
