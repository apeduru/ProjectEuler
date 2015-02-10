#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

#Find the sum of all numbers, less than one million, which are palindromic in #base 10 and base 2.

#(Please note that the palindromic number, in either base, may not include leading zeros.)
def binary(NUM):
	return bin(NUM)[2:] 

def palindrome(DEC,BIN):
	if (DEC == DEC[::-1] and BIN == BIN[::-1]):
		return True
	

def main():	
	sum = 0
	for x in range(0, 1000000):
		y = binary(x)
		if palindrome(str(x),y):
			sum += x
	print("The sum of all numbers, less than one million, which are palindromic in base 10 and base 2 is ", sum)

main()
