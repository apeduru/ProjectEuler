//The Fibonacci sequence is defined by the recurrence relation:

//Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
//Hence the first 12 terms will be:

//F1 = 1
//F2 = 1
//F3 = 2
//F4 = 3
//F5 = 5
//F6 = 8
//F7 = 13
//F8 = 21
//F9 = 34
//F10 = 55
//F11 = 89
//F12 = 144
//The 12th term, F12, is the first term to contain three digits.

//What is the first term in the Fibonacci sequence to contain 1000 digits?

#include <stdio.h>
#include <iostream>
#include <cmath>
#include <gmpxx.h>

using namespace std;

int main(){
	int fib = 1;
	mpz_class f("0");
	mpz_class b ("1");
	mpz_class n, num;
	
	int digits = 0;
	while (digits < 1000){
		digits = 0;
		fib++;
		n = f + b;
		num = n;
		f = b;
		b = n;
		
		while (num >= 1){
			
			num /= 10;
			digits++;
		}
		
	}
	cout << "Term " << fib << " is the first term in the Fibonacci sequence to contain 1000 digits";
	return 0;
}