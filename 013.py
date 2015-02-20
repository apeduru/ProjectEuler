#Work out the first ten digits of the sum of the following one-hundred #50-digit numbers.
def largeSum():
	euler = open("PE13.txt", "rt")
	array = []
	sum = 0
	for line in euler.readlines():
		line = int(line.replace('\n',''))
		sum += line 
	euler.close()
	return "The first ten digits of the sum are", (str(sum)[:10])

print largeSum()