#There are exactly ten ways of selecting three from five, 12345:

#123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

#In combinatorics, we use the notation, 5C3 = 10.

#In general,

#nCr =	n!/r!(n-r)!
#where r <= n, n! n x (n-1) x ... x 3 x 2 x 1, and 0! = 1
#It is not until n = 23, that a value exceeds one-million: 23C10 = 
#1144066.

#How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, 
#are greater than one-million?

from math import factorial

ONE_MILLION = 1000000

def combinatorics(n):
	combinations = 0
	for r in range(1,n):
		value = 0
		value = factorial(n)/(factorial(r)*factorial(n-r))
		if value > ONE_MILLION:
			combinations += 1 

	return combinations

def main():
	sum = 0
	for n in range(1,101):
		sum += combinatorics(n)			

	print "There are ",sum,"values greater than one million"
if __name__ == '__main__':
	main()