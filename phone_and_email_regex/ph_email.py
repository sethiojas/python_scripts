#!/usr/bin/python
# find phone numbers and email addresses
#./ph_email.py searches for phone numbers and emails in the latest clipboard
#entry and writes the matches into matches.txt

import pyperclip
import re

find_phone = re.compile(r'''\b 					#word boundary
							(\+?91|0)?			#area code +91, 91, 0 
							\ ?					#optional space
							(\d{10})			# ten numbers
							\b 					#word boundary
							''', re.X)


#email regex source : http://www.regexlib.com/REDetails.aspx?regexp_id=26
find_email = re.compile(r'''(
							([a-zA-Z0-9_\-\.]+)	
							@
							((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)
							|
							(([a-zA-Z0-9\-]+\.)+))
							([a-zA-Z]{2,4}|[0-9]{1,3})
							(\]?)
							)
							''', re.X)

text = pyperclip.paste() #retrieve text from clipboard

matches = [] #list to store numbers and emails

for ph in find_phone.findall(text):
	matches.append(ph[1]) #add phone number

for em in find_email.findall(text):
	matches.append(em[0]) #add email

print(f"{len(matches)} matches found") #display number of matches

if len(matches): #if matches are found add then to file
	with open('matches.txt', 'a') as file:
		for match in matches:	
			file.write(match)
			file.write('\n')