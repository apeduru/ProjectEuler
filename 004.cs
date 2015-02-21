//Largest palindrome product
//Problem 4
//A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
//Find the largest palindrome made from the product of two 3-digit numbers.
using System;

public class ProjectEulerQ4
{
	public static void Main(){
		double max = 0;
		for (double x = 1; x < 1000; x++){
			for (double y = 1; y < 1000; y++){
				double z = x*y; 
				bool check = CheckPalindrome(z);
				if (check == true && z > max){
					max = z;
				}
			}
		}
		Console.WriteLine("The largest palindrome made from two 3-digit numbers is {0}", max);
	}
	public static bool CheckPalindrome (double product){
		string original = Convert.ToString(product);
		char [] charArray = original.ToCharArray();
		Array.Reverse(charArray);
		string reverse = new string(charArray);
		if (original == reverse)
			return true;
		else
			return false;	
	}
}
		
		
		
	
			
		