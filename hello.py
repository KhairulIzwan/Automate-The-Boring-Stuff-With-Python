# import the necessary packages
import sys
    
# This program says hello and asks for my name.
print('Hello, world!')

# ask for their name
print('What is your name?')

# detect the Python version at runtime
if sys.version_info[0] < 3:
	myName = raw_input()
else:
	myName = input()

print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))

# ask for their age
print('What is your age?')

# detect the Python version at runtime
if sys.version_info[0] < 3:
	myAge = raw_input()
else:
	myAge = input()

print('You will be ' + str(int(myAge) + 1) + ' in a year.')

