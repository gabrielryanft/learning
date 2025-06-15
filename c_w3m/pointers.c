#include <stdio.h>

int main (){

	int i = 1;
	int *po = &i;
	int *pi = po;

	printf("%d\n", i );
	printf("%d\n", *po );
	printf("%d\n", *pi );
	return 0;
}
