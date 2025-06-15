#include <stdio.h>

int main () {
	int base = 10;
	int height = 5;
	int area;

	area = base * height;

	// Octal result/data
	printf("Octal\n");
	printf("base: %o\t height: %o\n", base, height);	// %o is octal
	printf("area: %o\n\n", area);

	// Binary result/data
	printf("Binary\n");
	printf("base: %b\t height: %b\n", base, height);	// %b is binary
	printf("area: %b\n\n", area);

	printf("Decimal\n");
	printf("base: %d\t height: %d\n", base, height);
	printf("area: %d\n\n", area);

	return 0;
}
