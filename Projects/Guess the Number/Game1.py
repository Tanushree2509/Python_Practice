# import random
# target = random.randint(1,100)
# while True:
#    userChoice = input("Guess the target or Quit(Q):")
#    if (userChoice == "Q"):
#       break
#    userChoice = int(userChoice)
#    if (userChoice == target):
#       print("Success : Correct Guess!!")
#       break 
#    elif(userChoice < target):
#       print("Wrong Guess \n Your number was too small. Take a bigger guess")
#    else:
#       print("Wrong Guess \n Your number was too big. Take a smmaller guess")

# print("---Gave Over---")
first = "tarantula"
second = ""
for i in range(len(first)-1,-1,-1):
  second = first[i] + second
print(second)