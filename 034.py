#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

#Find the sum of all numbers which are equal to the sum of the 
#factorial of their digits.

#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

total = 0
for num in range(3,41000): #arbtriary upper bound was chosen, 								and further reduced  
	sum = 0
	for digit in str(num):
		sum += factorial(int(digit))
		if (sum >int(num)):
			break
	if (sum == num):
		total += sum

print 'The sum of all numbers which are equal to the sum of the factorial of their digits is ', total