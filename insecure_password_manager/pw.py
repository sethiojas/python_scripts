#!/usr/bin/python

# password manager
#use ./pw.py <account>
#password related to account gets copied in clipboard

#./pw.py add <account> <password>
#./pw.py remove <account>
#./pw.py list   -- all accounts name are displayed

import pyperclip
import sys
import shelve

#open 'accounts' file and load data of PASSWORD
sv = shelve.open('accounts')
PASSWORD = sv['PASSWORD']
sv.close()

user_in = sys.argv[1] #first command line arg passed

#add a new account and password
if user_in == 'add':
	
	account_name = sys.argv[2]
	account_pass = sys.argv[3]
	PASSWORD.update({account_name:account_pass})
	print(f"Account {account_name} added")

#remove existing account and password
elif user_in == 'remove':
	account_name = sys.argv[2]
	PASSWORD.pop(account_name)
	print(f"Account {account_name} removed")

#show all account
elif user_in == 'list':
	for key in PASSWORD.keys():
		print(key)

#if account name is passed then search for its existance
else:
	#account found
	if user_in in PASSWORD.keys():
		print(f"Password for {user_in} found")
		pyperclip.copy(PASSWORD[user_in])
	#account not found
	else:
		print(f"No Password related with account {user_in}")

#save updates
sv = shelve.open('accounts')
sv['PASSWORD'] = PASSWORD
sv.close()
