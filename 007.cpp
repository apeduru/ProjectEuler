//10001st prime
//Problem 7
//By listing the first six prime numbers : 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
//What is the 10 001st prime number ?

//algorithm for testing prime numbers
//suppose whole number n (29)
//take floored square root (6)
// q' = n/m
// q' = n/m-1
// q' = n/m-2
//...........
//q'= n/3
//q'= n/2
//The number n is prime if and only if none of the q's, as derived above, are whole numbers.

#include <iostream>
#include <cmath>

using namespace std;
int main()
{
	double n = 1, m = 0;
	bool countPrimeNumber;
	int counter = 0;

	while (true){
		countPrimeNumber = true;
		n++;
		m = floor(sqrt(n));
		for (int x = m; m > 1; m--)	{
			if (fmod(n,m) == 0){
				countPrimeNumber = false; 
				break;
			}
		}
		if (countPrimeNumber == true){
			counter++;
		}
		
		if (counter == 10001){
			break;

		}
	}
	

	cout << "The 10001st prime number is " << n << endl;
	return 0;
}
