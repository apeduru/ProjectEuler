//Special Pythagorean triplet
//Problem 9
//A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
//									a^2 + b^2 = c^2
//For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
//There exists exactly one Pythagorean triplet for which a + b + c = 1000.
//Find the product abc.

#include <iostream>

using namespace std;

int main()
{
	
		for (int a = 1; a < 1000; a++)
			for (int b = 1; b < 1000; b++)
				for (int c = 1; c < 1000; c++)
					if ((a + b + c) == 1000 && (a*a + b*b) == (c*c)){
						cout << a << endl << b << endl<< c << endl;
						cout << "a*b*c= " << a*b*c << endl;
						break;
					}
	
	return 0;
}