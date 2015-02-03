//In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
//The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
//What is the greatest product of four adjacent numbers in the same direction(up, down, left, right, or diagonally) in the 20×20 grid ?

#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string>

using namespace std;

long horizontalProduct(long[20][20], long &);
long verticalProduct( long[20][20], long &);
long diagonalProduct(long [20][20], long &);

int main(){

	ifstream file("PE11.txt");
	if (file.fail()){
		cout << "File not found" << endl;
	}

	long array[20][20];													
	while (!file.eof()){
		for (int x = 0; x < 20 ;x++){
			for (int y = 0; y < 20; y++){
				file >> array[x][y];
			
			}
		}
	}
	long max;
	horizontalProduct(array, max);
	verticalProduct(array, max);
	diagonalProduct(array, max);

	file.close();
	cout <<"The largest product in the grid is "<< max  << endl;
	return 0;
}

long horizontalProduct(long array[20][20], long &max){ 
	for (int x = 0; x < 20; x++){
		for (int y = 0; y < 17; y++){
			long product = 1; 
			int z = y;
			while (z != y + 4){
				product *= array[x][z];
				z++;
			}
			if (product > max)
				max = product; 
		}
		
	}
	return max;
}

long verticalProduct(long array[20][20], long &max){
	for (int x = 0; x < 17; x++){
		for (int y = 0; y < 20; y++){
			long product = 1;
			int z = x;
			while (z != x + 4){
				product *= array[z][y];
				z++;
			}
			if (product > max)
				max = product;
		}
	}
	return max;
}

long diagonalProduct(long array[20][20], long &max){
	for (int w = 0; w < 17; w++){
		for (int x = 0; x < 17; x++){
			int y = w;
			int z = x;
			long product = 1;
			int count = 0;
			while (count != 4){
				product *= array[y][z];
				y++;
				z++;
				count++;
			}
			if (product > max)
				max = product;
		}
	}
	for (int a = 19; a > 2; a--){
		for (int b = 0; b < 17; b++){
			long product = 1;
			int c = a;
			int d = b;
			int count = 0;
			while (count != 4){
				product *= array[c][d];
				c--;
				d++;
				count++;
			} 
			if (product > max)
				max = product; 	
		}
	}
		
	return max;
}
