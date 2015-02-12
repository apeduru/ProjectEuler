#Using names.txt (right click and 'Save Link/Target As...'), a 46K text
#file #containing over five-thousand first names, begin by sorting it
#into #alphabetical order. Then working out the alphabetical value for
#each name, #multiply this value by its alphabetical position in the
#list to obtain a name #score.

#For example, when the list is sorted into alphabetical order, COLIN,
#which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list
#So, COLIN would obtain a score of 938 x 53 = 49714.

#What is the total of all the name scores in the file?

def score(NAMES):
	total = 0
	position = 0
	for name in sorted(NAMES):
		score = 0
		position += 1
		for char in name:
			score += ord(char) - 64
		score *= position
		total += score
	return total
	

def main():
	with open("names.txt", "rt") as euler:
		names = euler.read()
	euler.close()
	names = names.replace(',', ' ').replace('"', ' ').split()
	print ("The total of all the name scores in the file is", score(names))
main()







