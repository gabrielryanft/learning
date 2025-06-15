#include <stdio.h>

int main(){
	int integer = 12;
	float little_float = 1.1234567;
	double long_float = 1.12345678912345;
	char character = 'B';

	printf("d: %d \t i: %i \n", integer, integer);
	printf("f: %f \t F: %F \n", little_float, little_float);
	printf("lf: %lf\n", long_float); //Long float = %lf
	printf("c: %c\n", character); 
}
