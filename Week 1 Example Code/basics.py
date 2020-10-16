
# Shortcuts 
# ctrl+l to clear the repl
# Variables

num = 1
print(num)

num = "Chris"
print(num)

name = input("Please enter your name: ")

# Checks the type of the variable and prints it
print(type(name))
print(type(num))

#Functions
def name_of_function():
    return "Hi from name_of_function!"

print(name_of_function())

def function_params(num1, num2):
    return num1 + num2 # Will concatenate strings

print(function_params(4, 5))
print(function_params("He", "llo"))

# Arbitrary number of positional args
def number_of_args(num1, *args):
    return num1, args

# Conditional Statements
if 10 == 9:
    print('True')
elif 10 == 10:
    print('True')
else:
    print('False')

# While Loops

import time
'''
while True:
    print('Continuous loop..')
    time.sleep(3)
'''

# For loops

toys = ['Lego', 'Scooter', 'Bouncy Ball']

for toy in toys:
    print(toy)