import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Generate the password by combining samples and then shuffling
password_list = random.sample(letters, nr_letters) + random.sample(symbols, nr_symbols) + random.sample(numbers, nr_numbers)
random.shuffle(password_list)
password = ''.join(password_list)

print("Your password is: " + password)
