#include <stdio.h>

int main (){
	int i_one = 1;						// 2 or 4 bytes
	int zi_one = 0;						// 2 or 4 bytes
	int ni_one;						// 2 or 4 bytes
	float f_one = 1.1;					// 4 bytes
	float bf_one = 1.111111;			// 4 bytes
	float nf_one;			// 4 bytes
	double d_one = 1.11;				// 8 bytes
	double bd_one = 1.1111111111111111;	// 8 bytes
	double nd_one;	// 8 bytes
	char  c_g = 'g';					// 1 byte
	char  n_c;					// 1 byte

	printf("i_one: %lu\n", sizeof(i_one));
	printf("zi_one: %lu\n", sizeof(zi_one));
	printf("ni_one: %lu\n", sizeof(ni_one));
	printf("f_one: %lu\n", sizeof(f_one));
	printf("bf_one: %lu\n", sizeof(bf_one));
	printf("nf_one: %lu\n", sizeof(nf_one));
	printf("d_one: %lu\n", sizeof(d_one));
	printf("bd_one: %lu\n", sizeof(bd_one));
	printf("nd_one: %lu\n", sizeof(nd_one));
	printf("c_g: %lu\n", sizeof(c_g));
	printf("n_c: %lu\n", sizeof(n_c));
	// lu = long unsigned integer = 0 to 4,294,967,295
	// diferent from a normal int: -2,147,483,648 to 2,147,483,647
	// the ul just "stacks everythng in the positive side."

	// even when there is nothing inside the var, it have the "normal" size.

	/*
	i_one: 4
	zi_one: 4
	ni_one: 4
	f_one: 4
	bf_one: 4
	nf_one: 4
	d_one: 8
	bd_one: 8
	nd_one: 8
	c_g: 1
	n_c: 1
	*/

	return 0;
}
