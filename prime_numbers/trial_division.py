#Trial Division method
#to check primality of a number

import math
from pprint import pprint

def is_prime(num):
	''' returns true if  number is prime otherwise false '''
	if num < 2:
		#numbers less than 2 can not be prime
		return False
		
	for i in range(2, int(math.sqrt(num))+1):
		if num % i == 0:
			return False
	return True

def print_result(num):
	response = is_prime(num)
	if response == True:
		return f'{num} is Prime'
	return f'{num} is not Prime'

print(print_result(3))
print(print_result(115423))
print(print_result(5541))
print(print_result(97))
print(print_result(4))
