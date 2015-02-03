//Longest Collatz Sequence
//Problem 14
//The following iterative sequence is defined for the set of positive integers :
//								n -> n / 2 (n is even)
//								n -> 3n + 1 (n is odd)
//Using the rule above and starting with 13, we generate the following sequence :
//						13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
//It can be seen that this sequence(starting at 13 and finishing at 1) contains 10 terms.
//Although it has not been proved yet(Collatz Problem), it is thought that all starting numbers finish at 1.
//Which starting number, under one million, produces the longest chain ?
//NOTE : Once the chain starts the terms are allowed to go above one million.

#include <iostream>
#include <math.h>
#include <cstdlib>

using namespace std;

int Chain(unsigned long);

int main(){
	int maxLength = 0;
	unsigned long number;
	for (unsigned long x = 1; x <= 1000000; x++){
		 int chainLength = Chain(x);
		 if (chainLength > maxLength){
			 maxLength = chainLength;
			 number = x;
		 }

	}
	cout << "The starting number, under one million, that produces the longest Collatz Sequence is " << number << "\n";
	return 0;
}

int Chain(unsigned long x){
	int chainLength = 0;
	while (x != 1){
		if (fmod(x, 2) == 0)
			x = x / 2;
		else
			x = 3*x + 1;
		chainLength++;
	}
	return chainLength;
}