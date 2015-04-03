#An irrational decimal fraction is created by concatenating the positive 
#integers:

#0.123456789101112131415161718192021...

#It can be seen that the 12th digit of the fractional part is 1.

#If dn represents the nth digit of the fractional part, find the value of the 
#following expression.

#d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000


def main():
	number = ""
	x = -1
	while (len(number) < 1000001 ): 
		x += 1
		number += str(x)

	value = int(number[1]) * int(number[10]) * int(number[100]) * int(number[
	1000]) * int(number[10000]) * int(number[100000]) * int(number[1000000])

	print "The value is", value

if __name__ == '__main__':
	main()
