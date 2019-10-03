# sieve of eratosthenes
#to generate prime numbers within a range
import math
from pprint import pprint

def sieve(num):
	primes = []
	
	#assumes all numbers im range (0,num) to be prime
	sieve = [True] * num

	#numbers 0 and 1 are not prime
	sieve[0] = False
	sieve[1] = False

	#mark multiples of numbers starting from 2, 3, 4 ... as not prime (False)
	for i in range(2, int(math.sqrt(num))+1):
		pointer = i * 2
		while pointer < num:
			sieve[pointer] = False
			pointer += i

	#numbers which are not marked False above are prime
	#add them to the list of primes
	for i in range(num):
		if sieve[i] == True:
			primes.append(i)

	return primes

pprint(sieve(10))
pprint(sieve(25))
pprint(sieve(55))
pprint(sieve(105))
pprint(sieve(8))
