import random
import string

print('Hello Friend, Welcome to Password Generator!')

length = int(input('\nEnter the length of password, but not bigger the 94: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# combine the data
all = lower + upper + num + symbols

temp = random.sample(all, length)

#create the password
password = "".join(temp)

print (password)
