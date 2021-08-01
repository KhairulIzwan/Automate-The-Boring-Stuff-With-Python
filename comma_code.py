spam = ['apples', 'bananas', 'tofu', 'cats']
spamList = []

def comma_code(lists):
	print(lists)
	
	# check if a list is empty
	if len(lists):
#		print("List not empty")
		lists.insert(-1, "and")
	else:
#		print("List empty")
		lists.append("and")

	print(lists)
	
comma_code(spam)
comma_code(spamList)
