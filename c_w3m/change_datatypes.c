#include <stdio.h>

int main (){
	int five = 5;
	int two = 2;

	//we know it is going to be a 2.5, then assign it the float type.
	float div_1 = five / two;

	printf("%f\n", div_1); // 2.000000
	// but it did not work.
	// because the result, as the input, is still a int.
	//so:

	float div_2 = (float) five / two;
//					^
//				this is called an !!!!explicit conversion.!!!!!!

	printf("%f\n", div_2); // 2.500000
	printf("%.1f\n", div_2); // 2.500000

	//!!!!implicit conversion!!!!!

	float nine = 9;
	printf("%f", nine); //9.000000 
	// converted 9 to 9.000000
	// in other words: automatic conversion done by the compiler

	return 0;
}

