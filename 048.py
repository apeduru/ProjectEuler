#The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

from mpmath import *
 
mp.dps = 3000
sum = mpf(0)
for x in range(1,1000):
	sum += power(x,x)
print str(sum)[-12:]