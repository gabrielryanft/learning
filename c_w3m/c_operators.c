#include <stdio.h>

// OPERATORS

int main(){
	// the groups of operetots are:
	// arithmetic  operators
	// assignment  operators
	// comparision operators
	// logical     operators
	// bitwise     operators
	
	int one = 1;
	int two = 2;

	int result;
	float _result;

	// ARITHMETIC OPERATORS
	result = two + one;
	printf("two + one: %d\n", result);
	result = two - one;
	printf("two - one: %d\n", result);
	result = two * one;
	printf("two * one: %d\n", result);
	result = two / one;
	printf("two / one: %d\n", result);
	result = two % one;
	printf("two %% one: %d\n", result);
	result = ++two;
	// or, for two recive itself + 1
	// two++;
	printf("++two: %d\n", result);
	result = --one;
	// or, for one recive itself - 1
	// one--
	printf("--one: %d\n\n", result);

	// ASSIGNMENT OPERATORS

	result = 3;
	printf("r = 3: %d\n", result);

	result += 1;
	printf("r += 1: %d\n", result);
	result -= 1;
	printf("r -= 1: %d\n", result);
	result *= 1;
	printf("r *= 1: %d\n", result);
	result /= 1;
	printf("r /= 1: %d\n", result);
	result %= 1;
	printf("r %= 1: %d\n", result);

	result = 3;
	printf("r = 3: %d\n\n", result);

	// Binary assignment oparetor.

	result &= 4; // AND 
	printf("r &= 1: %d\n", result);
	result |= 1; //or
	printf("r |= 1: %d\n", result);
	result ^= 1; // zor
	printf("r ^= 1: %d\n", result);
	result >>= 1;
	printf("r >>= 1: %d\n", result);
	result <<= 1;
	printf("r <<= 1: %d\n\n", result);

	// COMPARISION OPERATORS
	// when printing the result as a integer, 
	// 1 = true;
	// 0 = false.

	result = one == two;
	printf("one == two: %d\n", result);
	result = one != two;
	printf("one != two: %d\n", result);
	result = one < two;
	printf("one < two: %d\n", result);
	result = one > two;
	printf("one > two: %d\n", result);
	result = one <= two;
	printf("one <= two: %d\n", result);
	result = one >= two;
	printf("one >= two: %d\n", result);

	return 0;
}


































