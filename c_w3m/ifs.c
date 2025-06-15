#include <stdio.h> 
#include <stdbool.h>

int main () {
	bool is_true = true;
	bool is_false = false;

	if (is_false){
		printf("true\n");
	} else {
		printf("false\n");
	} // false

	if (is_true){
		printf("true\n");
	} else {
		printf("false\n");
	} // true

	if (12 != 40){ // == <= >= < > !=
		printf("true\n");
	} else {
		printf("false\n");
	} // true

	if (12 == 40){
		printf("true\n");
	} else if (12 >= 6){
		printf("first was false\n");
	} else {
		printf("first and second was false\n");
	} // true

	// psychopath shorthand
	// ternary operator
	( 1 == 1 ) ? printf("true") : printf("false");

	return 0;
}
