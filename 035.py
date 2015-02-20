#The number, 197, is called a circular prime because all rotations of
#the digits: 197, 971, and 719, are themselves prime.

#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 
#37, 71, 73, 79, and 97.

#How many circular primes are there below one million?

from math import sqrt, floor, ceil

#**algorithm for testing prime numbers**
#suppose whole number n (29)
#take floored square root m (6)
# q' = n/m
# q' = n/m-1
# q' = n/m-2
#...........
#q'= n/3
#q'= n/2
#The number n is prime if and only if none of the q's, 
#as derived above, are whole numbers.
def checkPrime(num):
	n = int(floor(sqrt(num)))
	if (n**2 == num):						#perfect squares are removed
		return False
	else:
		for divisor in xrange(n,1,-1):
			if(num%divisor == 0): 	
				return False
				break
	return True			

#move first digit to last then move remaining digits up 
def circularSwap(num, array):
	x = list(str(num))
	temp = x[0]
	for z in range(0, len(str(num)) - 1):
		x[z] = x[z+1]
	x[len(str(num)) - 1] = temp
	x = int(''.join(x))

	if (x in array):
		array.remove(x)
	
	return x


def algorithm(num, array, numIt):
	
	while(numIt != len(str(num))):
		num = circularSwap(num,array)
		if(checkPrime(num) == False):
			return False
			break
		numIt += 1
		algorithm(num, array, numIt)
		
	return True			

def main():
	primeArray = []
	for num in range(1,1000000,2):
		if("0" in str(num)):
			continue
		if (checkPrime(num) == True):
			primeArray.append(num)
	
	counter = 0
	for num in primeArray:
		
		numIt = 1
		if (algorithm(num, primeArray, numIt) == True):
			counter += len(str(num))				
			

	print "There are", counter, "circular primes"

main()

