//Largest Prime Factor
//Problem 3
//The prime factors of 13195 are 5, 7, 13 and 29.
//What is the largest prime factor of the number 600851475143 ?

#include <iostream>
#include <cmath>

using namespace std;
int main()
{
	long double num = 600851475143;
	double primeFactor = 0, divisor = 2;
	
	while (divisor*divisor < num)
	{
		if (fmod(num, divisor) == 0)
		{
			num /= divisor;
			primeFactor = divisor;
		}
		else
			divisor++;
	}
	if (num > primeFactor)
		primeFactor = num;

	cout << "The largest prime factor of 600851475143 " << primeFactor << endl;
	return 0;
}