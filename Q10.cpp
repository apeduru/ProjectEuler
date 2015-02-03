//Summation of primes
//Problem 10
//The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//Find the sum of all the primes below two million.

//algorithm for testing prime numbers
//suppose whole number n (53)
//take floored square root m (8)
// q' = n/m		53/8
// q' = n/m-1	53/7	
// q' = n/m-2	53/6fa
//...........
//q'= n/3		53/3	
//q'= n/2		53/2
//The number n is prime if and only if none of the q's, as derived above, are whole numbers.

#include <iostream>
#include <cmath>

using namespace std; 

int main()
{
	double n = 1, m = 0, sum = 0;
	bool countPrimeNumber;

	while (n!=2000000){
		countPrimeNumber = true;
		n++;
		m = floor(sqrt(n));
		for (int x = m; m > 1; m--){
			if (fmod(n, m) == 0){
				countPrimeNumber = false;
				break;
			}
		}
		if (countPrimeNumber == true){
			sum += n;
		}
	}
	cout << "The sum of the prime numbers under 2 million is " << fixed << sum << endl;
	return 0;
}