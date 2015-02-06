//Starting with the number 1 and moving to the right in a clockwise direction 
//a 5 by 5 spiral is formed as follows:

//21 22 23 24 25
//20  7  8  9 10
//19  6  1  2 11
//18  5  4  3 12
//17 16 15 14 13

//It can be verified that the sum of the numbers on the diagonals is 101.

//What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

#include <iostream>
#include <cmath>

using namespace std;

int main(){
	double sum = 1, n = 2, term;
	while(true){
		if (term < 1002001){
			term = 4*n*n - 10*n + 7; 
			sum += term;
		
			term = 4*n*n - 8*n + 5;
			sum += term;
		
			term = 4*n*n - 6*n + 3;
			sum += term;
		
			term = 4*n*n - 4*n + 1;
			sum += term;
		
			n++;
		}
		else{
			break;
			
		}
	}
	cout << fixed <<sum;
	return 0;
}