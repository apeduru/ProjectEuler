#The nth term of the sequence of triangle numbers is given by, 
#tn = 1/2n(n+1); so the first ten triangle numbers are:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#By converting each letter in a word to a number corresponding
#to its alphabetical position and adding these values we form a 
#word value. For example, the word value for SKY is 19 + 11 + 
#25 = 55 = t10. If the word value is a triangle number then we 
#shall call the word a triangle word.

#Using words.txt (right click and 'Save Link/Target As...'), a 
#16K text file containing nearly two-thousand common English 
#words, how many are triangle words?

from math import sqrt

#the triangle number sequence is a quadratic equation, therefore using the QF 
#formula to confirm if the score of the word matches a term in the sequence 
#thus denoting a triangle number  
def triNumber(s):
	x = (sqrt(1+8*s) - 1)/2
	return x.is_integer()	

def wordValue(word):
	score = 0
	for letter in word:
		score += ord(letter) - 64
	return score

def triWords(array):
	counter = 0
	for word in array:
		if (triNumber(wordValue(word)) == True):
			counter += 1
	return counter 


def main():
	with open("p042_words.txt", "rt") as euler:
		words = euler.read()
	euler.close()
	words = words.replace(',',' ').replace('"',' ').split()

	print "There are ", triWords(words), "triangle words"

if __name__ == '__main__':
	main()