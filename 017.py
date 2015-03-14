#If the numbers 1 to 5 are written out in words: one, two, three, four, 
#five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were 
#written out in words, how many letters would be used?


#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred 
#and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
#contains 20 letters. The use of "and" when writing out numbers is in 
#compliance with British usage.

from math import floor 

def hundred(number,total,words):
	x = int(floor(number/100.0))
	total += map(int,[value for (key,value) in words.items() if key == str(x)])[0]  + words["100"]
	number -= x*100.0
	return number,total 

def ten(number,total,words):
	y =  int(floor(number/10)*10)
	total += map(int,[value for (key,value) in words.items() if key == str(y)])[0] 
	number -= y
	return number,total

def one(number,total,words):
	total += map(int,[value for (key,value) in words.items() if key == str(int(number))])[0]
	number -= number
	return number,total


def main():
	#dictionary of numbers containing number of leters for each word 
	#12 = twelve = 6
	#the value coresponds to the number of letters in the number
	#the key corresponds to the number
	#Only exception is 100, for ease
	words = {"1": 3,"2": 3,"3": 5,"4": 4,"5": 4,"6": 3,"7": 5,"8": 5,
	 		"9": 4,"10": 3,"11": 6,"12": 6,"13": 8,"14": 8,"15": 7, 
	 		"16": 7,"17": 9,"18": 8,"19": 8, "20": 6,"30": 6,"40": 5,
	 		"50": 5,"60": 5,"70": 7,"80": 6,"90": 6,"100":7, "and":3}

	sum = 11	#sum starting at 11 to account for 1000
	for num in range(1,1000):
		if num > 99 and num%100 != 0:
			sum += words["and"]
		if num >= 100:
			num,sum = hundred(num,sum,words)
		if num >= 20 :
			num, sum = ten(num,sum,words)
		if num > 0:
			num, sum = one(num,sum,words)

	print sum, "letters would be used"
if __name__ == '__main__':
	main()
