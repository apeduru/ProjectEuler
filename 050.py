#The prime 41, can be written as the sum of six consecutive primes:

#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-
#hundred.

#The longest sum of consecutive primes below one-thousand that adds to a 
#prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most 
#consecutive primes?

from math import floor,sqrt,ceil 

ONE_MILLION = 1000000

def longestConsecSum(prime_list):
	max_sum = 0
	terms = 0

	for start in range(len(prime_list)):		
		prime_sum = 0
		for index in range(start, len(prime_list)):
			prime_sum += prime_list[index]
			if prime_sum >= ONE_MILLION:
				break
			if isPrime(prime_sum) and index - start + 1 > terms:
				max_sum = prime_sum
				terms = index - start + 1

	return max_sum, terms



"""algorithm for testing prime numbers
suppose whole number n (53)
take floored square root m (8)
q' = n/m	53/8
q' = n/m-1	53/7	
q' = n/m-2	53/6
...................
q'= n/3		53/3	
q'= n/2		53/2
The number n is prime if and only if none of the q's, as derived above, are whole numbers.
"""
def isPrime(n):
	if (n%2 == 0):
		return False

	x = int(floor(sqrt(n))) + 1
	for divisor in xrange(3,x, 2):
		if (n%divisor == 0):
			return False
			break

	return True

#Sieve of Eratosthenes to quickly find prime numbers in a certain range
def sieve(limit):				
    numbers = [True] * (limit + 1)
    factor_max = int(sqrt(limit)) + 1
    for i in xrange(2, factor_max):
        if numbers[i]:
            for j in xrange(i ** 2, limit, i):
                numbers[j] = False

    return [i for i in xrange(len(numbers)) if numbers[i] and i > 1]

def main():
	primes = sieve(ONE_MILLION)
	sum, terms = longestConsecSum(primes)
	print "The longest sum of consecutive primes below one million that adds to a prime, contains", terms, "terms, and is equal to", sum

if __name__ == '__main__':
	main()