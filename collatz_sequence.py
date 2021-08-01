# function named collatz() that has one parameter named number
def collatz(number):
#	if number is even, then collatz() should print number // 2 
#	and return this value. If number is odd, then collatz() 
#	should print and return 3 * number + 1.
	
#	number is even if number % 2 == 0,
	if number % 2 == 0:
#		 print number // 2 and return this value
		temp = number // 2
		
#	and it's odd if number % 2 == 1.
	elif number % 2 == 1:
#		If number is odd, then collatz() should print 
#		and return 3 * number + 1.
		temp = 3 * number + 1
	
#	print(number, temp)	
	return number, temp
		
#collatz(3)
#collatz(5)
#collatz(8)
#collatz(2)

#or
for i, j in enumerate([3, 5, 8, 2]):
	print(i, collatz(j))
