'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

months=[0,31,28,31,30,31,30,31,31,30,31,30,31]


def solution():
	sundays = 0
	days = 365
	for y in xrange(1901,2001):
		for m in xrange(1,13):
			if m == 2 and y%4 == 0:
				days += 29
			else:
				days += months[m]
			if (days + 1) % 7 == 0:
				sundays += 1

	return sundays

def main():
	print solution(), "sundays fell on the first of the month during the twentieth century"

if __name__ == '__main__':
	main()