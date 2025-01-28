#include <stdio.h>

int main (){

	// "pointers allow direct manipulation of data in memory"
	int num = 10;
	// poingter and target:
	int * poin = &num;
	printf("%p\n", poin); // prints the memory address in hex
	printf("%p\n", *poin); // print the value of num in hex
	// * is known as "dereferencer", as it is "transforming" the mamoru addr hex in the var value.
	// [int * pinter = var] and [printf("%p", *pointer)] are different things 
	// int * ... makes a pointer
	// *pointer translates the pointer into a value


	printf("%p\n", &num); // print some large hexadecimal number
	// %p is to print the pointer to the memory block of the var. It is necessary to use the & to point to the memory address
	printf("%p\n", num); // print 0xa bacause 0x = hexadecimal "identifier" and a = 10 in hexadecimal 

	return 0;
}
