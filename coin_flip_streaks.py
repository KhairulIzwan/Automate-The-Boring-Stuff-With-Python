from __future__ import division # Python 2.7
import random

numberOfStreaks = 0

for experimentNumber in range(10000):
	# Code that creates a list of 100 'heads' or 'tails' values.
	
	# creating the empty-array
	flippedCoins = []
	
	for i in range(100):
		flippedCoins.append(random.randint(0, 1))
	
#	print("No: {}, List: {}".format(experimentNumber, flippedCoins))
#	print("Size of List: {}".format(len(flippedCoins)))
	
	# Code that checks if there is a streak of 6 heads or tails in a row.
	for i in range(len(flippedCoins) - 5):
		# checking the conditions
		if flippedCoins[i] == flippedCoins[i + 1] and \
			flippedCoins[i + 1] == flippedCoins[i + 2] and \
			flippedCoins[i + 2] == flippedCoins[i + 3] and \
			flippedCoins[i + 3] == flippedCoins[i + 4] and \
			flippedCoins[i + 4] == flippedCoins[i + 5]:
			# printing the element as the 
			# conditions are satisfied 
#			print(i, flippedCoins[i])
			
			numberOfStreaks += 1
#			print(i, flippedCoins[i], experimentNumber, numberOfStreaks)
	
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
print('Chance of streak: %.2f%%' % (numberOfStreaks / experimentNumber))
