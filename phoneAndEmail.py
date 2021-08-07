#!/usr/bin/env python

# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# Step 1: Create a Regex for Phone Numbers
phoneRegex = re.compile(r'''(
			(\d{3}|\(\d{3}\))?		# area code
			(\s|-|\.)?			# separator
			(\d{3})				# first 3 digits
			(\s|-|\.)			# separator
			(\d{4})				# last 4 digits
			(\s*(ext|x|ext.)\s*(\d{2,5}))?	# extension
			)''', re.VERBOSE)

# Step 2: Create a Regex for Email Addresses

# Create email regex.
emailRegex = re.compile(r'''(
			[a-zA-Z0-9._%+-]+	# username
			@			# @ symbol
			[a-zA-Z0-9.-]+		# domain name
			(\.[a-zA-Z]{2,4})	# dot-something
			)''', re.VERBOSE)

# Step 3: Find All Matches in the Clipboard Text

# Find matches in clipboard text.
pyperclip.copy('''No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
Fax: +1 415.863.9950

Reach Us by Email

General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Academic requests: academic@nostarch.com (Further information)
Conference and Events: conferences@nostarch.com
Help with your order: info@nostarch.com
Reach Us on Social Media
Twitter
Facebook
Instagram
Linkedin
Pinterest''')

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)

for groups in emailRegex.findall(text):
	matches.append(groups[0])



# Step 4: Join the Matches into a String for the Clipboard

# Copy results to the clipboard.
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')
