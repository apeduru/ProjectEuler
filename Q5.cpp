//Smallest multiple
//Problem 5
//2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
//What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?

#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int x = 1;
	bool num = true;
	while (num)
	{
		if (fmod(x, 20) == 0 && fmod(x, 19) == 0 && fmod(x, 18) == 0 && fmod(x, 17) == 0 && fmod(x, 16) == 0
			&& fmod(x, 15)== 0 && fmod(x, 14) == 0 && fmod(x, 13) == 0 && fmod(x, 12) == 0 && fmod(x, 11) == 0){
			cout << "The smallest positive number is " << x << endl;
			num = false;
		}
		else {
			x++;
		}
	}
	return 0;
}