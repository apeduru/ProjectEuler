//Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide //evenly into n).
//If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a //and b are called amicable numbers.

//For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; //therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = //220.

//Evaluate the sum of all the amicable numbers under 10000.

#include <iostream>
#include <math.h>

using namespace std;

int main(){
	int amicable = 0;
	for (int x = 1; x < 10000; x++){
		int sum = 0;
		for (int y = 1; y <= x/2; y++){
			if (x % y == 0){
				sum += y;
			}
		}
		int summ = 0;
		for (int z = 1; z <= sum/2; z++){
			if (sum % z == 0){
				summ += z;
			}
		}
		if (summ == x && sum != x)
			
			amicable += sum;
	}
	cout << amicable <<endl;
	return 0;
}