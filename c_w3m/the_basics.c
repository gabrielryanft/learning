#include <stdio.h>

/*int main(){*/
/*	printf("Hello world!\n"); // This is a comment*/
/*	return 0;*/
/*}*/

int main(){
	int number = 1;			// printf: "%d"
	float num_ber = 1.5;	// printf: "%f"
	char not_num = 'G';		// printf: "%c"
	// Put the %d (inside double quotes)
	// for the variable to be read (and outputed)
	printf("d: %d\t i: %i\n", number, number);	//using %d and %i to print
	printf("f: %f\n", num_ber);
	printf("c: %c\n", not_num);

	// Placeholder with no variables
	printf("int: %d\t float: %f\t char: %c\n\n", 10, 5.777, 'P');

	int x = 10;
	int y = 2;

	x = 100;
	y = x / 5;	// can do with other operators too

	y = 30;

	// Operations
	printf("x: %d\t y: %d\n", x, y);
	printf("x + y = %d\n", x + y);	// +
	printf("x * y = %d\n", x * y);	// *
	printf("x / y = %d\n", x / y);	// /
	printf("x - y = %d\n", x - y);	// -
	printf("x % y = %d\n", x % y);	// %

	int one = 1, two = 2, three = 3;
	printf("one: %d \t two: %d \t three: %d \t\n", one, two, three);

	one = two = three = 0;
	printf("one: %d \t two: %d \t three: %d \t\n", one, two, three);

	/*
	 * You can name a variable with a underscore at the beggining;
	*/
	char _letter = 'g';
	char __letter = 'A';
	printf("_: %d, __: %d\n", _letter, __letter);

	return 0;
}

/*
this is
a
multi line
commant
*/
