#include <stdbool.h>
#include <stdio.h>

int main(){
	bool not_true = false;
	bool yes_true = true;

	printf("false: %d\n", not_true);	// 0
	printf("true: %d\n", yes_true);	// 1

	printf("1 == 1 \t: %d\n", 1 == 1);
	printf("2 == 1 \t: %d\n", 2 == 1);
	printf("1 < 1 \t: %d\n", 1 < 1);
	printf("1 <= 1 \t: %d\n", 1 <= 1);
	printf("1 >= 1 \t: %d\n", 1 >= 1);
	return 0;
}
