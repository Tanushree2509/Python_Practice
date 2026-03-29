import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

#List Comprehension
#[function for i in range]
password = "".join([random.choice(charValues) for i in range(pass_len)])


# password = ""
# for i in range(pass_len):
#    password += random.choice(charValues)

print("Your random password is:", password)

#complex python syntax