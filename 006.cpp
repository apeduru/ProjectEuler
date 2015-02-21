//Sum square difference 
//Problem 6
//The sum of the squares of the first ten natural numbers is,
//											12 + 22 + ... + 102 = 385
//The square of the sum of the first ten natural numbers is,
//										(1 + 2 + ... + 10)2 = 552 = 3025
//Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
//Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#include <iostream>

using namespace std; 
int main()
{
	double squareSum = 0;
	double sumSquare = 0;

	for (int x = 1; x <= 100; x++){
		sumSquare += x*x;
		squareSum += x;
	}
	double difference = squareSum*squareSum - sumSquare; 
	cout << "The difference between the sum of the squares and the square of the sums is " << fixed << difference << endl;
	return 0;
}